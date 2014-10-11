from random import choice, randint
import pygame as pg
from .. import prepare



class Water(object):
    def __init__(self, rect):
        self.rect = rect
        
        
    def draw(self, surface):
        r, g, b = 0, 70, 120
        for y in range(0, self.rect.height + 1, 8):
            pg.draw.rect(surface, (r, g, b), (0, self.rect.top + y, self.rect.width, 8))
            g = max(8, g - 1)
            b = max(15, b - 2)

            
class Sky(object):
    def __init__(self, rect):
        self.rect = rect
        
    def draw(self, surface):
        r, g, b = 142, 229, 238
        for y in range(self.rect.top, self.rect.bottom + 1, 2):
            pg.draw.rect(surface, (int(r), g, b), (self.rect.left, y, self.rect.width, 2))
            r = min(232, r + .3)
            
            
class Ice(object):
    def __init__(self, rect):
        self.rect = rect
        
    def draw(self, surface):
        r,g,b = 255, 255, 255
        for y in range(self.rect.top, self.rect.bottom + 1, 2):
            pg.draw.rect(surface, (r,g,b), (self.rect.left, y, self.rect.width, 2))
            r = max(70, r - 10)
            b = max(198, b - 5)
            
            
class Forest(object):
    def __init__(self, bottomleft):
        self.image = prepare.GFX["forest"]
        self.rect = self.image.get_rect(bottomleft=bottomleft)
        
    def draw(self, surface):
        surface.blit(self.image, self.rect)
        

class BgroundShack(object):
    def __init__(self, image_name, ice_rect):
        self.image = prepare.GFX[image_name]
        self.rect = self.image.get_rect()
        x = randint(ice_rect.left - self.rect.width, ice_rect.right)
        self.rect.bottomleft = (x, ice_rect.top)
        
    def draw(self, surface):
        surface.blit(self.image, self.rect)
        
        
class TinyShack(BgroundShack):
    images = ["tinyshack{}".format(i) for i in range(1, 6)]
    def __init__(self, ice_rect):
        image_name = choice(self.images)
        super(TinyShack, self).__init__(image_name, ice_rect)
        
class SmallShack(BgroundShack):
    images = ["smallshack{}".format(i) for i in range(1, 6)]
    def __init__(self, ice_rect):
        image_name = choice(self.images)
        super(SmallShack, self).__init__(image_name, ice_rect)
        
class MediumShack(BgroundShack):
    images = ["medshack{}".format(i) for i in range(1, 6)]
    def __init__(self, ice_rect):
        image_name = choice(self.images)
        super(MediumShack, self).__init__(image_name, ice_rect)



