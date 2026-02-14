"""
Filename: modbusManager.py
Author: Cooper Parlee <cooper.parlee@mma.edu>
Date: 01-14-2026
Description: Manager for modbus addresses
"""

from pymodbus.server import StartAsyncTcpServer
from pymodbus.datastore import ModbusServerContext, ModbusDeviceContext
from pymodbus.datastore import ModbusSequentialDataBlock
import asyncio

from src.devices.device import Device

class ModbusManager:
    async def updateSensors(self, context : ModbusServerContext):
        server_context = context[1]
        while True:
            await asyncio.sleep(0.1)
            for sensorAddress in self.addresses:
                sensor = self.addresses[sensorAddress]
                for address in sensor.getAddresses():
                    #print(address)
                    value = sensor.get() * sensor.getScale()
                    #print(f"Updating sensor on address {address} to {value}")
                    server_context.setValues(4, address, [int(value)])


    async def run_server(self, address="127.0.0.1", port = 5020):
        # Initialize the datastore for the 4 i/o classes
        self.store = ModbusDeviceContext(
            di = ModbusSequentialDataBlock(100, [False]*100), # discrete inputs (100) - read only
            co = ModbusSequentialDataBlock(200, [False]*100), # coils (100) - read/write bits
            hr = ModbusSequentialDataBlock(300, [1]*100), # holding registers (read/write 16-bits)
            ir = ModbusSequentialDataBlock(400, [2]*100), # input registers (100) - read only 16-bit
        )

        context = ModbusServerContext(devices=self.store, single=True) # Create context containing one store as single context

        asyncio.create_task(self.updateSensors(context))
        asyncio.create_task(self.monitorHoldingRegisters(context))

        await StartAsyncTcpServer(context=context, address=(address, port))

    def __init__(self):
        self.addresses = {}
        self.holding_register_cache = {} # store last holding register status
        self.holding_register_callbacks = {} # Store callbacks for addresses

        self.lastFree = 400

    def register_hr_callback (self, address, callback):
        """
        Saves a method to execute (inside or outside of thread) to call if the specific
        holding register address changes.

        Args:
            address (int): the holding register to monitor
            callback (function): Function to call with signature callback(address, old_value, new_value)
        """

        if address not in self.holding_register_callbacks:
            self.holding_register_callbacks[address] = []
        self.holding_register_callbacks[address].append(callback)

    async def monitorHoldingRegisters(self, context: ModbusServerContext):
        server_context = context[1]

        while True:
            await asyncio.sleep(0.05)

            current_vals = server_context.getValues(0x03, 300, count=99)
            addresses = range(300, 400)

            for i in range(len(current_vals)):
                val = current_vals[i]
                address = addresses[i]
                old_val = self.holding_register_cache.get(address)
                if(old_val != val):
                    print(f"address changed to {val}")
                    if address in self.holding_register_callbacks:
                        for callback in self.holding_register_callbacks[address]:
                            try:
                                await callback(address, old_val, val)
                            except Exception as e:
                                print(f"Error in callback for address {address}: {e}")
                    self.holding_register_cache[address] = val



    def addSensor(self, device: Device, address=-1):
        if (address == -1):
            # Find next empty id
            for i in range(self.lastFree, 499):
                if i not in self.addresses:
                    address = i
                    print(i)
                    self.lastFree = i+1
                    break
            if (address == -1): 
                raise LookupError("Unable to find an empty sensor id in the specified range")
        print(f"Add sensor to address {address}")
        self.addresses[address] = device
        device.addAddress(address)
        print("Successfully added device")
        
    def addSensors(self, devices: list[Device]):
        for device in devices:
            if isinstance(device, Device):
                self.addSensor(device)
