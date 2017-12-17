#!/usr/bin/env python
"""class for 3D point in space
also used for operations on vectors center at origin"""
import math

__author__ = "Carlos Diaz"

class Point:
    def __init__(self, x = 0.0, y = 0.0, z = 0.0):
        self.x, self.y, self.z = x, y, z

    def __str__(self):
        return "({0},{1},{2})".format(self.x,self.y,self.z)

    def __add__(self,other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return Point(x,y,z)

    def __sub__(self,other):
        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z
        return Point(x,y,z)
    
    def __mul__(self,other):
        """multiply Point() by float on right side"""
        x = self.x * other
        y = self.y * other
        z = self.z * other
        return Point(x,y,z)
    #def __rmul__(self,other):
        
    def __div__(self,other):
        """divide Point() by float"""
        x = self.x / other
        y = self.y / other
        z = self.z / other
        return Point(x,y,z)
    
    def dot(self,other):
        """dot product between two vectors"""
        x = self.x * other.x
        y = self.y * other.y
        z = self.z * other.z
        return x+y+z

    def cross(self,other):
        """cross product between two vectors"""
        x = self.y*other.z - self.z*other.y
        y = self.z*other.x - self.x*other.z
        z = self.x*other.y - self.y*other.x
        return Point(x,y,z)

    def rotatearound(self,n,t):
        """Rodrigues' rotation formula"""
        #vrot = self*math.cos(t) + n.cross(self)*math.sin(t) + n*n.dot(self)*(1-math.cos(t))
        vrot = self*math.cos(t) + n.cross(self)*math.sin(t) + n*n.dot(self)*(2*math.sin(t/2)**2) #more stable according to Yoh
        return vrot

def normalize(self):
    """normalize vector"""
    normalized_self = self * (1/norm(self))
    return normalized_self

def norm(self):
    norm=math.sqrt(self.x*self.x + self.y*self.y + self.z*self.z)
    return norm

