import pygame
from support import import_folder


class ParticleEffect(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.frame_index = 0
        self.animation_speed = 0.15
        self.frames = import_folder('graphics/enemy/death')
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(center=pos)

    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index > len(self.frames) - 0.1:
            self.kill()
        else:
            self.image = self.frames[int(self.frame_index)]

    def update(self, x_shit):
        self.animate()
        self.rect.x += x_shit
