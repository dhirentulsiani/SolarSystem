import pygame
import background as bg
from planet import planet
import CreatePlanetTests as cpt
import numpy as np
import nbody

#### CONSTANTS ####
RES = (1280, 960)
CENTER = (RES[0]//2, RES[1]//2)
BLACK = (0, 0, 0)

#### PYGAME SETUP ####
#pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode(RES, pygame.NOFRAME)

#### SCENE SETUP ####
# Background
background = bg.Background(1, 100)

# Planets
time = 0.001
#earth = planet('sprites/earth/', 120, 1, 0.5, [-0.4120368860763734, 0.8931877188599627, -3.841025986125005e-05], [-0.01590795372926265, -0.007276426236568541, 7.601167919244166e-07], 3.0025138260432377e-06, time)
#sun = planet('sprites/sun/', 60, 2, 0.5, [-0.006753102164233409, 0.005916352944610752, 0.0001089046022064163], [-6.742297302722944e-06, -5.909346489609531e-06, 2.13856454410461e-07], 1, time)
#mercury = planet('sprites/earth/', 120, 1, 0.5, [0.3561706902565177, -0.01506065601899402, -0.03390255348201873], [-0.004247234190204095, 0.02936721662170006, 0.002789379116682074], 1.6515837104072397e-07, time)

sun = planet('sprites/sun/', 60, 2, 0.5, [0, 0, 0], [0, 0, 0], 1, time)

mercury = planet('sprites/mercury/', 30, 1, 0.5, [0.3507626097429233, 0.01432354671171785, -0.03100530076885245], [-0.006581625235022489, 0.02936887463390415, 0.003003650546848923], 1.6515837104072397e-07, time)
venus = planet('sprites/sun/', 30, 1, 0.5, [-0.1780646549205903, -0.7038818025711587, 0.000615870147439354], [0.01947197548136475, -0.005044261397381249, -0.001192871221191632], 2.4469582704876823e-06, time)
mars = planet('sprites/sun/', 30, 2, 0.5, [0.4321593703259651, 1.466410355954691, 0.02012876985921669], [-0.01289327610133903, 0.005144431868605684, 0.0004240924245065008], 3.212669683257918e-07, time)
moon = planet('sprites/moon/', 30, 0.2, 0.5, cpt.getInitPosition(301), cpt.getInitVelocity(301), 3.691302161890397e-08, time)
earth = planet('sprites/earth/', 30, 2, 0.5, [-0.427879316669597, 0.8857723172178902, -3.771076024444916e-05], [-0.01577605920428391, -0.007553929074446021, 6.370092343965473e-07], 3.0025138260432377e-06, time, [moon])
phobos = planet('sprites/moon/', 30, 0.2, 0.5, cpt.getInitPosition('phobos'), cpt.getInitVelocity('phobos'), (10.659*10**15)/(1.989*10**30), time)
deimos = planet('sprites/moon/', 30, 0.2, 0.5, cpt.getInitPosition('phobos'), cpt.getInitVelocity('deimos'), (1.4762*10**15)/(1.989*10**30), time)

jupiter = planet('sprites/sun/', 30, 2, 0.5, cpt.getInitPosition(5), cpt.getInitVelocity(5), 0.0009543, time)
saturn = planet('sprites/sun/', 30, 2, 0.5, cpt.getInitPosition(6), cpt.getInitVelocity(6), 0.0002857214680744092, time)
uranus = planet('sprites/sun/', 30, 2, 0.5, cpt.getInitPosition(7), cpt.getInitVelocity(7), 4.364504776269482e-05, time)
neptune = planet('sprites/sun/', 30, 2, 0.5, cpt.getInitPosition(8), cpt.getInitVelocity(8), 5.1483157365510307e-05, time)


#earth = planet('sprites/earth/', 120, 0.5, 0.5, cpt.getInitPosition(399), cpt.getInitVelocity(399), 3.0025138260432377e-06, time)
#moon = planet('sprites/moon/', 60, 0.2, 0.5, cpt.getInitPosition(301), cpt.getInitVelocity(301), 3.691302161890397e-08, time)

dis = np.linalg.norm(earth.nbody.position - moon.nbody.position)

#planets = [sun, mercury, venus, earth, mars, moon]
#planets = [mercury, venus, earth, sun, mars, jupiter, saturn, uranus, neptune, moon]
planets = [mercury, venus, earth, sun, mars, jupiter, saturn, neptune, moon, uranus]
#planets = [earth, moon]
bodies = [p.nbody for p in planets]
satellites = [moon, phobos, deimos]

"""
Planet values:
Mercury: 1.46
Venus: 1.74
Mars: 2.64
Jupiter: 6.2

"""

#### MAIN FUNCTION ####
def small_system():
    # main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
            for p in planets:
                p.onClick(event, planets)

        screen.fill(BLACK)

        # Drawing background
        background.draw(screen)


        # Updating positions loop
        # for i in range(100):
        #     for p in planets:
        #         for p2 in planets:
        #             if p2 != p:
        #                 p.nbody.updateVelocity(p2.nbody, p.time)
        #         p.nbody.updatePosition(time)
        nbody.test(bodies)


        for p in planets[:5]:
            p.draw(screen)
        
        #print(earth.nbody.position)
        
        moon.draw(screen)
         
        me = np.linalg.norm(earth.nbody.position - mercury.nbody.position)
        e = np.linalg.norm(earth.nbody.position)
        ve = np.linalg.norm(earth.nbody.position - venus.nbody.position)
        ma = np.linalg.norm(earth.nbody.position - mars.nbody.position)
        mo = np.linalg.norm(earth.nbody.position - earth.satellite[0].nbody.position)


        #j = np.linalg.norm(earth.nbody.position - jupiter.nbody.position)
        if ((me < 0.52 or me > 1.46) or ve < 0.264 or ve > 1.74 or ma < 0.413 or ma  > 2.64 or e > 1.02):
            print('mercury: (0.554 to 1.46) ' + str(me))
            print('venus: (0.264 to 1.74)' + str(ve))
            print('earth: (1.02)' + str(e))
            print('mars (0.413 to 2.64)' + str(ma))
            print(mo)
            raise IndexError
        pygame.display.flip()
        clock.tick(30)

if __name__ == '__main__':
    small_system()
    # count = 0
    # while count < 365250:
    #     for event in pygame.event.get():
    #         if event.type == pygame.KEYDOWN:
    #             break
    
    
    #     for p in planets:
    #         for p2 in planets:
    #             if p2 != p:
    #                 p.nbody.updateVelocity(p2.nbody, p.time)
    #         p.nbody.updatePosition(p.time)

    #     me = np.linalg.norm(earth.nbody.position - mercury.nbody.position)
    #     e = np.linalg.norm(earth.nbody.position)
    #     ve = np.linalg.norm(earth.nbody.position - venus.nbody.position)
    #     ma = np.linalg.norm(earth.nbody.position - mars.nbody.position)
    #     mo = np.linalg.norm(earth.nbody.position - earth.satellite[0].nbody.position)

    #     #j = np.linalg.norm(earth.nbody.position - jupiter.nbody.position)
    #     if (me < 0.50 or me > 1.46) or (ve < 0.264 or ve > 1.74) or (ma < 0.413 or ma > 2.64) or (e > 1.02): #mo 0.0275
    #         print('mercury: (0.554 to 1.46) ' + str(me) + str(me < 0.554 or me > 1.46))
    #         print('venus: (0.264 to 1.74)' + str(ve))
    #         print('earth: (1.02)' + str(e))
    #         print('mars (0.413 to 2.64)' + str(ma))
    #         print(mo)
    #         raise IndexError

    #     if count % 10000 == 0:
    #         print('here' + str(count))
    #     count += 1
    # print(earth.nbody.position)