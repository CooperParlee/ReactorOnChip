"""
Filename: materialWater.py
Author: Cooper Parlee <cooper.parlee@mma.edu>
Date: 02-14-2026
Description: File for the class declaration for water.
"""
from src.material import MaterialBase
class MaterialWater(MaterialBase):
    def __init__(self):
        super().__init__(999, 1.02E-3, spec_heat = 4182)