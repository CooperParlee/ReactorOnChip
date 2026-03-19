from random import uniform

class DeviceSensorBase():
    def getScale(self):
        return self.scale
    def doNoise(self, real):
        #print(self.scale * self.noise)
        return max(real + uniform(-self.noise, self.noise), 0)