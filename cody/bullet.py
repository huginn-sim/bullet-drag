# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 15:49:52 2014

@author: cody
"""
class bullet:
    def __init__(self, name, mass, bc, model):
        ''' Initializes a 'bullet' object with:

name -> Name given by manufacturer.
mass -> The mass (in grains) of the bullet.
bc -> Ballistic coefficient with respect to some reference (usually G1).
Dimensionless parameter which accounts for variations in the sectional
densities and drag coefficients of this 'bullet' and a reference bullet.
model -> The reference bullet used to model the 'bullet' object's trajectory.
'''
        from constants import convert

        self.name = name
        self.mass = convert(mass, f='grains', t='pounds')
        self.bc = bc
        self.m = model

    def __str__(self):
        return self.name

    def shoot(self, x, t):
        ''' Integration. '''
        from numpy import array, zeros, size
        from scipy import linalg
        
        from constants import g

        m = self.m

        v = array([x[2],x[3]])
        vm = linalg.norm(v)
        ax = -1*((m.A(vm)/self.bc)*(vm**(m.M(vm) - 1))*(x[2]/vm))/(self.mass)
        ay = -g - (((m.A(vm)/self.bc)*(vm**(m.M(vm) - 1))*(x[3]/vm)))/(self.mass)
        return array([x[2], x[3], ax, ay])