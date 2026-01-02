"""
Filename: deviceInline.py
Author: Cooper Parlee <cooper.parlee@mma.edu>
Date: 01-02-2026
Description: File for the class declaration for a generic inline device.
"""
from warnings import warn
from device import Device
from nodes.node import Node
from nodes.nodeManager import NodeManager

class DeviceInline(Device):
    
    inlet_node: Node = -1
    outlet_node: Node = -1

    def computeDeltas(self):
        if (type(self.inlet_node) is Node and type(self.outlet_node) is Node):
            pass
        else:
            warn("Both inlet and outlet nodes must be defined to compute deltas.")
            
        # Always assume that flow rate will be the same into and out of a device
        self.outlet_node.setFlowRate(self.inlet_node.getFlowRate())
    
    def __init__(self, manager : NodeManager, inlet=-1, outlet=-1):
        # Initialize nodes if inlet or outlet go unspecified.
        if (inlet == -1):
            inlet = manager.addNode()
        if (outlet == -1):
            outlet = manager.addNode()
        self.inlet_node = inlet
        self.outlet_node = outlet
        

