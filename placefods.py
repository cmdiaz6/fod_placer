#!/usr/bin/env python
"""places FOD tetrahedron"""

import os
import math
from pointclass import *

__author__ = "Carlos Diaz"
__credits__ = ["Carlos Diaz"]
__maintainer__ = "Carlos Diaz"

    
def place_fod(point):
    """"Places FOD at given point"""
    pointlist = [point]
    printfods(pointlist)

def place_doublebond(atom1,atom2, dist=1.0, planeatom = None):
    """places two FODs above and below plane between two atoms"""

    midpoint = (atom1 + atom2) * 0.5

    v1 = atom1 - atom2
    if planeatom == None: 
        v2 = v1 + Point(0.0,0.0,1.0)
    else:
        v2 = atom1 - planeatom 
    #define vector normal to plane
    n = v1.cross(v2)
    n = normalize(n) 

    #place FOD above and below plane
    p1 = midpoint + n*dist
    p2 = midpoint - n*dist
    pointlist = [p1,p2]

    printfods(pointlist)

def place_triplebond(atom1,atom2, dist=1.3):
    """places three FODs around midpoint between two atoms"""

    midpoint = (atom1 + atom2) * 0.5

    p1 = Point( 0.0,1.0,0.0) * dist
    p2 = Point(-math.sqrt(3)/2, -0.5, 0.0) * dist
    p3 = Point( math.sqrt(3)/2, -0.5, 0.0) * dist
    pointlist = [p1,p2,p3]

    #align norm of triangle with bond direction 
    vtop = p1.cross(p2)
    print('tp: vtop should point along Z-direction ',vtop)
    vbond = atom1 - atom2
    #define axis of rotation as point perpendicular to top and vbond
    n = vtop.cross(vbond)
    
    #rotate points around n, align vtop with vbond
    pointlist = rotatepoints(pointlist,n,vtop,vbond)
    
    #translate to midpoint
    pointlist = translatepoints(pointlist,midpoint)

    printfods(pointlist)


def place_tetrahedron(centeratom,tsize,bondatom = None, alignatom = None):
    """Places tetrahedron at given point
    top of tetrahedron points toward bond atom"""
    
    atom_center=centeratom #atom center
    if bondatom == None:
        vbond = atom_center + Point(0.0,0.0,1.0)
    else:
        vbond=bondatom   #bond direction
    
    #type: tetrahedron
    p1 = Point( 1.0, 1.0, 1.0) * tsize
    p2 = Point(-1.0,-1.0, 1.0) * tsize
    p3 = Point(-1.0, 1.0,-1.0) * tsize
    p4 = Point( 1.0,-1.0,-1.0) * tsize
    pointlist = [p1,p2,p3,p4]

    vtop = p1 #top of tetrahedron

    #translate vector to origin
    vbond = vbond - atom_center
    
    print('rotating tetrahedron to point to bond vector:',vbond)
    
    #define axis of rotation as point perpendicular to top and vbond
    n = vtop.cross(vbond)

    #rotate points around n, align vtop with vbond
    pointlist = rotatepoints(pointlist,n,vtop,vbond)

#OPTIONAL: ALIGN TETRAHEDRON
    if alignatom is not None:
        print('aligning atom to ',alignatom)
        b2=alignatom
        #new n: rotate along bond angle, keeps top p1 fixed
        n = pointlist[0]
        print('rotate around: ',n)
        #new theta = angle between normal vectors of planes (b1,center,b2) and (b1,center,p2) 
        #     (b2 x b1).(p2 x b1) /
        # ||(b2 x b1|| * || p2 x b1||
        a1 = b2.cross(vbond)
        a2 = pointlist[2].cross(vbond)

        #rotate points around n, align a1 with a2
        pointlist = rotatepoints(pointlist,n,a1,a2)

    print()
#translate back
    pointlist = translatepoints(pointlist,atom_center)

    printfods(pointlist)
        
def printfods(pointlist):
    """"prints fods to xyz"""
    f1 = open('tmp.xyz','a')
    for point in pointlist:
        line=' H {0:10.6f} {1:10.6f} {2:10.6f} \n'.format(point.x,point.y,point.z)
        f1.write(line)

    f1.close()
