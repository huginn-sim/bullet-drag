class model:
    def __init__(self, V, Av, Mv):
        self.V = V
        self.Av = Av
        self.Mv = Mv

    def A(self, v):
        ''' Interpolate an A(v) value based on reference. '''
        from numpy import interp
        return interp(v, self.V, self.Av)
        # for i in range(len(V)):
        #     r = V[i]
        #     if r >= v:
        #         v1 = self.V[i-1]; v2 = r
        #         alpha = (v - v1) / (v2 - v1)

        #         return self.Av[i-1] + alpha*self.Av[i]

        #return 0.

    def M(self, v):
        ''' Interpolate an M(v) value based on reference. '''
        from numpy import interp
        return interp(v, self.V, self.Mv)
        # V = self.V
        # for i in range(len(V)):
        #     r = V[i]
        #     if r >= v:
        #         v1 = self.V[i-1]; v2 = r
        #         alpha = (v - v1) / (v2 - v1)

        #         return self.Mv[i-1] + alpha*self.Mv[i]

        # return 0.

import model_data as md
G1 = model(md.G1[:,0], md.G1[:,1], md.G1[:,2])
G2 = model(md.G2[:,0], md.G2[:,1], md.G2[:,2])
G5 = model(md.G5[:,0], md.G5[:,1], md.G5[:,2])
G6 = model(md.G6[:,0], md.G6[:,1], md.G6[:,2])
G7 = model(md.G7[:,0], md.G7[:,1], md.G7[:,2])
G8 = model(md.G8[:,0], md.G8[:,1], md.G8[:,2])

if __name__ == "__main__":
    print "hello!"