from random import choice, randint
import pygame as pg
from .. import prepare


class Sturgeon(object):
    def __init__(self, water, x_velocity, speed, depth):
        self.name = "Sturgeon"
        self.pos = [randint(water.left, water.right), water.top + depth]
        self.x_velocity = x_velocity
        self.speed = speed
        self.images = {-1: prepare.GFX["sturgeon"],
                               1: pg.transform.flip(prepare.GFX["sturgeon"], True, False)}
        self.image = self.images[self.x_velocity]
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.collider_info = {-1: [(44, 17, 25, 22),(12, 28, 32, 8),(68, 12, 122, 31),
                                            (191, 13, 27, 30),(220, 27, 49, 12)],
                                      1: [(106, 14, 144, 26),(251, 21, 23, 6),(86, 21, 20, 22),
                                            (275, 28, 23, 6),(47, 27, 38, 11)]
                                     }
        self.colliders = []
        for info in self.collider_info[self.x_velocity]:
            self.colliders.append(pg.Rect(self.rect.left + info[0], self.rect.top + info[1], info[2], info[3]))
            
    def update(self, water_rect):
        if self.x_velocity == -1:
            if self.rect.left < 0:
                self.x_velocity *= -1
                self.image = self.images[self.x_velocity]
        elif self.x_velocity == 1:
            if self.rect.right > water_rect.width:
                self.x_velocity *= -1
                self.image = self.images[self.x_velocity]
        self.pos[0] += self.x_velocity * self.speed
        self.rect.center = self.pos
        self.colliders = []
        for info in self.collider_info[self.x_velocity]:
            self.colliders.append(pg.Rect(self.rect.left + info[0], self.rect.top + info[1], info[2], info[3]))
            
    def draw(self, surface):
        surface.blit(self.image, self.rect)
        