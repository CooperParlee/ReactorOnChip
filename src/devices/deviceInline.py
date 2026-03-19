"""
Filename: deviceInline.py
Author: Cooper Parlee <cooper.parlee@mma.edu>
Date: 01-02-2026
Description: File for the class declaration for a generic inline device.
"""
from warnings import warn
from src.devices import Device
from src.nodes.node import Node
from typing import TYPE_CHECKING
from math import pi

if TYPE_CHECKING:
    from src.nodes.nodeManager import NodeManager

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
    
    def __init__(self, manager : 'NodeManager', inlet=-1, outlet=-1, k=0, diameter=-1, volume = -1, length = 1, verbose=False):
        super().__init__(k = k, verbose = verbose)
        # Initialize nodes if inlet or outlet go unspecified.
        if (inlet == -1):
            inlet = manager.addNode()
        if (outlet == -1):
            outlet = manager.addNode()
        self.inlet_node = inlet
        # Tells the node on the inlet to this device that this device is the outlet of the node.
        inlet.attachOutlet(self)
        self.outlet_node = outlet
        # Tells the node on the outlet of this device that this device is the inlet of the node.
        outlet.attachInlet(self)
        if (diameter == -1):
            self.diameter = manager.getDefaultDiameter()
        else:
            self.diameter = diameter

        self.a = (self.diameter ** 2 * pi / 4)
        self.length = length
        
        if (volume == -1):
            volume = self.computeVolume()

        self.volume = volume
        self.flow = 0
        self.containedMass = -1

        self.parcels = []

    def getInlet(self):
        return self.inlet_node

    def addParcel (self, parcel):
        self.parcels.append(parcel)
        self.computeContainedMass()
        self.getInlet().setTemperature(parcel.temperature)

    def removeParcel(self, parcel):
        if (parcel in self.parcels):
            self.parcels.remove(parcel)
        self.computeContainedMass()
    
    def setFlow(self, flow):
        self.flow = flow

    def getOutlet(self):
        return self.outlet_node

    def computeContainedMass(self):
        self.containedMass = 0
        for parcel in self.parcels:
            self.containedMass += parcel.mass

    def getContainedMass(self):
        if (self.containedMass == -1):
            self.computeContainedMass()
        return self.containedMass
    
    def computeVolume(self):
        return self.a * 0.5 * self.diameter

    def getDiameter(self):
        return self.diameter

    def computeMinorLoss(self, Q):

        g = 9.81
        v = Q / self.a

        return self.k * (v**2 / 2 / g)

    def computeHeatFlow(self, mdot, T_media):
        return 0
    def getVolume(self):
        return self.volume