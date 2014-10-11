from random import choice, randint, uniform
from collections import OrderedDict
import pygame as pg
from .. import prepare


class Fish(object):
    def __init__(self, name, img_name, x_velocity, water_rect):
        self.name = name
        self.images = {-1: prepare.GFX[img_name],
                               1: pg.transform.flip(prepare.GFX[img_name], True, False)}
        self.x_velocity = x_velocity
        self.image = self.images[self.x_velocity]
        self.rect = self.image.get_rect()
        self.pos = [randint(-self.rect.width, water_rect.width + self.rect.width),
                         randint(self.depth_range[0] + water_rect.top,
                                     self.depth_range[1] + water_rect.top)]
        self.rect.center = self.pos
        self.weight = uniform(*self.weight_range)
        self.out_of_water = False
        
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
        
    def draw(self, surface):
        surface.blit(self.image, self.rect)    
        
        
class BlackCrappie(Fish):
    depth_range = (80, 250)
    speed = .4
    weight_range = (10.0, 40.0)
    mouth_offset = (1, 6)
    def __init__(self, water_rect):
        super(BlackCrappie, self).__init__("Black Crappie", "blackcrappie", choice((-1, 1)), water_rect)
        

class WhiteCrappie(Fish):
    depth_range = (100, 300)
    speed = .4
    weight_range = (10.0, 48.0)
    mouth_offset = (0, 6)
    def __init__(self, water_rect):
        super(WhiteCrappie, self).__init__("White Crappie", "whitecrappie", choice((-1, 1)), water_rect)
        
        
class YellowPerch(Fish):
    depth_range = (80, 250)
    speed = .4
    weight_range = (8.0, 36.0)
    mouth_offset = (0, 7)
    def __init__(self, water_rect):
        super(YellowPerch, self).__init__("Yellow Perch", "yellowperch", choice((-1, 1)), water_rect)
        
        
class WhitePerch(Fish):
    depth_range = (100, 300)
    speed = .4
    weight_range = (10.0, 54.0)
    mouth_offset = (0, 9)
    def __init__(self, water_rect):
        super(WhitePerch, self).__init__("White Perch", "whiteperch", choice((-1, 1)), water_rect)
        

class Pickerel(Fish):
    depth_range = (250, 450)
    speed = .5
    weight_range = (17.0, 80.0)
    mouth_offset = (0, 6)
    def __init__(self, water_rect):
        super(Pickerel, self).__init__("Pickerel", "pickerel", choice((-1, 1)), water_rect)
    
class Bass(Fish):
    depth_range = (250, 500)
    speed = .5
    weight_range = (22.0, 96.0)
    mouth_offset = (0, 13)
    def __init__(self, water_rect):
        super(Bass, self).__init__("Bass", "bass", choice((-1, 1)), water_rect)
       

class BrookTrout(Fish):
    depth_range = (350, 500)
    speed = .5
    weight_range = (12.0, 58.0)
    mouth_offset = (0, 8)
    def __init__(self, water_rect):
        super(BrookTrout, self).__init__("Brook Trout", "trout", choice((-1, 1)), water_rect)
        
    
class LakeTrout(Fish):
    depth_range = (500, 650)
    speed = .5
    weight_range = (30.0, 163.0)
    mouth_offset = (0, 15)
    def __init__(self, water_rect):
        super(LakeTrout, self).__init__("Lake Trout", "laketrout", choice((-1, 1)), water_rect)

        
class Salmon(Fish):
    depth_range = (350, 500)
    speed = .5
    weight_range = (16.0, 78.0)
    mouth_offset = (0, 9)
    def __init__(self, water_rect):
        super(Salmon, self).__init__("Salmon", "salmon", choice((-1, 1)), water_rect)
        
        
class Pike(Fish):
    depth_range = (500, 660)
    speed = .4
    weight_range = (40.0, 192.0)
    mouth_offset = (1, 16)
    def __init__(self, water_rect):
        super(Pike, self).__init__("Pike", "pike", choice((-1, 1)), water_rect)
        
        
FISH_CLASSES = OrderedDict([("Yellow Perch", YellowPerch),
                                              ("White Perch", WhitePerch),
                                              ("White Crappie", WhiteCrappie),
                                              ("Black Crappie", BlackCrappie),
                                              ("Pickerel", Pickerel),
                                              ("Bass", Bass),
                                              ("Brook Trout", BrookTrout),
                                              ("Salmon", Salmon),
                                              ("Lake Trout", LakeTrout),                            
                                              ("Pike", Pike)])