from numba import jit, njit, guvectorize, float64, float32, vectorize, prange
import numba
import numpy as np
import timeit
import math
from numba.experimental import jitclass

GRAVITY = -2.959e-4 #6.673*(10**-11)

class Nbody():
 
    def __init__(self, mass: float, position, initialVelocity):
        self.mass = mass
        self.velocity = np.array(initialVelocity, dtype=np.float)
        self.position = np.array(position, dtype=np.float)

    def updateVelocity(self, obj, time):
        time = time
        uv(self.position, obj.position, time, obj.mass, self.velocity)

    def updatePosition(self, time):
        time = time
        up(self.position, self.velocity, time)

@njit
def magnitudes(array):
    sum = 0
    for i in array:
        sum += math.pow(i,2)
    return sum


@guvectorize([(float64[:], float64[:], float64, float64, float64[:])], '(n), (n), (), (), (n)')
def uv(self, obj, time, mass, velocity):
    distance = self - obj
    magnitude = magnitudes(distance)
    acceleration = (-2.959e-4 * mass / (math.pow(magnitude, 1.5))) * distance
    velocity += acceleration * time


def  up(self, velocity, time):
    self += velocity * time


def update(planets):
    for i in range(300):
        for p in planets:
            for p2 in planets:
                if p2 != p:
                    p.updateVelocity(p2, 0.001)
            p.updatePosition(0.001)
