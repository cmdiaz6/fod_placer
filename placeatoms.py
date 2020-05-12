#!/usr/bin/env python3
"""places FOD tetrahedron"""

import os
import math
from pointclass import *
from placefods import *

__author__ = "Carlos Diaz"
__credits__ = ["Carlos Diaz"]
__maintainer__ = "Carlos Diaz"

    
def place_neon(centeratom, bondatom = None, alignatom = None, pol = 'unp'):
    """places two tetrahedra, 2nd one inverted"""
    dist=1.07966 #PBE
    place_fod(centeratom)
    place_tetrahedron(centeratom,dist,bondatom,alignatom)

    if pol == 'pol':
        if bondatom is not None:
            bondatom = 2.0*centeratom - bondatom
        if alignatom is not None:
            alignatom = 2.0*centeratom - alignatom

        place_fod(centeratom,'dn')
        place_tetrahedron(centeratom,dist,bondatom,alignatom,spn='dn')

def place_argon(centeratom, bondatom = None, alignatom = None, pol = 'unp'):
    """places four tetrahedra"""
    dist=3.869 #PBE
    #dist2=1.33 #inner tetrahedron
    place_tetrahedron(centeratom,dist,bondatom,alignatom)
    if bondatom is not None:
        bondatom = 2.0*centeratom - bondatom
    if alignatom is not None:
        alignatom = 2.0*centeratom - alignatom

    if pol == 'pol':
        place_tetrahedron(centeratom,dist,bondatom,alignatom,spn='dn')
      
    place_neon(centeratom,bondatom,alignatom,pol)

def place_COOH(carbon,oxy1,oxy2,hydrogen):
    pass
