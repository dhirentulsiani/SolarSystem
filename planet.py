import sprite_loader as sp
import nbody as nbody
import pygame
import background as bg
import fade
import datetime

RES = (1280, 960)

class planet():
    def __init__(self, spr_path, num_sprs, scale, speed, position, velocity, mass, time, satellite = []):
        self.planet_group = pygame.sprite.Group()
        self.planet = sp.Spr_load(position[0], position[1], 
                                spr_path, num_sprs, scale, speed)
        self.planet_group.add(self.planet)

        self.nbody = nbody.Nbody(mass, position, velocity)
        self.time = time

        self.scale = 4
        self.satellite = satellite

        self.path = []
        self.path_gap = 0

    def onClick(self, event, planets = [], screen = None, date=None):
        pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.planet.rect.collidepoint(pos):
                fade.fade(RES, screen)
                return self.system(planets, date)

    
    def moveWindows(self, screen, position = [], size = 1, drawpath = True):
        x_pos = RES[0]//2 + 280 * self.nbody.position[0]
        y_pos = RES[1]//2 - 280 * self.nbody.position[1]
        if x_pos > RES[0] - 165 or x_pos < 0 + 165:
            self.nbody.velocity[0] *= -1
        if y_pos > RES[1] - 165 or y_pos < 0 + 165:
            self.nbody.velocity[1] *= -1

        self.nbody.updatePosition(0.001)

        # On mouse hover reduce opacity
        pos = pygame.mouse.get_pos()
        if self.planet.rect.collidepoint(pos):
            self.planet.image.set_alpha(100)

        #### DRAWING AND UPDATING ####
        if position == []:
            self.planet.position(x_pos, y_pos)
        else:
            self.planet.position(position[0], position[1])

        # Drawing path

        self.path_gap = self.path_gap + 1
        if len(self.path) < 100 and self.path_gap % 7 == 0:
            self.path.append(pygame.Rect(x_pos, y_pos, 6, 6))
        elif len(self.path) >= 100:
            self.path = self.path[1:]
        for i in self.path:
            pygame.draw.ellipse(screen, (255, 255, 255), i)

        # Drawing planet
        self.planet_group.draw(screen)
        self.planet.animate()
        self.planet.image.set_alpha(300)
        self.planet_group.update(None, size)


    def draw(self, screen, position = [], size = 1, drawpath = True, scale=280):
        # On mouse hover reduce opacity
        pos = pygame.mouse.get_pos()
        if self.planet.rect.collidepoint(pos):
            self.planet.image.set_alpha(100)

        #### DRAWING AND UPDATING ####
        x_pos = RES[0]//2 + scale * self.nbody.position[0]
        y_pos = RES[1]//2 - scale * self.nbody.position[1]
        if position == []:
            self.planet.position(x_pos, y_pos)
        else:
            self.planet.position(position[0], position[1])

        # Drawing path

        self.path_gap = self.path_gap + 1
        if len(self.path) < 100 and self.path_gap % 7 == 0:
            self.path.append(pygame.Rect(x_pos, y_pos, 6, 6))
        elif len(self.path) >= 100:
            self.path = self.path[1:]
        for i in self.path:
            pygame.draw.ellipse(screen, (255, 255, 255), i)

        # Drawing planet
        self.planet_group.draw(screen)
        self.planet.animate()
        self.planet.image.set_alpha(300)
        self.planet_group.update(None, size)
    
    def system(self, planets=[], date=None):
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode(RES, pygame.NOFRAME)
        background = bg.Background(1, 100)
        bodies = [p.nbody for p in planets]
        interval = datetime.timedelta(hours=7, minutes=12)
        font = pygame.font.Font('Arcade.ttf', 70)

        while True:
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        for planet in planets:
                            planet.path = []
                        fade.fade(RES, screen)
                        return date
            screen.fill((0, 0, 0))
            self.path = []
            time = self.time
            
            nbody.update(bodies)
            
            screen.fill((0, 0, 0))
            background.draw(screen)
            
            self_x = RES[0]//2 + 30000 * self.nbody.position[0]
            self_y = RES[1]//2 - 30000 * self.nbody.position[1]
            change_x = self_x - 640
            change_y = self_y - 480

            self.draw(screen, [self_x - change_x, self_y - change_y], 1)

            date += interval

            for moon in self.satellite:
                moon_x =  RES[0]//2 + 30000 * moon.nbody.position[0]
                moon_y =  RES[1]//2 - 30000 * moon.nbody.position[1]
                moon.path = []
                moon.draw(screen, [moon_x - change_x, moon_y - change_y])
            
            text = font.render(str(date.strftime('%Y-%m-%d')), True, (255,255,255))
            screen.blit(text, (RES[0]//2 - 150 ,900))

            pygame.display.flip()
            clock.tick(60)