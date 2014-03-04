# -*- coding: utf-8 -*-
"""
.. module:: bullet

.. moduleauthor:: Huginn
"""

class bullet:
    def __init__(self, name, mass, bc, model):
        ''' Initializes a 'bullet' object with:

            name        -> Name given by manufacturer.
            mass        -> The mass (in grains) of the bullet.
            bc          -> Ballistic coefficient with respect to some reference (usually G1).
                           Dimensionless parameter which accounts for variations in the sectional
                           densities and drag coefficients of this 'bullet' and a reference bullet.
            model   -> The reference bullet used to model the 'bullet' object's trajectory.
        '''
        from constants import convert

        self.name = name
        self.mass = convert(mass, f='grains', t='pounds'); print self.mass
        self.bc = bc
        self.m = model

    def __str__(self):
        return self.name

    def shoot(self, x, t):
        ''' Integration. '''
        from numpy import array
        from scipy import linalg

        from constants import g

        m = self.m

        v = abs(linalg.norm(array([x[2], x[3]])))
        ax = -x[2]/v*(m.A(v)/self.bc)*v**(m.M(v)-1)/self.mass
        ay = -g - (x[3]/v*(m.A(v)/self.bc)*v**(m.M(v)-1))/self.mass

        return array([x[2], x[3], ax, ay])
