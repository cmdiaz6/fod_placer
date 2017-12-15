#!/usr/bin/env python
"""places FOD tetrahedron"""

import os
import math
from pointclass import *

__author__ = "Carlos Diaz"
__credits__ = ["Carlos Diaz"]
__maintainer__ = "Carlos Diaz"

    
def place_fod(self):
    """"Places FOD at given point"""
    pointlist = [self]
    printfods(pointlist)

def place_tetrahedron(self,tsize,bondatom, alignatom = None):
    """Places tetrahedron at given point
    top of tetrahedron points toward bond atom"""
    
    atom_center=self #atom center
    vbond=bondatom   #bond direction
    
    #type: tetrahedron
    numpoints = 4
    p1 = Point( 1.0, 1.0, 1.0) * tsize
    p2 = Point(-1.0,-1.0, 1.0) * tsize
    p3 = Point(-1.0, 1.0,-1.0) * tsize
    p4 = Point( 1.0,-1.0,-1.0) * tsize
    pointlist = [p1,p2,p3,p4]

    vtop = p1 #top of tetrahedron

    #translate vector to origin
    vbond = vbond - atom_center
    
    #print('rotating tetrahedron:',p1,p2,p3,p4)
    print('rotating tetrahedron')
    print('point to bond vector:',vbond)
    
    #define axis of rotation as point perpendicular to top and vbond
    n = vtop.cross(vbond)

    if norm(n) == 0.0:
        if vbond.x < 0.0:
            theta = math.pi #180 degrees
        else:
            print('already aligned')
            theta = 0.0
    else:
        n = n*(1/norm(n)) #normalize
        #print('normalized n',n)
        
        #define angle of rotation as angle between top and vbond
        #theta = acos( a.b / ||a||*||b|| )
        theta = vtop.dot(vbond) / (norm(vtop)*norm(vbond))
        theta = math.acos(theta)

    print('by theta:',theta)
    print()
    
#Rotate tetrahedron to point along bond
    newlist = pointlist 
    for i, point in enumerate(newlist):
        #rotate around n by theta
        pointlist[i] = point.rotatearound(n,theta)

#OPTIONAL: ALIGN TETRAHEDRON
    if alignatom is not None:
        b2=alignatom
        #new n: rotate along bond angle, keeps top p1 fixed
        n = p1 
        #new theta = angle between normal vectors of planes (b1,center,b2) and (b1,center,p2) 
        #     (b2 x b1).(p2 x b1) /
        # ||(b2 x b1|| * || p2 x b1||
        a1 = b2.cross(vbond)
        a2 = p2.cross(vbond)
        theta = a1.dot(a2) *(1/norm(a1))*(1/norm(a2))
        theta = math.acos(theta)

        newlist = pointlist
        for i, point in enumerate(newlist):
           pointlist[i] = point.rotatearound(n,theta) 

#translate back
    newlist = pointlist
    for i, point in enumerate(newlist): 
        #translate to atom center
        pointlist[i] = point + atom_center

    print('printing to file')
    printfods(pointlist)
        
def printfods(self):
    if os.path.exists('new.xyz'):
        f1=open('new.xyz','a')
        f1.write('\n')
    else:
        f1=open('new.xyz','a')
        line = ' ' + str(1) + '\n  #replace with # of FODS \n'
        f1.write(line)

    for point in self:
        line=' He ' + str(point.x) + ' ' + str(point.y) + ' ' + str(point.z) + '\n'
        f1.write(line)

    f1.close()
