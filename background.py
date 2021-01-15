import pygame
import sprite_loader as sp

RES = (1280, 960)

class Background():
    def __init__(self, scale, alpha):
        self.sprite_group = pygame.sprite.Group()
        self.bg = sp.Spr_load(RES[0]//2, RES[1]//2, \
                            'sprites/launchscreen/starrs-', \
                            101, scale, 0.5, alpha)
        self.sprite_group.add(self.bg)
    
    def draw(self, screen):
        self.sprite_group.draw(screen)
        self.bg.animate()
        self.sprite_group.update()


    