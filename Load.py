import os
import pygame


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    image = image.convert()
    if colorkey is not None:
        image = image.convert()
        if colorkey is -1:
            colorkey = image.get_at((1, 1))
        image.set_colorkey(colorkey)
    return image
