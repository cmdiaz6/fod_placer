#!/usr/bin/env python3
import os
import math
from pointclass import * 
from placefods import *
from placeatoms import *

def place_core(atom, centeratom, pol = 'pol', bondatom = None, alignatom = None):
    """call place atom core"""
    print('--atom',atom,pol)
    if atom == 'he' or atom == 'helium' or atom == '2':
        place_helium(centeratom, pol)
        nfods = 1
    elif atom == 'ne' or atom == 'neon'  or atom == '10':
        place_neon(centeratom, bondatom, alignatom, pol=pol)
        nfods=5
    elif atom == 'ar' or atom == 'argon' or atom == '18':
        place_argon(centeratom, bondatom, alignatom, pol=pol)
        nfods = 9

    if pol == 'pol': nfods*=2
    return nfods
