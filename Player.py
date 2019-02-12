import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, sheet1, sheet2, stand, fire, columns, rows, x, y, group):
        super().__init__(group)
        self.group = group
        self.standimg = stand
        self.fireimg = fire
        self.all_frames = []
        self.cut_sheet(sheet1, columns, rows)
        self.cut_sheet(sheet2, columns, rows)
        self.forward_frames = self.all_frames[:4]
        self.back_frames = self.all_frames[4:]
        self.cur_forward_frame = 0
        self.cur_back_frame = 0
        self.image = self.standimg
        self.rect = self.rect.move(x, y)
        self.manaballs = pygame.sprite.Group()
        self.mana = 30
        self.health = 30
        self.mask = pygame.mask.from_surface(self.image)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.all_frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self, direction):
        if direction == 1:
            self.cur_forward_frame = (self.cur_forward_frame + 1) % len(self.forward_frames)
            self.image = self.forward_frames[self.cur_forward_frame]
            self.mask = pygame.mask.from_surface(self.image)
        else:
            self.cur_back_frame = (self.cur_back_frame + 1) % len(self.back_frames)
            self.image = self.back_frames[self.cur_back_frame]
            self.mask = pygame.mask.from_surface(self.image)
