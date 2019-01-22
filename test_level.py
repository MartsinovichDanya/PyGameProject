import pygame
from Background import Background
from Load import load_image

pygame.init()

size = width, height = 700, 700
screen = pygame.display.set_mode(size)
all_sprites = pygame.sprite.Group()
bg = Background('background.jpg', [0, 0])
sprite = pygame.sprite.Sprite()
sprite.image = load_image("hero.png")
sprite.rect = sprite.image.get_rect()
all_sprites.add(sprite)

running = True
clock = pygame.time.Clock()
while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        sprite.rect.x += 4
    if keys[pygame.K_LEFT]:
        sprite.rect.x -= 4
    if keys[pygame.K_UP]:
        sprite.rect.y -= 4
    if keys[pygame.K_DOWN]:
        sprite.rect.y += 4
    screen.blit(bg.image, bg.rect)
    all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()
