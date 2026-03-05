from time import time
class FluidParcelManager:
    class FluidParcel:
        def __init__ (self, parcelCode, element, startPosition, mass, material, temperature):
            self.parcelCode = parcelCode
            self.element = element
            self.position = startPosition
            self.mass = mass
            self.material = material
            self.temperature = temperature

    def determinePositionFromLen(self, len):
        for device in self.controlLoop.getDevices():
            if device.length > len:
                return device, len / device.length
            len -= device.length

    def __init__(self, nodeManager, controlLoop, material, startTemp = 273, n=20):
        self.nodeManager = nodeManager
        self.controlLoop = controlLoop
        self.material = material

        self.fluids = []

        totalVol = controlLoop.determineSysVol()
        totalMass = totalVol/material.density
        self.totalLength = controlLoop.getTotalSysLength()
        
        for i in range(n):
            len = i/n * self.totalLength
            print(len)
            element, frac = self.determinePositionFromLen(len)
            parcel = FluidParcelManager.FluidParcel(i, element, frac, totalMass/n, self.material, startTemp)

            element.addParcel(parcel)
            self.fluids.append(parcel)

        self.lastTime = time()

        for parcel in self.fluids:
            print(parcel.element)

    def update (self):
        dt = time() - self.lastTime
        for parcel in self.fluids:
            v = parcel.element.flow / parcel.element.a
            dfrac = dt * v / parcel.element.length
            parcel.position += dfrac

            if parcel.position > 1:
                parcel.element.removeParcel(parcel)

                parcel.element = parcel.element.outlet_node.getOutletDevice()
                parcel.element.addParcel(parcel)
                parcel.element.outlet_node.setTemperature(parcel.temperature)
                parcel.position -= 1
        
        print(self.fluids[0].element)

        self.lastTime = time()