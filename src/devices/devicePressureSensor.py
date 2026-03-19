"""
Filename: deviceSensor.py
Author: Cooper Parlee <cooper.parlee@mma.edu>
Date: 02-05-2026
Description: A basic class for reading pressure sensor values
"""
from src.devices import DeviceParallel
from src.devices import DeviceSensorBase

class DevicePressureSensor (DeviceParallel, DeviceSensorBase):
    def __init__(self, attached_node, scale = 100, noise = 0.05):
        super().__init__(attached_node)
        self.scale = scale
        self.noise = noise
    def get(self):
        super().get()
        return self.doNoise(self.pressure)
