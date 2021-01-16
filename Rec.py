import pygame, random, planet

class Rec:
    def __init__(self, screen_width, screen_height):
        self.planet = planet.planet('sprites/sun/', 60, 2.5, 0.5, [0, 0, 0], [0, 0, 0], 1, 0.001)
        self.dir_x = 1
        self.dir_y = 1
        self.rectangle_speed_x = 5 * self.dir_x
        self.rectangle_speed_y = 5 * self.dir_y
        self.img = pygame.image.load('windows.png')
        self.rectangle = self.img.get_rect()
        self.rectangle.center = 1280/2, 960/2
    
    def direction(self):
        if self.rectangle.bottomright[0] >= 1280 or self.rectangle.x <= 0:
            self.dir_x = self.dir_x * -1
        if self.rectangle.bottomright[1] >= 960 or self.rectangle.y <= 0:
            self.dir_y = self.dir_y * -1
        self.rectangle.x += self.dir_x * self.rectangle_speed_x
        self.rectangle.y += self.dir_y * self.rectangle_speed_y

    
