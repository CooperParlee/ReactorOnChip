"""
Filename: deviceSensor.py
Author: Cooper Parlee <cooper.parlee@mma.edu>
Date: 01-14-2026
Description: A basic class for reading temperature sensor values
"""
from src.devices import DeviceParallel, DeviceSensorBase

class DeviceTempSensor (DeviceParallel, DeviceSensorBase):
    def __init__(self, attached_node, scale = 100):
        super().__init__(attached_node)
        self.scale = scale

    def get(self):
        super().get()
        return self.temp
