import pygame
from Load import load_image
import sys


def terminate():
    pygame.quit()
    sys.exit()


def start_screen(surf):
    intro_text = ["Для начала игры нажмите на любую кнопку",
                  "",
                  "MartsinovichDanya",
                  "copyright 2019"]

    fon = pygame.transform.scale(load_image('fon.jpg'), (surf.get_width(), surf.get_height()))
    surf.blit(fon, (0, 0))
    font = pygame.font.Font(None, 20)
    text_coord = 550
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        surf.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()
