from time import time
from src.devices import DeviceThermal
class FluidParcelManager:
    class FluidParcel:
        def __init__ (self, parcelCode, element, startPosition, mass, material, temperature):
            self.parcelCode = parcelCode
            self.element = element
            self.position = startPosition
            self.mass = mass
            self.material = material
            self.temperature = temperature

    def determinePositionFromLen(self, len):
        for device in self.controlLoop.getDevices():
            if device.length > len:
                return device, len / device.length
            len -= device.length

    def __init__(self, nodeManager, controlLoop, material, startTemp = 290, n=20):
        self.nodeManager = nodeManager
        self.controlLoop = controlLoop
        self.material = material

        self.fluids = []

        totalVol = controlLoop.determineSysVol()
        totalMass = totalVol*material.density
        self.totalLength = controlLoop.getTotalSysLength()
        
        for i in range(n):
            len = i/n * self.totalLength
            #print(len)
            element, frac = self.determinePositionFromLen(len)
            parcel = FluidParcelManager.FluidParcel(i, element, frac, totalMass/n, self.material, startTemp)

            element.addParcel(parcel)
            self.fluids.append(parcel)

        self.lastTime = time()

    def update (self):
        dt = time() - self.lastTime
        for parcel in self.fluids:
            element = parcel.element
            if isinstance(element, DeviceThermal):
                #print("yes, is a thermal object")
                _totalmass = element.getContainedMass()
                print(element.parcels)
                dT = element.temperature - parcel.temperature

                energy = element.getHeatFlow(element.a_total * parcel.mass / _totalmass, dT, dt)
                element.updateThermalMass(energy/dt, dt) # test this
                parcel.temperature += energy/parcel.material.getSpecHeat()/parcel.mass

                #print(f"{parcel.mass} / {_totalmass}")

            v = element.flow / element.a
            dfrac = dt * v / element.length
            parcel.position += dfrac

            if parcel.position > 1:
                element.removeParcel(parcel)

                element = element.outlet_node.getOutletDevice()
                element.addParcel(parcel)
                element.inlet_node.setTemperature(parcel.temperature)
                parcel.element = element
                parcel.position = parcel.position % 1

        
        #print(self.fluids[0].element)

        self.lastTime = time()