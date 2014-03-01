# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 16:06:23 2014

@author: cody
"""
class model:
    import model_data as md
    
    def __init__(self, V, Av, Mv, md):
        self.V = V
        self.Av = Av
        self.Mv = Mv
        self.md = md
        
    def A(self, ):
        ''' Interpolate an A(v) value based on reference round '''
        A = interp(V, flipud(self.md.G1[:,0]), flipud(self.md.G1[:,1]))
        return A

    def M(self, v):
        ''' Interpolate an M(v) value based on reference round '''
        M = interp(V, flipud(self.md.G1[:,0]), flipud(self.md.G1[:,2]))
        return M
        
if __name__ == "__main__":
    print "hello!"