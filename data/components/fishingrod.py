from math import pi, cos, sin
from random import randint, uniform
import pygame as pg
from .. import prepare
from ..components.angles import project

GRAVITY = .02

class LineSegment(object):
    def __init__(self, centerx, topy, length, thickness, color):
       self.pos = [centerx, topy]
       self.length = length
       self.thickness = thickness
       self.color = color
       self.momentum = 0.0
       self.angle = 1.5 * pi
       self.end_pos = list(project(self.pos, self.angle, self.length))

       
    def draw(self, surface):
        int_pos = [int(self.pos[0]), int(self.pos[1])]
        int_end = [int(self.end_pos[0]), int(self.end_pos[1])]
        pg.draw.line(surface, self.color, int_pos, int_end, self.thickness)
        
        
class FishingLine(object):
    def __init__(self, midtop, length, segment_length=2, 
                         thickness=2, color=(255, 255, 255)):
        self.pos = list(midtop)
        self.length = length
        self.segment_length = segment_length
        self.thickness = thickness
        self.color = color
        self.angle_increment = .005
        self.swinger = None
        self.cooldown = 0
        self.segments = []
        for y in range(0, self.length, self.segment_length):
            self.segments.append(LineSegment(self.pos[0], self.pos[1] + y,
                                                                   self.segment_length,
                                                                   self.thickness, self.color))                                                                  

    
    
    
    
    def update(self, rod_end):
        gravity = .01
        for segment in self.segments[::-1]:
            if segment.angle < 1.5 * pi:
                segment.angle += gravity
            elif segment.angle > 1.5 * pi:
                segment.angle -= gravity
            gravity *= .99
        top_pos = list(rod_end)             
        for segment in self.segments:
            segment.pos = top_pos
            segment.end_pos = list(project(segment.pos, segment.angle, segment.length))
            top_pos = segment.end_pos            
            
    def draw(self, surface):
        for segment in self.segments:
            segment.draw(surface)
            
            
            
class FishingRod(object):
    def __init__(self, hand_pos):
        self.hand_pos = hand_pos
        self.length = 100
        self.min_length = 60
        self.max_length = 360
        self.rod_end = [self.hand_pos[0] + self.length, self.hand_pos[1]]
        self.line = FishingLine(self.rod_end, 130)
        self.fish_on = False
        self.splash = prepare.SFX["fishsplash"]
            
    def draw(self, surface):
        pg.draw.line(surface, pg.Color("saddlebrown"), self.hand_pos, self.rod_end, 2)
        self.line.draw(surface)
        if self.fish_on:
            self.fish.draw(surface)
        
    def update(self, fishes, sturgeons, fisherman, water):
        msg = None
        if self.fish_on:
            self.fish_ticks += 1
            if not self.fish_ticks % 3:
                self.reel("up", fisherman.bac)
            self.fish.pos = self.line.segments[-1].end_pos
            f = self.fish
            f.rect.center = (f.pos[0] - (f.x_velocity * (f.rect.width//2)),
                                   f.pos[1])
            for sturgeon in sturgeons:
                if any([c.colliderect(self.fish.rect) for c in sturgeon.colliders]):
                    self.fish = None
                    self.fish_on = False
                    return
            if self.fish.pos[1] <= water.rect.top + 32:
                if not self.fish.out_of_water:
                    self.fish.out_of_water = True
                    self.splash.play()
            if self.fish.pos[1] <= water.rect.top + 35:
                self.fish.image = pg.transform.rotate(self.fish.images[-1], -90)
                self.fish.rect = self.fish.image.get_rect(midtop = self.line.segments[-1].end_pos)
            if self.fish.pos[1] < self.rod_end[1] + 3:
                msg = "CATCH_WINDOW", self.fish
                self.fish = None
                self.fish_on = False
                
        else:
            hook = pg.Rect(0, 0, 9, 9)
            hook.center = self.line.segments[-1].end_pos
            for fish in fishes:
                mouth = (fish.rect.centerx + (fish.x_velocity * ((fish.rect.width//2) - fish.mouth_offset[0])),
                               fish.rect.top + fish.mouth_offset[1])
                if hook.collidepoint(mouth):
                    chance = 10 + (fisherman.bac * fisherman.beer.bonuses[fish.name])
                    if randint(0, 2000) < chance:
                        fish.caught = True
                        fishes.remove(fish)
                        self.fish = fish
                        self.fish_on = True
                        self.fish_ticks = 0
                        break           
        self.rod_end = (self.hand_pos[0] + self.length, self.hand_pos[1])
        self.line.update(self.rod_end)
        return msg
        
         
        
        
        
        
    def extend_rod(self, direction, bac):
        end = self.line.segments[-1]
        force = .015 + uniform(-bac/5.0, bac/5.0) 
        if direction == "left" and self.length > self.min_length:
            
            for segment in self.line.segments[::-1]:
                segment.pos[0] -= 2
                segment.angle = min(1.55 * pi, segment.angle + force)
                force *= .99
            self.length -= 2    
        elif direction == "right" and self.length < self.max_length:
            for segment in self.line.segments[::-1]:
                segment.pos[0] += 2
                segment.angle = max(1.45 * pi, segment.angle - force)
                force *= .99
            self.length += 2
            
    def reel(self, direction, bac):        
        if not(randint(0, 100) < bac * 200):
            num = 1
            jerk = randint(0, 100) < (bac * 100)
            if jerk:
                num = randint(2, 4) 
            if direction == "down":
                for _ in range(num):
                    end_pos = self.line.segments[-1].end_pos
                    new_segment = LineSegment(end_pos[0], end_pos[1], self.line.segment_length,
                                                             self.line.thickness, self.line.color)
                    new_segment.angle = self.line.segments[-1].angle            
                    self.line.segments.append(new_segment)
            elif direction == "up":
                for _ in range(num):
                    if len(self.line.segments) > 1:
                        self.line.segments.pop()
                 
            
            
            
            
            
            