import pygame
from Background import Background
from Load import load_image
from Player import Player
from ManaBall import ManaBall

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
    tick = clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                wizard.image = wizard.fireimg
                ManaBall(all_sprites, wizard.manaballs,
                         wizard.rect.right, wizard.rect.center[1] + 10)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        if wizard.rect.right < 700:
            wizard.rect.x += 3
        wizard.update(1)
    if keys[pygame.K_LEFT]:
        if wizard.rect.left > 0:
            wizard.rect.x -= 3
        wizard.update(2)
    if keys[pygame.K_UP]:
        if wizard.rect.top > 0:
            wizard.rect.y -= 3
        wizard.update(1)
    if keys[pygame.K_DOWN]:
        if wizard.rect.bottom < 700:
            wizard.rect.y += 3
        wizard.update(1)
    screen.blit(bg.image, bg.rect)
    all_sprites.draw(screen)
    wizard.manaballs.update(screen)
    pygame.display.flip()
pygame.quit()
