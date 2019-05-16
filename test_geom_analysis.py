"""
Tests for geom_analysis.py
"""

import pytest
import geom_analysis as ga

def test_calculate_distance():
    coord1 = [0, 0, 2]
    coord2 = [0, 0, 0]

    observed = ga.calculate_distance(coord1, coord2)

    assert observed == 2

def test_bond_check():
    bond_distance = 1.47

    observed = ga.bond_check(bond_distance)

    assert observed == True

def tes_bond_check_false():
    bond_distance = 1.6

    observed = ga.bond_check(bond_distance)

    assert observed == False

def test_bond_check_error():
    bond_distance = 'a'

    with pytest.raises(TypeError):
	
        observed = ga.bond_check(bond_distance)
