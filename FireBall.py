from ManaBall import ManaBall
import pygame


class FireBall(ManaBall):
    def __init__(self, group1, group2, x, y, vx, vy, color):
        super().__init__(group1, group2, x, y, color)
        self.vx = vx
        self.vy = vy

    def update(self, surf, enemi):
        if not surf.get_rect().colliderect(self.rect):
            self.kill()
        self.rect = self.rect.move(self.vx, self.vy)

        if pygame.sprite.collide_mask(self, enemi):
            enemi.health -= 50
            self.kill()
