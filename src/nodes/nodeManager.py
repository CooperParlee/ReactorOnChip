"""
Filename: nodeManager.py
Author: Cooper Parlee <cooper.parlee@mma.edu>
Date: 01-02-2026
Description: Class declaration for a program that manages the creation of nodes 
and the automatic assignment of node IDs.
"""
from src.nodes.node import Node

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

    def addNode(self, node : Node):
        nodeCt = len(self.nodes)
        if(Node is None or not isinstance(node, Node)):
            node = Node(nodeCt)

        node.setPressureUnits(self.default_pressure)
        node.setTemperatureUnits(self.default_temp)
        
        self.nodes.append(node)
    def update(self):
        for node in self.nodes:
            node.update()