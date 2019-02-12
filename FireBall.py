import pygame


class FireBall(pygame.sprite.Sprite):
    def __init__(self, group1, group2, img, x, y, vx, vy):
        super().__init__(group1)
        self.add(group2)
        self.image = img
        self.rect = pygame.Rect(x, y, self.image.get_width(),
                                self.image.get_height())
        self.mask = pygame.mask.from_surface(self.image)
        self.vx = vx
        self.vy = vy

    def update(self, surf, enemi):
        if not surf.get_rect().colliderect(self.rect):
            self.kill()
        self.rect = self.rect.move(self.vx, self.vy)

        if pygame.sprite.collide_mask(self, enemi):
            enemi.health -= 10
            self.kill()
