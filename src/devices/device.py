"""
Filename: device.py
Author: Cooper Parlee <cooper.parlee@mma.edu>
Date: 01-02-2026
Description: File for the class declaration for a generic device.
"""

from warnings import warn

class Device:
    addresses = []

    def getAddresses(self):
        return self.addresses
    
    def addAddress(self, address):
        if (type(address) is not int):
            raise TypeError("Address must be of type integer.")

        self.addresses.append(address)

    def removeAddress(self, address):
        if (address in self.addresses):
            self.addresses.remove(address)
        else:
            warn(f"Address {address} was not found and cannot be removed.")
