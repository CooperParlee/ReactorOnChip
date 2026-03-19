from time import time

from src.util.dump import dump_arrays_to_excel

class DeviceThermal:
    def __init__(self, k_th = 1, a_total = 0, mass = 0, cp = 500, l_c = 0, temperature = 293):
        """Initializes the thermal properties of the device in question. Takes a thermal conductivity, k, a total conductive area, a,
        a thermal mass, mass, a characteristic length, l_c, and an initial temperature for the device.

        Args:
            k_th (double, optional): _description_. Defaults to 1.
            a_total (double, optional): _description_. Defaults to 0.
            mass (double, optional): _description_. Defaults to 0.
            cp (double, optional): specific heat capacity of the device in J/kg*K. Defaults to 500.
            l_c (double, optional): _description_. Defaults to 0.
            temperature (double, optional): _description_. Defaults to 293.
        """
        self.k_th = k_th
        self.temperature = temperature
        self.mass = mass
        self.cp = cp
        self.a_total = a_total
        self.r_cond = l_c/(k_th * a_total) # [K/W]
        h = 3000 # constant for now.
        self.r_conv = 1/(h*a_total)

        self.start_time = time()

        self.temp_array = []
        self.time_array = []
        self.debounce = False
    def getHeatFlow(self, area, dT, dt):
        """Returns the heat flow in Joules in the thermal object using a fractional area (determined elsewhere)
        and the resistance coefficient determined on the initialization of the function.

        Args:
            area (double): the fractional area in question
            dt (double): the temperature delta between the thermal device and the surrounding medium
        """
        R = (self.r_cond + self.r_conv) * (self.a_total / area)
        #u = 1/self.r_cond/area # [W/m^2-K]
        Q = dT/ R * dt

        #self.temperature -= Q/self.cp/self.mass

        if(self.verbose):
            # For logging purposes
            self.temp_array.append(self.temperature)
            self.time_array.append(time() - self.start_time)

            if (time() - self.start_time > 10 and not self.debounce): # takes an excel sized shit after 10 seconds
                dump_arrays_to_excel(self.time_array, self.temp_array, "thermal_log.xlsx", headers=("Time(s)", "Temperature(K)"))
                self.debounce = True

        return Q

    def updateThermalMass(self, Q, dt):
        """_summary_

        Args:
            Q (float): [W] heat flow into the mass
            dt (float): time delta since last calculated
        """
        self.temperature -= Q/self.cp/self.mass*dt