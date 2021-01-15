#from planet import planet
from astroquery.jplhorizons import Horizons
from astropy.time import Time

#ççprint(Time.now())
time = 0.1
#sun = planet('sprites/earth/', 120, 1, 0.5, [0, 0], [0, 0], 1, time)

def getInitPosition(id, time = None):
    obj = Horizons(id=id, location="@sun", epochs=Time("2021-01-16").jd, id_type='id').vectors()
    #print(obj)
    return [float(obj['x']), float(obj['y']), float(obj['z'])]

def getInitVelocity(id, time = None):
    obj = Horizons(id=id, location="@sun", epochs=Time("2021-01-16").jd, id_type='id').vectors()
    return [float(obj['vx']), float(obj['vy']), float(obj['vz'])]

if __name__ == '__main__':
    """obj = Horizons(id=301, location="@399", epochs=Time("2021-01-15").jd, id_type='id').vectors()
    print(obj)
    print([float(obj['vx']), float(obj['vy']), float(obj['vz'])])
    print((7.34767*10**22) / (1.989*(10**30)))"""

    print('pos: ' + str(getInitPosition(8)))
    print('pos: ' + str(getInitPosition('199')))
    print('vel: ' + str(getInitVelocity('1')))


"""obj = Horizons(id=2, location="@sun", epochs=Time("2021-01-15").jd, id_type='id').vectors()
obj2 = Horizons(id=3, location="@sun", epochs=Time("2021-01-15").jd, id_type='id').vectors()
positions = [float(obj['x']), float(obj['y']), float(obj['z'])]
velocities = [float(obj['vx']), float(obj['vy']), float(obj['vz'])]
#print(obj)
#print(obj2)

positions2 = [float(obj2['x']), float(obj2['y']), float(obj2['z'])]
velocities2 = [float(obj2['vx']), float(obj2['vy']), float(obj2['vz'])]

#print(positions)
#print(positions2)
#print(velocities)
#print(velocities2)

mercury = planet('sprites/earth/', 120, 1, 0.5, [0.3561706902565177, -0.01506065601899402, -0.03390255348201873], [-0.004247234190204095, 0.02936721662170006, 0.002789379116682074], 1.6515837104072397e-07, time)
#

#earth = planet('sprites/earth/', 120, 1, 0.5, [-0.4120368860763734, 0.8931877188599627, -3.841025986125005e-05], [-0.01590795372926265, -0.007276426236568541, 7.601167919244166e-07], 3.0025138260432377e-06, time)
"""