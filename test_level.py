import pygame
from Background import Background
from Load import load_image
from Player import Player

pygame.init()

size = width, height = 700, 700
screen = pygame.display.set_mode(size)
all_sprites = pygame.sprite.Group()
bg = Background('background.jpg', [0, 0])
wizard = Player(load_image("sorlowalk.png", (128, 128, 128, 255)),
                load_image("sorlowalkback.png", (128, 128, 128, 255)),
                load_image("sorlostand.png", (128, 128, 128, 255)),
                load_image("sorlofire.png", (128, 128, 128, 255)), 4, 1, 73, 73, all_sprites)


running = True
clock = pygame.time.Clock()
while running:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        wizard.rect.x += 3
        wizard.update(1)
    if keys[pygame.K_LEFT]:
        wizard.rect.x -= 3
        wizard.update(2)
    if keys[pygame.K_UP]:
        wizard.rect.y -= 3
        wizard.update(1)
    if keys[pygame.K_DOWN]:
        wizard.rect.y += 3
        wizard.update(1)
    if keys[pygame.K_SPACE]:
        wizard.fire()
    screen.blit(bg.image, bg.rect)
    all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()
