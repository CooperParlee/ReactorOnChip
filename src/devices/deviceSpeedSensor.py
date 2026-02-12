"""
Filename: deviceSpeedSensor.py
Author: Cooper Parlee <cooper.parlee@mma.edu>
Date: 01-14-2026
Description: A basic class for reading pump speed sensor values
"""

from src.devices import Device, DevicePump, DeviceSensorBase

class DeviceSpeedSensor (Device, DeviceSensorBase):
    def __init__(self, attached_pump : DevicePump, scale = 1):
        super().__init__()
        self.attached_pump = attached_pump
        self.scale = scale
    def get(self):
        return self.attached_pump.getSpeed()
