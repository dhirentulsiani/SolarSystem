from numba import jit, njit, guvectorize, float64, float32, vectorize
import numba
import numpy as np
import timeit
import math

GRAVITY = -2.959e-4 #6.673*(10**-11)



class ObjectInSpace():
 
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

#@njit
def magnitudes(array):
    sum = 0
    for i in array:
        sum += i**2
    return sum**0.5


@guvectorize([(float64[:], float64[:], float64, float64, float64[:])], '(n), (n), (), (), (n)', target='cpu')
def uv(self, obj, time, mass, velocity):
    distance = self - obj
    #magnitude = magnitudes(distance)
    magnitude = 0
    for i in distance:
        magnitude += math.pow(i, 2)
    magnitude = math.sqrt(magnitude)
    acceleration = (-2.959e-4 * mass / (magnitude ** 3)) * distance
    velocity += acceleration * time

@jit
def  up(self, velocity, time):
    self += velocity * time



@jit
def test(planets):
    for i in range(300):
        for p in planets:
            for p2 in planets:
                if p2 != p:
                    p.updateVelocity(p2, 0.001)
            p.updatePosition(0.001)

# time=0.01
# sun = ObjectInSpace(1, [0, 0, 0], [0, 0, 0])
# #earth = planet('sprites/earth/', 30, 2, 0.5, [-0.427879316669597, 0.8857723172178902, -3.771076024444916e-05], [-0.01577605920428391, -0.007553929074446021, 6.370092343965473e-07], 3.0025138260432377e-06, time)
# earth = ObjectInSpace(3.0025138260432377e-06, [-0.427879316669597, 0.8857723172178902, -3.771076024444916e-05], [-0.01577605920428391, -0.007553929074446021, 6.370092343965473e-07])

# def test():
#     uv(earth.position, sun.position, time, sun.mass)
#     return 0

# print(timeit.timeit(test, number=10000))

# print(numba.typeof(sun.position))

# array(float64, 1d, A)