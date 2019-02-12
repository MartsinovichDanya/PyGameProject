import pygame
import random
from FireBall import FireBall


class Boss(pygame.sprite.Sprite):
    def __init__(self, img, x, y, group):
        super().__init__(group)
        self.image = img
        self.rect = pygame.rect.Rect(x, y, self.image.get_width(),
                                     self.image.get_height())
        self.health = 1500
        self.fire_freq = 20
        self.fireballs = pygame.sprite.Group()

    def update(self, counter):
        self.rect = self.rect.move(random.randrange(3) - 1,
                                   random.randrange(3) - 1)

    def fire(self):
        pass
