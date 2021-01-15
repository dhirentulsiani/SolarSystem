import pygame

class Spr_load(pygame.sprite.Sprite):
    """
    Loads animated sprites

    pos_x, pos_y: the position where sprite will be placed
    img_location: the filepath where sprite is contained
    num_imgs: the number of animated sprites
    scale: changes size of sprite by a scale factor
    """
    def __init__(self, pos_x, poss_y, img_location, num_imgs, scale=None, speed=0.5, alpha=300):
        super().__init__()
        self.sprites = []
        for i in range(1, num_imgs + 1):
            load = pygame.image.load(img_location + str(i) + '.png')
            load = load.convert_alpha()
            load.set_alpha(alpha)
            if scale != None:
                load = pygame.transform.scale(load, (int(scale *load.get_width()), int(scale * load.get_height())))
            self.sprites.append(load)
        
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.center = pos_x, poss_y

        self.is_animating = False
        self.speed = speed
    
    def position(self, x, y):
        self.rect.center = x, y
    
    def animate(self):
        self.is_animating = True
    
    def update(self, speed=None, scale=None):
        if self.is_animating == True:
            if speed != None:
                self.current_sprite += speed
            else:
                self.current_sprite += self.speed

            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False

            self.image = self.sprites[-int(self.current_sprite)]

            if scale != None:
                size = int(self.image.get_width() * scale), int(self.image.get_height() * scale)
                self.image = pygame.transform.scale(self.image, size)