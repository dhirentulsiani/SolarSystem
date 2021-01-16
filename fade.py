# A simple module which fades out the screen
import pygame

def fade(size, screen, color=(0, 0, 0)):
    block = pygame.Surface(size)
    block.fill(color)
    for alpha in range(0, 300, 3):
        block.set_alpha(alpha)
        screen.blit(block, (0, 0))
        pygame.display.update()
        pygame.time.delay(1)
