import os
import math
from pointclass import * 
from placefods import *


if os.path.exists('fod_input'):
    f1=open('fod_input')
else:
    print('no fod_input file found')
    raise SystemExit(0)

if os.path.exists('new.xyz'):
    os.remove('new.xyz')
    
for line in f1:
    args = line.split()
    narg = len(args)
    if narg == 0:
        continue

    # 0           1  2  3  4    5     6       7  8  9             10      11 12 13
    # tetrahedron ax ay az size tsize pointto bx by bz (optional: alignto cx cy cz)
    if args[0].lower() == 'tetrahedron':
        center=Point(float(args[1]),float(args[2]),float(args[3]))
        tsize = float(args[5])
        bondatom=Point(float(args[7]),float(args[8]),float(args[9]))
        place_tetrahedron(center,tsize,bondatom)

    # 0     1  2  3
    # point ax ay az
    elif args[0].lower() == 'point':
        center=Point(float(args[1]),float(args[2]),float(args[3]))
        place_fod(center)

print('DONE READING')

#center1=Point(-5,5,5)
#tsize=1.3
#bondatom=Point(0,0,0)
#place_tetrahedron(center1,tsize,bondatom)

# place 1 FOD
#center1=Point(5,5,5)
#place_fod(center1)

#place_COH(oxygencenter,directions)
