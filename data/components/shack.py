from itertools import cycle
import pygame as pg
from .. import prepare


class Shack(object):
    def __init__(self, midbottom):
        self.image = prepare.GFX["shack"]
        self.rect = self.image.get_rect(midbottom=midbottom)
        
        self.stove = prepare.GFX["stove"]
        self.stove_rect = self.stove.get_rect(bottomright=(self.rect.right - 50, self.rect.bottom))
        self.smokes = cycle([prepare.GFX["smoke{}".format(i)] for i in range(1, 4)])
        self.smoke = next(self.smokes)
        self.smoke_rect = self.smoke.get_rect(midbottom=(self.stove_rect.centerx - 25, self.stove_rect.top))
        self.flames = cycle([prepare.GFX["flame{}".format(i)] for i in range(1, 6)])
        self.flame = next(self.flames)
        self.flame_rect = self.flame.get_rect(topleft=(self.stove_rect.left + 12, self.stove_rect.top + 300))
        self.flame_timer = 0.0
        self.smoke_timer = 0.0
        self.icehole = prepare.GFX["icehole"]
        self.hole_rect = self.icehole.get_rect(topleft=(self.rect.left + 150, self.rect.bottom))
        
    def draw(self, surface, dt):
        self.flame_timer += dt
        self.smoke_timer += dt
        if self.smoke_timer >= 350:
            self.smoke_timer -= 150
            self.smoke = next(self.smokes)
        if self.flame_timer >= 100:
            self.flame_timer -= 100
            
            self.flame = next(self.flames)
        surface.blit(self.image, self.rect)
        surface.blit(self.flame, self.flame_rect)
        surface.blit(self.smoke, self.smoke_rect)
        surface.blit(self.stove, self.stove_rect)
        surface.blit(self.icehole, self.hole_rect)
        
        
        