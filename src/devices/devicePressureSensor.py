"""
Filename: deviceSensor.py
Author: Cooper Parlee <cooper.parlee@mma.edu>
Date: 02-05-2026
Description: A basic class for reading pressure sensor values
"""
from src.devices import DeviceParallel
from src.devices import DeviceSensorBase

class DevicePressureSensor (DeviceParallel, DeviceSensorBase):
    def __init__(self, attached_node, scale = 100):
        super().__init__(attached_node)
        self.scale = scale
    def get(self):
        super().get()
        return self.pressure
