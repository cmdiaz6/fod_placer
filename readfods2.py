#!/usr/bin/env python3
import os
import math
from pointclass import * 
from placefods import *
from placecore import *

#check for input file
if os.path.exists('fod_input.test'):
    f1=open('fod_input.test')
else:
    print('no fod_input file found')
    raise SystemExit(0)

count=0
while True:
    line=f1.readline()
    if line == "":
        break
    args = line.split()
    narg = len(args)
    if narg == 0: #blank line
        continue

    #read atoms
    if args[0].lower() == 'atom':
        atm=args[1].lower()
        pol='pol'
        bondatom  = None
        alignatom = None
        nfods = 0
        while True:
            line=f1.readline()
            args = line.split()
            narg = len(args)
            if narg == 0:
                continue
            if args[0].lower() == 'end':
                print('placing atom ',atm,pol)
                nfods = place_core(atm,center,pol,bondatom,alignatom)
                #place_core(args[1],center,nfods,pol,sizes,bondatom,alignatom)
                count+=nfods
                break

            if args[0].lower() == 'center':
                center=Point(float(args[1]),float(args[2]),float(args[3]))
            elif args[0].lower() == 'pointto':
                bondatom=Point(float(args[1]),float(args[2]),float(args[3]))
            elif args[0].lower() == 'alignto':
                alignatom=Point(float(args[1]),float(args[2]),float(args[3]))
            elif args[0].lower() == 'sizes':
                # pass in all tetrahedron sizes
                pass
            elif args[0].lower() == 'spin':
                pol=args[1].lower()
                if pol == 'unpolarized': pol == 'unp'

    #TETRAHEDRON
    if args[0].lower() == 'tetrahedron':
        count+=4
        bondatom  = None
        alignatom = None
        spin = 'up'
        while True:
            line=f1.readline()
            args = line.split()
            narg = len(args)
            if narg == 0:
                continue
            if args[0].lower() == 'end':
                print('placing tetrahedron: align atom',alignatom)
                place_tetrahedron(center,tsize,bondatom,alignatom,spin)  
                break

            if args[0].lower() == 'center':
                center=Point(float(args[1]),float(args[2]),float(args[3]))
            elif args[0].lower() == 'size':
                tsize = float(args[1])
            elif args[0].lower() == 'pointto':
                bondatom=Point(float(args[1]),float(args[2]),float(args[3]))
            elif args[0].lower() == 'alignto':
                alignatom=Point(float(args[1]),float(args[2]),float(args[3]))
            elif args[0].lower() == 'spin':
                spin=args[1].lower()
                if spin == 'down': spin == 'dn'

    # point ax ay az
    elif args[0].lower() == 'fod':
        count+=1
        center=Point(float(args[1]),float(args[2]),float(args[3]))
        print('placing fod',center)
        spin = 'up'
        if len(args) == 5:
            if args[4] == 'down' or args[4] == 'dn':
                spin = 'dn'
        place_fod(center,spin)

    elif args[0].lower() == 'point':
        count+=1
        center=Point(float(args[1]),float(args[2]),float(args[3]))
        print('placing fod',center)
        place_fod(center)
   
    #DOUBLE BOND
    elif args[0].lower() == 'db' or args[0].lower() == 'doublebond':
        count+=2
        planeatom = None
        spin = 'up'
        while True:
            line=f1.readline()
            args = line.split()
            narg = len(args)
            if narg == 0:
                continue
            if args[0].lower() == 'end':
                print('placing doublebond')
                place_doublebond(atom1,atom2,dist,planeatom,spn=spin)
                break

            if args[0].lower() == 'atom1':
                atom1=Point(float(args[1]),float(args[2]),float(args[3]))
            if args[0].lower() == 'atom2':
                atom2=Point(float(args[1]),float(args[2]),float(args[3]))
            if args[0].lower() == 'distance':
                dist = float(args[1])
            if args[0].lower() == 'planeatom':
                planeatom=Point(float(args[1]),float(args[2]),float(args[3]))
            if args[0].lower() == 'spin':
                spin=args[1].lower()
                if spin == 'down': spin == 'dn'
            elif args[0].lower() == 'spin':
                spin=args[1].lower()
                if spin == 'down': spin == 'dn'
                

    elif args[0].lower() == 'tb' or args[0].lower() == 'triplebond':
        count+=3
        spin = 'up'
        while True:
            line=f1.readline()
            args = line.split()
            narg = len(args)
            if narg == 0:
                continue
            if args[0].lower() == 'end':
                print('placing triplebond')
                place_triplebond(atom1,atom2,dist,spn=spin)
                break

            if args[0].lower() == 'atom1':
                atom1=Point(float(args[1]),float(args[2]),float(args[3]))
            if args[0].lower() == 'atom2':
                atom2=Point(float(args[1]),float(args[2]),float(args[3]))
            if args[0].lower() == 'distance':
                dist = float(args[1])
            elif args[0].lower() == 'spin':
                spin=args[1].lower().strip()
                if spin == 'down': 
                    spin = 'dn'

print('DONE READING')

#write to xyz with number of FODS on first line
f2=open('new.xyz','w')
line = str(count) + '\n\n'
f2.write(line)

f1=open('tmp.xyz','r')
for line in f1:
    f2.write(line)

#remove tmp file
os.remove('tmp.xyz')

#center1=Point(-5,5,5)
#tsize=1.3
#bondatom=Point(0,0,0)
#place_tetrahedron(center1,tsize,bondatom)

# place 1 FOD
#center1=Point(5,5,5)
#place_fod(center1)

#place_COH(oxygencenter,directions)

