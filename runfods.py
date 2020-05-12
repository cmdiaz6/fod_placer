import os
import math
from pointclass import * 
from placefods import *
from placeatoms import *

if os.path.exists('new.xyz'):
    os.remove('new.xyz')
    
center1=Point(-5,5,5)
tsize=1.3
bondatom=Point(0,0,0)
place_tetrahedron(center1,tsize,bondatom)

center1=Point(0,0,0)
tsize=1.3
bondatom=Point(-5,5,5)
place_tetrahedron(center1,tsize,bondatom)

center1=Point(10,10,10)
tsize=1.3
bondatom=Point(5,5,5)
place_tetrahedron(center1,tsize,bondatom)


# place 1 FOD
center1=Point(5,5,5)
place_fod(center1)

center1=Point(-5,5,5)
place_fod(center1)

#place_COOH(Ocenter,directions)

center1=Point(10,0,0)
bondatom=Point(0,0,0)
#place_neon(center1,bondatom)
place_neon(center1,bondatom,pol='pol')
center1=Point(-10,0,0)
#place_argon(center1,bondatom)
place_argon(center1,bondatom,pol='pol')
center1=Point(0,10,0)
place_argon(center1,bondatom)

