# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 16:05:28 2014

@author: cody
"""
#~ Modules
from pylab import *
from scipy.integrate import ode, odeint
#/~ Modules

#~ Custom Modules
from bullet import *
from model import *
from viz import configure
#/~ Custom Modules

def main():
    #~ State Variables
    
    t0 = 0; tf = 0.5; dt=.001;
    times = np.linspace(t0, tf, 200)
    #/~ State Variables

    #~ Bullet-specific Variables
    name = '50 ATV BT'
    b = bullet(name, mass=50, bc=0.242, model=G1)
    vtot = 3300 #
    theta = 0.05
    vxi = vtot*(cos(theta*pi/180))
    vyi = vtot*(sin(theta*pi/180))
    #~/ Bullet-Specific Variables

    #~ Integrate
    y0 = [0., 0., vxi, vyi]
    states = odeint(b.shoot, y0, times)
    states = array(states)
    #/~ Integrate

    #~ Get Samples
    from sample_data import samples
    x = samples[name]['st'][:,0]; #print len(x)
    y = samples[name]['st'][:,1]; #print len(y)
    #/~ Get Samples

    #~ Plot
    fig, ax = subplots()

    r_mark, = ax.plot(x, y, 'ro', alpha=.8)
    b_mark, = ax.plot(states[:,0], states[:,1]*12., 'bo', lw=3, alpha=.8)

    legend( [r_mark, b_mark],
            ['Sample Trajectory',
             'Simulated ('+str(b)+')'],
            numpoints=1)

    configure( ax=ax,
                title=r'G1 Model of Remington .233 cartridge',
                xlabel=r'Horizontal Displacement (yards)',
                ylabel=r'Height (inches)',
                xbounds=None, ybounds=None)

    fig.suptitle('Bullet Trajectory Simulation', size=30)
    fig.subplots_adjust(left=0.05, right=0.95, top=0.9, bottom=0.08)

    show()
    #/~ Plot

if __name__ == "__main__":
    main()