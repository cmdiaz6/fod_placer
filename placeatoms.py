#!/usr/bin/env python3
"""places FOD tetrahedron"""

import os
import math
from pointclass import *
from placefods import *

__author__ = "Carlos Diaz"
__credits__ = ["Carlos Diaz"]
__maintainer__ = "Carlos Diaz"

def place_helium(centeratom, pol = 'pol'):
    """places 1 or 2 FODs"""
    place_fod(centeratom)
    if pol == 'pol':
        place_fod(centeratom,spn='dn')

def place_neon(centeratom, bondatom = None, alignatom = None, dist = 1.07966, pol = 'pol'):
    """places two tetrahedra, 2nd one inverted"""
    place_helium(centeratom,pol)
    place_tetrahedron(centeratom,dist,bondatom,alignatom)

    if pol == 'pol':
        if bondatom is not None:
            bondatom = 2.0*centeratom - bondatom
        if alignatom is not None:
            alignatom = 2.0*centeratom - alignatom

        place_tetrahedron(centeratom,dist,bondatom,alignatom,spn='dn')

def place_argon(centeratom, bondatom = None, alignatom = None, dist = 3.869, dist1 = 1.33, pol = 'pol'):
    """places four tetrahedra"""
    place_tetrahedron(centeratom,dist,bondatom,alignatom)
    if bondatom is not None:
        bondatom = 2.0*centeratom - bondatom
    if alignatom is not None:
        alignatom = 2.0*centeratom - alignatom

    if pol == 'pol':
        place_tetrahedron(centeratom,dist,bondatom,alignatom,spn='dn')
      
    place_neon(centeratom,bondatom,alignatom,dist1,pol)

def place_Na_core(centeratom, bondatom = None, alignatom = None, pol = 'pol'):
    """Sodium atom core FODs"""
    #spin up and spin down distances are different. taking the average for now
    place_neon(centeratom, bondatom, alignatom, dist=0.8907, pol=pol)

def place_K_core(centeratom, bondatom = None, alignatom = None, pol = 'pol'):
    """Theoretical Potassium atom core FODs"""
    #FODs do not actually look like this. spin-up are not tetrahedron
    place_argon(centeratom, bondatom = None, alignatom = None, dist=1.26919, dist1=0.35445, pol=pol)

def place_COOH(carbon,oxy1,oxy2,hydrogen):
    pass

