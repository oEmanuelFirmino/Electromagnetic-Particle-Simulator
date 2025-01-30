import numpy as np

class Particle:
    def __init__(self, q, m, E, B, v0, r0):
        self.q = q
        self.m = m
        self.E = np.array(E)
        self.B = np.array(B)
        self.v0 = np.array(v0)
        self.r0 = np.array(r0)

    def force(self, v):
        return (self.q / self.m) * (self.E + np.cross(v, self.B))
