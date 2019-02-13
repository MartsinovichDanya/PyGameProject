import pygame
import sys
from Load import load_image
import random


def terminate():
    pygame.quit()
    sys.exit()


exit_place = random.randint(73, 627)


def secret(surf, player):
    if player.rect.left == 0 and player.rect.center[1] == exit_place:
        pygame.mixer.music.stop()
        intro_text = ["Нажмите на любую кнопку",
                      "",
                      "MartsinovichDanya",
                      "copyright 2019"]

        fon = pygame.transform.scale(load_image('vobhod.png'), (surf.get_width(), surf.get_height()))
        surf.blit(fon, (0, 0))
        font = pygame.font.Font(None, 20)
        text_coord = 590
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
                    terminate()
            pygame.display.flip()

    else:
        pass
