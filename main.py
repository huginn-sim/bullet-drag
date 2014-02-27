#~ Modules
from pylab import *
from scipy.integrate import ode, odeint
#/~ Modules

#~ Custom Modules
from bullet import bullet
from model import *
from viz import configure
#/~ Custom Modules

def main():
	#~ State Variables
    
    t0 = 0; tf = .2; dt=.001;
    times = np.arange(t0, tf+dt, dt)
    #/~ State Variables

    #~ Bullet-specific Variables
    name = '50 ATV BT'
    b = bullet(name, mass=.5, bc=0.942, model=G1)
    #~/ Bullet-Specific Variables

    #~ Integrate
    y0 = [50., 0., 3300., 0.]
    states = odeint(b.shoot, y0, times)
    states = array(states)
    #/~ Integrate

    #~ Get Samples
    from sample_data import samples
    x = samples[name]['st'][:,0]; print len(x)
    y = samples[name]['st'][:,1]; print len(y)
    #/~ Get Samples

    #~ Plot
    fig, ax = subplots()

    r_mark, = ax.plot(x, y, 'ro', alpha=.8)
    b_mark, = ax.plot(states[:,0], states[:,1]*12., 'b-', lw=3, alpha=.8)

    legend( [r_mark, b_mark],
            ['Sample Trajectory',
             'Simulated ('+str(b)+')'],
            numpoints=1)

    configure(  ax=ax,
                title=r'G1 Model of Remington .233 cartridge',
                xlabel=r'Horizontal Displacement (feet)',
                ylabel=r'Height (inches)',
                xbounds=None, ybounds=None)

    fig.suptitle('Bullet Trajectory Simulation', size=30)
    fig.subplots_adjust(left=0.05, right=0.95, top=0.9, bottom=0.08)

    show()
    #/~ Plot

if __name__ == "__main__":
    main()