"""
Filename: magicNode.py
Author: Cooper Parlee <cooper.parlee@mma.edu>
Date: 01-02-2026
Description: A very strange node which can exist on its own and has a strange pattern
"""
from src.nodes.node import Node
from math import sin, pi

class MagicNode(Node):

    def __init__(self, id, frequency = 1/6):
        super().__init__(id)
        self.frequency = frequency
        

    def update(self):
        super().update()
        self.setTemperature(sin(self.timeSinceStart * self.frequency*2*pi))
        press = self.getPressure()
