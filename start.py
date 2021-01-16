# the start screen
import pygame
from background import Background
import sprite_loader as sp
import math
import small_system
import fade

#### CONSTANTS ####
RES = (1280, 960)
CENTER = (RES[0]//2, RES[1]//2 - 100)
BLACK = (0, 0, 0)

#### PYGAME SETUP ####
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode(RES, pygame.NOFRAME)

#### SCENE SETUP ####
# Background
background = Background(1, 100)

# PLANETS
earth = sp.Spr_load(0, 0, 'sprites/earth/', 120, 2, 0.5)
mars = sp.Spr_load(0, 0, 'sprites/mars/', 60, 2, 0.5)
earth_g = pygame.sprite.Group()
mars_g = pygame.sprite.Group()
earth_g.add(earth)
mars_g.add(mars)

# Image
image = pygame.image.load('sprites/start.png').convert_alpha()

def launch():
    time = 0
    time1 = 3
    show = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    fade.fade(RES, screen)
                    return
                if event.key == pygame.K_SPACE:
                    fade.fade(RES, screen)
                    small_system.small_system()


        screen.fill(BLACK)
        background.draw(screen)

        stage = pygame.Rect(0, 0, 500, 500)
        stage.center = CENTER
        pygame.draw.rect(screen, (255,255,255), stage, 10)

        earth_x = RES[0]//2 + 200 * math.cos(time) - 430
        earth_y = RES[1]//2 + 200 * math.sin(time) - 280

        mars_x = RES[0]//2 + 200 * math.cos(time1) - 430
        mars_y = RES[1]//2 + 200 * math.sin(time1) - 280

        earth.position(earth_x, earth_y)
        mars.position(mars_x, mars_y)

        surf = pygame.Surface((500, 500))


        earth_g.draw(surf)
        mars_g.draw(surf)
        earth.animate()
        mars.animate()
        earth_g.update(None, 2)
        mars_g.update(None, 2)

        i_rect = pygame.Rect(0, 0, 500, 200)
        i_rect.center = (CENTER[0], 800)
        screen.blit(surf, stage)

        if show < 30 and show > 15:
            screen.blit(image, i_rect)
        elif show > 30:
            show = 0
        
        
        time += 0.01
        time1 += 0.01
        show += 1
        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    launch()