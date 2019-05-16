# This is my geometry analysis python script
"""
Functions and script for geomtery analysis
"""

import os
import numpy
import sys

def calculate_distance(atom1, atom2):
    """
    Calculate the distance between two atoms.

    Parameters
    ----------
    atom1: list
	A list of coordinates [x, y, z]
    atom2: list
	A list of coordinates [x, y, z]

    Returns
    -------
    distance: float
	The distance between atoms.

    Examples
    --------
    >>> calculate_distance([0, 0, 0], [0, 0, 1])
    1.0
    """
    x_distance = atom1[0]-atom2[0]
    y_distance = atom1[1]-atom2[1]
    z_distance = atom1[2]-atom2[2]
    distance = numpy.sqrt(x_distance**2 + y_distance**2 + z_distance**2)
    return distance

def bond_check(bond_distance,minimum_value=0,maximum_value=1.5):
    """
    Determine whether a bond length fits within a specified, or default value.

    Parameters
    ----------
    bond_distance: float
	The distance between atoms.
    minimum_value=value: float
	The lowest allowable vaule for the distance of a bond
    maximum_value=value: float
	The highest allowable vaule for the distance of a bond

    Returns
    -------
    True if the bond distance is acceptable
    False if the bond distance is not acceptable
    """
    if bond_distance>minimum_value and bond_distance<maximum_value:
        return True
    else:
        return False

if __name__ == "__main__":
	if len(sys.argv) < 2:
	        raise IndexError('No file name given. This script requires an xyz file to run')

	file_path = sys.argv[1]

	coords_xyz = numpy.genfromtxt(fname=file_path, delimiter=None, dtype='unicode', skip_header=2)
	mol_sym = coords_xyz[:,0]
	xyz = coords_xyz[:,1:]
	xyz = xyz.astype(numpy.float)

	for numA, atomA in enumerate(xyz):
	    for numB, atomB in enumerate(xyz):
	        if numB<numA:
	            distance_AB = calculate_distance(atomA, atomB)
	            if bond_check(distance_AB) is True:
	                print(F'{mol_sym[numA]} to {mol_sym[numB]}: {distance_AB:.3F}')
