import pygame
import random
from FireBall import FireBall
from Load import load_image


class Boss(pygame.sprite.Sprite):
    def __init__(self, img, x, y, group):
        super().__init__(group)
        self.image = img
        self.rect = pygame.rect.Rect(x, y, self.image.get_width(),
                                     self.image.get_height())
        self.health = 150
        self.fire_freq = 40
        self.fireballs = pygame.sprite.Group()
        self.group = group

    def update(self):
        self.rect = self.rect.move(random.randrange(3) - 1,
                                   random.randrange(3) - 1)

    def fire(self, player):
        start_pos = (self.rect.left, self.rect.center[1])
        diff_x = player.rect.center[0] - start_pos[0]
        diff_y = player.rect.center[1] - start_pos[1]
        FireBall(self.group, self.fireballs, load_image('fireball.png', -1),
                 start_pos[0], start_pos[1], diff_x // 30, diff_y // 30)
