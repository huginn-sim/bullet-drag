#~ Modules
from pylab import *
from scipy.integrate import ode, odeint
#/~ Modules

#~ Custom Modules
from viz import configure
#/~ Custom Modules

class bullet:
    def __init__(self, name, bc, samples, reference):
        ''' Initializes a 'bullet' object with:

            name        -> Name given by manufacturer.
            bc          -> Ballistic coefficient with respect to some reference (usually G1).
                           Dimensionless parameter which accounts for variations in the sectional
                           densities and drag coefficients of this 'bullet' and a reference bullet.
            reference   -> The reference bullet used to model the 'bullet' object's trajectory.
        '''
        self.name = name
        self.bc = bc
        self.__samples = samples
        self.__ref = reference[::-1]

    def __str__(self):
        return self.name

    def A(self, v):
        ''' Interpolate an A(v) value based on reference. '''
        ref = self.__ref
        for i in range(len(ref)):
            r = ref[i]
            if r[0] >= v:
                v1 = ref[i-1][0]; v2 = r[0]
                alpha = (v - v1) / (v2 - v1)

                return ref[i-1][1] + alpha*r[1]

        return 0.

    def M(self, v):
        ''' Interpolate an M(v) value based on reference. '''
        ref = self.__ref
        for i in range(1,len(ref)):
            r = ref[i]
            if r[0] >= v:
                v1 = ref[i-1][0]; v2 = r[0]
                alpha = (v - v1) / (v2 - v1)

                return ref[i-1][2] + alpha*r[2]

        return 0.

    def v(self, x):
        ''' Interpolate a 'v' based on a current x displacement. '''
        samples = sorted(self.__samples['velocity'].items())
        for i in range(1,len(samples)):
            s = samples[i]
            if s[0] >= x:
                v1 = samples[i-1][0]; v2 = s[0]
                alpha = (x - v1) / (v2 - v1)

                return samples[i-1][1] + alpha*s[1]

            return 0.

    def shoot(self, x, t):
        ''' Integration. '''
        v = abs(linalg.norm(np.array([x[2], x[3]])))
        ax = -x[2]*(self.A(v)/self.bc)*v**(self.M(v)-1)
        ay = -g - x[3]*(self.A(v)/self.bc)*v**(self.M(v)-1)

        return array([x[2], x[3], ax, ay])

if __name__ == "__main__":
    #~ State Variables
    g = 32
    t0 = 0; tf = .2; dt=.001;
    times = np.arange(t0, tf+dt, dt)
    #/~ State Variables

    #~ Bullet-specific Variables
    samples = {}
    samples['velocity'] = \
        {
            0:3300, 100:2889, 200:2514,
            300:2168, 400:1851, 500:1568
        }
    samples['energy'] = \
        {
            0:1209, 100:927, 200:701,
            300:522, 400:380, 500:273
        }
    samples['sr-trajectory'] = \
        {
            50:0., 100:.5, 150:0.,
            200:-1.7, 250:-4.8, 300:-9.4
        }
    samples['lr-trajectory'] = \
        {
            100:-.1, 150:1.3, 200:0.,
            250:-2.6, 300:-6.9, 400:-21.2, 500:-45.8
        }

    G1 = array([[ 4230 , 1.477404177730177e-04 , 1.9565 ],
                [ 3680 , 1.920339268755614e-04 , 1.925 ],
                [ 3450 , 2.894751026819746e-04 , 1.875 ],
                [ 3295 , 4.349905111115636e-04 , 1.825 ],
                [ 3130 , 6.520421871892662e-04 , 1.775 ],
                [ 2960 , 9.748073694078696e-04 , 1.725 ],
                [ 2830 , 1.453721560187286e-03 , 1.675 ],
                [ 2680 , 2.162887202930376e-03 , 1.625 ],
                [ 2460 , 3.209559783129881e-03 , 1.575 ],
                [ 2225 , 3.904368218691249e-03 , 1.55 ],
                [ 2015 , 3.222942271262336e-03 , 1.575 ],
                [ 1890 , 2.203329542297809e-03 , 1.625 ],
                [ 1810 , 1.511001028891904e-03 , 1.675 ],
                [ 1730 , 8.609957592468259e-04 , 1.75 ],
                [ 1595 , 4.086146797305117e-04 , 1.85 ],
                [ 1520 , 1.954473210037398e-04 , 1.95 ],
                [ 1420 , 5.431896266462351e-05 , 2.125 ],
                [ 1360 , 8.847742581674416e-06 , 2.375 ],
                [ 1315 , 1.456922328720298e-06 , 2.625 ],
                [ 1280 , 2.419485191895565e-07 , 2.875 ],
                [ 1220 , 1.657956321067612e-08 , 3.25 ],
                [ 1185 , 4.745469537157371e-10 , 3.75 ],
                [ 1150 , 1.379746590025088e-11 , 4.25 ],
                [ 1100 , 4.070157961147882e-13 , 4.75 ],
                [ 1060 , 2.938236954847331e-14 , 5.125 ],
                [ 1025 , 1.228597370774746e-14 , 5.25 ],
                [ 980 , 2.916938264100495e-14 , 5.125 ],
                [ 945 , 3.855099424807451e-13 , 4.75 ],
                [ 905 , 1.185097045689854e-11 , 4.25 ],
                [ 860 , 3.566129470974951e-10 , 3.75 ],
                [ 810 , 1.045513263966272e-08 , 3.25 ],
                [ 780 , 1.291159200846216e-07 , 2.875 ],
                [ 750 , 6.824429329105383e-07 , 2.625 ],
                [ 700 , 3.569169672385163e-06 , 2.375 ],
                [ 640 , 1.839015095899579e-05 , 2.125 ],
                [ 600 , 5.71117468873424e-05 , 1.950 ],
                [ 550 , 9.226557091973427e-05 , 1.875 ],
                [ 250 , 9.337991957131389e-05 , 1.875 ],
                [ 100 , 7.225247327590413e-05 , 1.925 ],
                [ 65 , 5.792684957074546e-05 , 1.975 ],
                [ 0 , 5.206214107320588e-05 , 2.000 ]])

    b = bullet("50 ATV BT", 0.942, samples, G1)
    #~/ Bullet-Specific Variables

    #~ Integrate
    y0 = [0., 0., 3300., 0.]
    states = odeint(b.shoot, y0, times)
    states = array(states)
    #/~ Integrate

    #~ Get Samples
    x = []; y = []
    for k in samples['sr-trajectory'].keys():
        x.append(k)
        y.append(samples['sr-trajectory'][k])
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
                ylabel=r'Height (feet)',
                xbounds=None, ybounds=None)

    fig.suptitle('Bullet Trajectory Simulation', size=30)
    fig.subplots_adjust(left=0.05, right=0.95, top=0.9, bottom=0.08)

    show()
    #/~ Plot