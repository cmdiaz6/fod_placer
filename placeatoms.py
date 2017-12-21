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

    place_tetrahedron(centeratom,2.0,bondatom,alignatom)
    if bondatom is not None:
        bondatom = centeratom - 2.0*bondatom
    if alignatom is not None:
        alignatom = centeratom - 2.0*alignatom

    place_tetrahedron(centeratom,1.0,bondatom,alignatom)

def place_argon(centeratom, bondatom = None, alignatom = None):
    pass

def place_COOH(carbon,oxy1,oxy2,hydrogen):
    pass
