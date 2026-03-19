from src.devices import DevicePlateHX
from typing import TYPE_CHECKING
from warnings import warn
if TYPE_CHECKING:
    from src.nodes.nodeManager import NodeManager

class special_DeviceInternalEngineHX(DevicePlateHX):
    def __init__(self, manager : 'NodeManager', inlet=-1, outlet=-1, k = 0, k_th=50, diameter=-1, temperature = 293, 
    mass = 0, cp = 500, l_c = 0.1, length = 1,
    area = 0, verbose=False, **kwargs):

        super().__init__(
            manager, inlet=inlet, outlet=outlet, diameter=diameter, length = length, k=k, k_th=k_th, temperature=temperature,
            mass=mass, cp=cp, l_c = l_c, area = area, verbose = verbose
        )

        self.engineLoad = 0
        self.enginePower = kwargs['engPwr'] # [kW]
        self.engineHeatRej = kwargs['engIneff'] # decimal representing how much heat is rejected to cooling water

    
    def updateThermalMass(self, Q, dt):
        super().updateThermalMass(Q-self.enginePower*1000*self.engineLoad*self.engineHeatRej, dt)

    async def updateEngineLoadCallback(self, address, old, new):
        if old is not None:
            print(f"Engine load: {old/100}>{new/100}")

        if (new > 100 or new < 0):
            warn(f"Engine load value of {new} is outside of acceptable range (0-100) okay.")
        self.engineLoad = max(min(new/100,1), 0)

