# -*- coding: utf-8 -*-
"""
.. module:: main

.. moduleauthor:: Huginn
"""

#~ Modules
from numpy import interp
from pylab import *
from scipy.integrate import ode, odeint
#/~ Modules

#~ Custom Modules
from bullet import bullet
from model import *
from viz import configure
#/~ Custom Modules

def find_angle(sight, vm, b, times, theta=0.0003, error=.0001, n=1000):
    for i in range(n):
        y0 = [0., 0., vm*cos(theta), vm*sin(theta)]
        states = odeint(b.shoot, y0, times)
        states = array(states)

        # Interpolate a y-value given the model predictions.
        yf = interp(sight, states[:,0]/3., states[:,1]/3.)
    
        # If the y-value is greater than the error, halve the angle.
        if yf > error:
            theta = theta*.5
        # If the y-value is less than the error, raise the angle.
        elif yf < -error:
            theta = theta*1.5
        # Else, the angle is good enough.
        else:
            return theta

    return None

def main():
	#~ State Variables
    t0 = 0; tf = .3; dt=.001;
    times = arange(t0, tf+dt, dt)
    #/~ State Variables

    #~ Bullet-specific Variables
    name = '50 ATV BT'
    b = bullet(name, mass=50., bc=0.242, model=G1)
    #~/ Bullet-Specific Variables

    #~ Get Samples
    from sample_data import samples
    vm = samples[name]['v'][:,1][0]
    sight = samples[name]['st'][:,0][2]
    
    x = samples[name]['st'][:,0]
    y = samples[name]['st'][:,1]
    #/~ Get Samples

    #~ Integrate
    theta = find_angle(sight, vm, b, times)
    print "THETA:", theta

    y0 = [0., 0., vm*cos(theta), vm*sin(theta)]
    states = odeint(b.shoot, y0, times)
    states = array(states)
    #/~ Integrate

    #~ Plot
    fig, ax = subplots()

    r_mark, = ax.plot(x, y, 'ro-', alpha=.8)
    b_mark, = ax.plot(states[:,0]/3., states[:,1]*12., 'b-', lw=3, alpha=.8)

    legend( [r_mark, b_mark],
            ['Sample Trajectory',
             'Simulated ('+str(b)+')'],
            numpoints=1)

    configure(  ax=ax,
                title=r'G1 Model of Remington .233 cartridge'+'\n'+r'$\theta\approx'+str(round(theta,6))+r'$ radians',
                xlabel=r'Horizontal Displacement (yards)',
                ylabel=r'Height (inches)',
                xbounds=None, ybounds=None)

    fig.suptitle('Bullet Trajectory Simulation', size=30)
    fig.subplots_adjust(left=0.05, right=0.95, top=0.9, bottom=0.08)

    show()
    #/~ Plot

if __name__ == "__main__":
    main()