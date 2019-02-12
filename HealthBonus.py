import pygame
import random


class HealthBonus(pygame.sprite.Sprite):
    def __init__(self, img, group1, group2, screen_width, screen_height):
        super().__init__(group1)
        self.add(group2)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(screen_width - 80)
        self.rect.y = random.randrange(screen_height - 80)
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, player, enemi):
        if pygame.sprite.collide_mask(self, player):
            if player.health < 30:
                player.health += 10
            self.kill()
        if pygame.sprite.collide_rect(self, enemi):
            self.kill()
