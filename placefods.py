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

def place_doublebond(self,other,dist, planeatom = None):
    """places two FODs above and below plane between two atoms"""

    midpoint = (self + other) * 0.5

    v1 = self - other
    if planeatom == None: 
        v2 = v1 + Point(0.0,0.0,1.0)
    else:
        v2 = self - planeatom 
    #define vector normal to plane
    n = v1.cross(v2)
    n = normalize(n) 

    #place FOD above and below plane
    p1 = midpoint + n*dist
    p2 = midpoint - n*dist
    pointlist = [p1,p2]

    printfods(pointlist)

def place_tetrahedron(self,tsize,bondatom = None, alignatom = None):
    """Places tetrahedron at given point
    top of tetrahedron points toward bond atom"""
    
    atom_center=self #atom center
    if bondatom == None:
        vbond = atom_center + Point(0.0,0.0,1.0)
    else:
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
    
    print('rotating tetrahedron to point to bond vector:',vbond)
    
    #define axis of rotation as point perpendicular to top and vbond
    n = vtop.cross(vbond)

    if norm(n) == 0.0:
        if vbond.x < 0.0:
            theta = math.pi #180 degrees
        else:
            print('already aligned')
            theta = 0.0
    else:
        n = normalize(n) #normalize
        #print('normalized n',n)
        
        #define angle of rotation as angle between top and vbond
        #theta = acos( a.b / ||a||*||b|| )
        theta = vtop.dot(vbond) / (norm(vtop)*norm(vbond))
        theta = math.acos(theta)

    print('by theta: {0:4.4f}'.format(theta))
    
#Rotate tetrahedron to point along bond
    newlist = pointlist 
    for i, point in enumerate(newlist):
        #rotate around n by theta
        pointlist[i] = point.rotatearound(n,theta)

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
        theta = a1.dot(a2) / (norm(a1)*norm(a2))
        theta = math.acos(theta)

        newlist = pointlist
        print('by theta: {0:4.4f}'.format(theta))
        for i, point in enumerate(newlist):
           pointlist[i] = point.rotatearound(n,theta) 

    print()
#translate back
    newlist = pointlist
    for i, point in enumerate(newlist): 
        #translate to atom center
        pointlist[i] = point + atom_center

    #print('printing to file')
    printfods(pointlist)
        
def printfods(self):
    """"prints fods to xyz"""
    f1 = open('tmp.xyz','a')
    for point in self:
        line=' H {0:10.6f} {1:10.6f} {2:10.6f} \n'.format(point.x,point.y,point.z)
        f1.write(line)

    f1.close()
