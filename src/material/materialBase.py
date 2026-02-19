"""
Filename: materialBase.py
Author: Cooper Parlee <cooper.parlee@mma.edu>
Date: 02-14-2026
Description: File for the class declaration for a generic material.
"""

class MaterialBase:
    def __init__(self, density, viscosity, spec_heat):
        self.density = density
        self.viscosity = viscosity
        self.cp = spec_heat

    def getViscosity (self):
        """Get the viscosity of the material in m^2/s

        Returns:
            float: Viscosity of the contained media (m^2/s)
        """
        return self.viscosity
    
    def setViscosity(self, viscosity):
        """Set the viscosity of the contained media in m^2/s

        Args:
            viscosity (float): Viscosity of the contained media (m^2/s)
        """
        self.viscosity = viscosity
    
    def getDensity (self):
        """Get the density of the contained media in kg/m^3

        Returns:
            float: Density of the contained media in kg/m^3
        """

        return self.density
    
    def setDensity(self, density):
        """Set the density of the contained media in kg/m^3

        Args:
            density (float): Density of the contained media (kg/m^3)
        """

        self.density = density

    def getSpecHeat (self):
        """Returns the specific heat of the material in Joules/kg-K

        Returns:
            float: Returns Cp, a measure of required heat to raise the temperature of the material in J/kg-K
        """
        return self.cp


