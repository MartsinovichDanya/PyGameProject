import pygame


class ManaBall(pygame.sprite.Sprite):
    def __init__(self, group1, group2, x, y):
        super().__init__(group1)
        self.add(group2)
        self.radius = 10
        self.image = pygame.Surface((2 * self.radius, 2 * self.radius), pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color("blue"), (self.radius, self.radius), self.radius)
        self.rect = pygame.Rect(x, y, 2 * self.radius, 2 * self.radius)
        self.vx = 5
        self.vy = 0
        self.k = False

    def update(self):
        self.rect = self.rect.move(self.vx, self.vy)
