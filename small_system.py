import pygame
import background as bg
from planet import planet
import CreatePlanetTests as cpt
import numpy as np
import nbody
import fade
import datetime

#### CONSTANTS ####
RES = (1280, 960)
CENTER = (RES[0]//2, RES[1]//2)
BLACK = (0, 0, 0)

#### PYGAME SETUP ####
pygame.init()
pygame.font.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode(RES, pygame.NOFRAME)

#### SCENE SETUP ####
# Background
background = bg.Background(1, 100)

# Planets
time = 0.001



phobos = planet('sprites/moon/', 30, 0.2, 0.5, cpt.getInitPosition('phobos'), cpt.getInitVelocity('phobos'), (10.659*10**15)/(1.989*10**30), time)
deimos = planet('sprites/moon/', 30, 0.2, 0.5, cpt.getInitPosition('deimos'), cpt.getInitVelocity('deimos'), (1.4762*10**15)/(1.989*10**30), time)
sun = planet('sprites/sun/', 1, 2.5, 0.5, [0, 0, 0], [0, 0, 0], 1, time)
mercury = planet('sprites/mercury/', 30, 0.3, 0.5, [0.3507626097429233, 0.01432354671171785, -0.03100530076885245], [-0.006581625235022489, 0.02936887463390415, 0.003003650546848923], 1.6515837104072397e-07, time)
venus = planet('sprites/venus/', 30, 1.3, 0.5, [-0.1780646549205903, -0.7038818025711587, 0.000615870147439354], [0.01947197548136475, -0.005044261397381249, -0.001192871221191632], 2.4469582704876823e-06, time)
mars = planet('sprites/mars/', 30, 1.2, 0.5, [0.4321593703259651, 1.466410355954691, 0.02012876985921669], [-0.01289327610133903, 0.005144431868605684, 0.0004240924245065008], 3.212669683257918e-07, time)
moon = planet('sprites/moon/', 30, 0.2, 0.5, cpt.getInitPosition(301), cpt.getInitVelocity(301), 3.691302161890397e-08, time)
earth = planet('sprites/earth/', 60, 1.7, 0.5, [-0.427879316669597, 0.8857723172178902, -3.771076024444916e-05], [-0.01577605920428391, -0.007553929074446021, 6.370092343965473e-07], 3.0025138260432377e-06, time, [moon])
jupiter = planet('sprites/sun/', 30, 2, 0.5, cpt.getInitPosition(5), cpt.getInitVelocity(5), 0.0009543, time)
saturn = planet('sprites/sun/', 30, 2, 0.5, cpt.getInitPosition(6), cpt.getInitVelocity(6), 0.0002857214680744092, time)
uranus = planet('sprites/sun/', 30, 2, 0.5, cpt.getInitPosition(7), cpt.getInitVelocity(7), 4.364504776269482e-05, time)
neptune = planet('sprites/sun/', 30, 2, 0.5, cpt.getInitPosition(8), cpt.getInitVelocity(8), 5.1483157365510307e-05, time)

windows = planet('', 1, 1.3, 0.5, [-0.1780646549205903, -0.7138818025711587, 0.000615870147439354], [0.08147197548136475, -0.06044261397381249, -0.001192871221191632], 20.4469582704876823, time)

all_planets = [mercury, venus, earth, sun, mars, jupiter, saturn, neptune, moon, uranus]
first_four_planets = [mercury, venus, earth, sun, mars]
first_six_planets = [mercury, venus, earth, sun, mars, jupiter, moon]
planets = first_six_planets
bodies = [p.nbody for p in planets]
satellites = [moon, phobos, deimos]


#### MAIN FUNCTION ####
def small_system():
    font = pygame.font.Font('Arcade.ttf', 70)
    date= datetime.datetime(2021,1,16)
    interval = datetime.timedelta(hours=7, minutes=12)
    # main loop
    global first_six_planets
    global windows
    global bodies
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    fade.fade(RES, screen)
                    return
                elif event.key == pygame.K_SPACE:
                    first_six_planets.append(windows)
                    bodies = [p.nbody for p in planets]
                    
            for p in planets:
                x = p.onClick(event, planets, screen, date)
                if x is not None:
                    date = x

        screen.fill(BLACK)

        # Drawing background
        background.draw(screen)
        nbody.update(bodies)

        for p in planets:
            if p != windows:
                p.draw(screen, scale=286)
            else:
                p.moveWindows(screen)         

        date += interval

        text = font.render(str(date.strftime('%Y-%m-%d')), True, (255,255,255))
        screen.blit(text, (RES[0]//2 - 150 ,900))
        pygame.display.flip()
        clock.tick(30)

if __name__ == '__main__':
    small_system()
