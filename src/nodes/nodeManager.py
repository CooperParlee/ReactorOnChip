"""
Filename: nodeManager.py
Author: Cooper Parlee <cooper.parlee@mma.edu>
Date: 01-02-2026
Description: Class declaration for a program that manages the creation of nodes 
and the automatic assignment of node IDs.
"""
from node import Node

class NodeManager:
    # Default unit values
    default_temp = 'undefined'
    default_pressure = 'undefined'
    default_mflow = 'undefined'

    nodes: list[Node] = []

    def __init__(self, d_temp='K', d_press='kPa', d_mflow='kg/s'):
        self.default_temp = d_temp
        self.default_pressure = d_press
        self.default_mflow = d_mflow

    def addNode(self):
        nodeCt = self.nodes.len()
        node = Node(nodeCt)

        node.setPressureUnits(self.default_Pressure)
        node.setTemperatureUnits(self.default_Temperature)
        
        self.nodes.append(node)