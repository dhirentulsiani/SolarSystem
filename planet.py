import sprite_loader as sp
import nbody as nbody
import pygame
import background as bg

RES = (1280, 960)

class planet():
    def __init__(self, spr_path, num_sprs, scale, speed, position, velocity, mass, time, satellite = []):
        self.planet_group = pygame.sprite.Group()
        self.planet = sp.Spr_load(position[0], position[1], 
                                spr_path, num_sprs, scale, speed)
        self.planet_group.add(self.planet)

        self.nbody = nbody.ObjectInSpace(mass, position, velocity)
        self.time = time

        self.scale = 1
        self.satellite = satellite

        self.spr_path = spr_path
        self.num_sprs = num_sprs
        

    def onClick(self, event, planets = []):
        pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.planet.rect.collidepoint(pos):
                self.system(planets)
    
    def draw(self, screen, position = []):
        # On mouse hover reduce opacity
        pos = pygame.mouse.get_pos()
        if self.planet.rect.collidepoint(pos):
            self.planet.image.set_alpha(100)

        #### DRAWING AND UPDATING ####
        # Updating Planet Position
        #self.nbody.updatePosition(self.time)
        #for i in range(100):
        #    self.nbody.updatePosition(self.time)
        if position == []:
            self.planet.position(RES[0]//2 + 200 * self.nbody.position[0], RES[1]//2 - 200 * self.nbody.position[1])
        else:
            self.planet.position(position[0], position[1])



        # Drawing planet
        self.planet_group.draw(screen)
        self.planet.animate()
        self.planet.image.set_alpha(300)
        self.planet_group.update(None, self.scale)
    
    def system(self, planets=[]):
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode(RES, pygame.NOFRAME)
        background = bg.Background(1, 100)

        while True:
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return
            
            #time = p.time
            time = 0.001

            for i in range(100):
                for p in planets:
                    
                    # for j in range(15):
                    #     for moon in p.satellite:
                    #         for p2 in planets:
                    #             moon.nbody.updateVelocity(p2.nbody, p.time/15)
                    #         # moon.nbody.updateVelocity(p.nbody, p.time/15)
                    #         # moon.nbody.updateVelocity(planets[0].nbody, p.time/15)
                    #         moon.nbody.updatePosition(p.time/15)

                    for p2 in planets:
                        if p2 != p:
                            p.nbody.updateVelocity(p2.nbody, time)
                    p.nbody.updatePosition(time)
            
            screen.fill((0, 0, 0))
            background.draw(screen)

            # draw self at centre screen
            #calculate moon position based on earth. (newMoonPos = earthPos - moonPos)

            # self.draw(screen, [RES[0]//2,  RES[1]//2])
            # new = self.nbody.position - self.satellite[0].nbody.position
            
            # newPos = [RES[0]//2 + 30000*new[0], RES[1]//2 - 30000 * new[1]]
            
            earth_x = RES[0]//2 + 30000 * self.nbody.position[0]
            earth_y = RES[1]//2 - 30000 * self.nbody.position[1]
            moon_x =  RES[0]//2 + 30000 * self.satellite[0].nbody.position[0]
            moon_y =  RES[1]//2 - 30000 * self.satellite[0].nbody.position[1]

            change_x = earth_x - 640
            change_y = earth_y - 640

            self.draw(screen, [earth_x - change_x, earth_y - change_y])

            for moon in self.satellite:
                moon.draw(screen, [moon_x - change_x, moon_y - change_y])
            



            pygame.display.flip()
            clock.tick(60)