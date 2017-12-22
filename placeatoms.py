#!/usr/bin/env python3
"""places FOD tetrahedron"""

import os
import math
from pointclass import *
from placefods import *

__author__ = "Carlos Diaz"
__credits__ = ["Carlos Diaz"]
__maintainer__ = "Carlos Diaz"

    
def place_neon(centeratom, bondatom = None, alignatom = None):
    """places two tetrahedra, smaller one inverted"""

    place_tetrahedron(centeratom,2/3,bondatom,alignatom)
    if bondatom is not None:
        bondatom = 2.0*centeratom - bondatom
    if alignatom is not None:
        alignatom = 2.0*centeratom - alignatom

    place_tetrahedron(centeratom,2/9,bondatom,alignatom)

def place_argon(centeratom, bondatom = None, alignatom = None):
    """places three tetrahedra"""
    place_tetrahedron(centeratom,2.0,bondatom,alignatom)
    if bondatom is not None:
        bondatom = 2.0*centeratom - bondatom
    if alignatom is not None:
        alignatom = 2.0*centeratom - alignatom
      
    place_neon(centeratom,bondatom,alignatom)

def place_COOH(carbon,oxy1,oxy2,hydrogen):
    pass
