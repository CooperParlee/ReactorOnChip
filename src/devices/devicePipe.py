"""
Filename: devicePipe.py
Author: Cooper Parlee <cooper.parlee@mma.edu>
Date: 01-02-2026
Description: Class declaration for a pipe.
"""
from deviceInline import DeviceInline
from nodes.node import Node

class Pipe(DeviceInline):
    dimeter: float = -1.0
    length: float = -1.0
    roughness: float = 0.0 # TODO: figure out units for this

    def __init__ (self, inlet_node : Node, outlet_node : Node):
        super.__init__(self, inlet_node, outlet_node)

    def computeDeltas(self):
        super().computeDeltas()
