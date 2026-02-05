"""
Filename: deviceSensor.py
Author: Cooper Parlee <cooper.parlee@mma.edu>
Date: 02-05-2026
Description: A basic class for reading pressure sensor values
"""
from src.devices import DeviceParallel

class DevicePressureSensor (DeviceParallel):
    def get(self):
        super().get()
        return self.pressure
