import pygame
import os


pygame.mixer.init()
scream = pygame.mixer.Sound(os.path.join('data', 'scream.wav'))


class ManaBall(pygame.sprite.Sprite):
    def __init__(self, group1, group2, x, y, color):
        super().__init__(group1)
        self.add(group2)
        self.radius = 10
        self.image = pygame.Surface((2 * self.radius, 2 * self.radius), pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, color, (self.radius, self.radius), self.radius)
        self.rect = pygame.Rect(x, y, 2 * self.radius, 2 * self.radius)
        self.vx = 5
        self.vy = 0
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, surf, enemi):
        if not surf.get_rect().colliderect(self.rect):
            self.kill()
        self.rect = self.rect.move(self.vx, self.vy)

        if pygame.sprite.collide_mask(self, enemi):
            enemi.health -= 10
            self.kill()
            scream.play()
