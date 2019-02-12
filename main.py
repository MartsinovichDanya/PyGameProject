import pygame

from Background import Background
from Load import load_image
from Player import Player
from ManaBall import ManaBall
from Boss import Boss
from ManaBonus import ManaBonus
from HealthBonus import HealthBonus

from StartScreen import start_screen
from GameOverScreen import game_over_screen
from WinScreen import win_screen

pygame.init()

size = width, height = 700, 700
screen = pygame.display.set_mode(size)
all_sprites = pygame.sprite.Group()
bg = Background('background.jpg', [0, 0])
wizard = Player(load_image("sorlowalk.png", (128, 128, 128, 255)),
                load_image("sorlowalkback.png", (128, 128, 128, 255)),
                load_image("sorlostand.png", (128, 128, 128, 255)),
                load_image("sorlofire.png", (128, 128, 128, 255)), 4, 1, 0, 300, all_sprites)

enemi = Boss(load_image("enemi.png", -1), 400, 250, all_sprites)


running = True
clock = pygame.time.Clock()
start_screen(screen)
font = pygame.font.Font(None, 30)
h_indicator = font.render(f'Health: {wizard.health}', 1, pygame.Color('red'))
m_indicator = font.render(f'Mana: {wizard.mana}', 1, (1, 46, 119))
h_rect = h_indicator.get_rect()
m_rect = m_indicator.get_rect()
h_rect.topleft = (20, 20)
m_rect.topleft = (20, 40)
manabonus_group = pygame.sprite.Group()
healthbonus_group = pygame.sprite.Group()
counter = 0
mana_bonus_counter = 0
health_bonus_counter = 0

while running:
    tick = clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                wizard.image = wizard.fireimg
                if wizard.mana >= 10:
                    ManaBall(all_sprites, wizard.manaballs,
                             wizard.rect.right, wizard.rect.center[1] + 10, (51, 51, 255))
                    wizard.mana -= 10

    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        if wizard.rect.right < width:
            wizard.rect.x += 3
        wizard.update(1)
    if keys[pygame.K_a]:
        if wizard.rect.left > 0:
            wizard.rect.x -= 3
        wizard.update(2)
    if keys[pygame.K_w]:
        if wizard.rect.top > 0:
            wizard.rect.y -= 3
        wizard.update(1)
    if keys[pygame.K_s]:
        if wizard.rect.bottom < height:
            wizard.rect.y += 3
        wizard.update(1)

    screen.blit(bg.image, bg.rect)
    h_indicator = font.render(f'Health: {wizard.health}', 1, pygame.Color('red'))
    m_indicator = font.render(f'Mana: {wizard.mana}', 1, (1, 46, 119))
    screen.blit(h_indicator, h_rect)
    screen.blit(m_indicator, m_rect)
    all_sprites.draw(screen)
    wizard.manaballs.update(screen, enemi)
    enemi.update()
    enemi.fireballs.update(screen, wizard)
    manabonus_group.update(wizard, enemi)
    healthbonus_group.update(wizard, enemi)
    pygame.display.flip()

    if counter == enemi.fire_freq:
        enemi.fire(wizard)
        counter = 0

    if mana_bonus_counter == 90:
        ManaBonus(load_image('manabonus.png', -1), all_sprites, manabonus_group, width, height)
        mana_bonus_counter = 0

    if health_bonus_counter == 600:
        HealthBonus(load_image('healthbonus.png', -1), all_sprites, healthbonus_group, width, height)
        health_bonus_counter = 0

    if wizard.health == 0:
        game_over_screen(screen)

    if enemi.health == 0:
        win_screen(screen)

    counter += 1
    mana_bonus_counter += 1
    health_bonus_counter += 1

pygame.quit()
