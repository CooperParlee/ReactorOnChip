"""
Filename: devicePump.py
Author: Cooper Parlee <cooper.parlee@mma.edu>
Date: 01-12-2026
Description: Device which takes a control setpoint and changes the inlet and outlet pressures of the adjacent nodes accordingly.
"""
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.nodes.nodeManager import NodeManager

from src.devices import DeviceInline
from warnings import warn
from time import time
from numpy import exp


class DevicePump (DeviceInline):
    def __init__(self, manager : "NodeManager", inlet=-1, outlet=-1, maxSpeed = 3480):
        super().__init__(manager, inlet, outlet)
        self.setpoint = 0
        self.processPoint = 0 # percent of pump maximum RPMs, used for updating the curve function
        self.lastPoint = 0
        self.lastSet = 0
        self.curve = lambda q: 0*q
        self.timeConst = 10 #seconds
        self.maxSpeed = maxSpeed

    def set(self, setpoint : float):
        if (setpoint > 1.0 or setpoint < 0):
            warn("Setpoint should be a floating point value between 0.0 and 1.0")
        self.setpoint = min(max(setpoint, 0), 1) # constrain the setpoint between 0 and 1
    
    def update(self):

        deltaT = time() - self.lastSet

        error = (self.setpoint - self.lastPoint) * (exp(-(deltaT)/self.timeConst))
        print(f"e: {error}")
        self.processPoint = self.setpoint - error
    def setPumpCurve (self, curve):
        if (not callable(curve)):
            raise TypeError("ERROR: Provided curve pointer is not a reference to a callable function.")
        else:
            self.curve = curve

    def getPumpCurve(self):
        """Returns the modified pump curve of the pump and is driven by the processPoint variable
        that is, what percent the pump is of its maximum efficient speed.

        Returns:
            Callable: A function that expects a flow rate double and returns the head provided by the pump at
            its current process point.
        """
        return lambda q: self.processPoint * self.curve(q*(1-self.processPoint))

    def setProcessPoint(self, sp):
        if (sp > 1.0 or sp < 0):
            warn("Process point should be a floating point value between 0.0 and 1.0")
        self.processPoint = min(max(sp, 0), 1)

    def getSpeed (self):
        return self.maxSpeed * self.processPoint

    async def processPointCallback(self, address, old, new):
        print(f"changing process point from {old} to {new}")
        self.lastPoint = self.processPoint
        self.lastSet = time()
        self.set(new/1000)
        #self.setProcessPoint(new/1000)
    
        
