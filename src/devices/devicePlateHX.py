"""
Filename: devicePlateHX.py
Author: Cooper Parlee <cooper.parlee@mma.edu>
Date: 01-30-2026
Description: File declaration for a basic heat exchanger.
"""

from src.devices import DeviceInline
from src.devices import DeviceThermal
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.nodes.nodeManager import NodeManager

class DevicePlateHX(DeviceInline, DeviceThermal):
    def __init__(self, manager : 'NodeManager', inlet=-1, outlet=-1, k = 0, k_th=50, diameter=-1, temperature = 293, 
    mass = 0, cp = 500, l_c = 0.1, length = 1,
    area = 0, verbose=False):
        DeviceInline.__init__(self, manager=manager, inlet=inlet, outlet=outlet, diameter=diameter, length = length, k=k, verbose=verbose)
        DeviceThermal.__init__(self, k_th=k_th, a_total=area, mass = mass, cp = cp, l_c = l_c, temperature = temperature)