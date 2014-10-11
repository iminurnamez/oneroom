from collections import OrderedDict, Counter
import pygame as pg

from ..components.competitor import Competitor
from ..components.fish import FISH_CLASSES
from ..components.labels import Label
from ..prepare import FONTS, SCREEN_SIZE
from ..components.sturgeon import Sturgeon

class Tournament(object):
    font = FONTS["SnowtopCaps"]
    def __init__(self, water_rect, name=None, num_competitors=50, catch_limits=None, fish_mins=None,
                         sturgeons=None, prizes=None, entry_fee=10, time_limit=7200):
        self.water_rect = water_rect
        self.name = name
        self.competitors = [Competitor() for _ in range(num_competitors)]
        self.catch_limits = OrderedDict(catch_limits)
        self.fish_mins = dict(fish_mins)
        self.fishes = []
        for fish in self.fish_mins:
            for _ in range(self.fish_mins[fish]):
                self.fishes.append(FISH_CLASSES[fish](self.water_rect))
        self.sturgeons = [Sturgeon(self.water_rect, *sturgeon) for sturgeon in sturgeons]
        self.prizes = prizes
        self.first_fish = False
        self.time_left = time_limit
        self.started = False
        self.ended = False
        self.make_time_label()
        
        
    def make_time_label(self):
        h, rem = divmod(self.time_left, 1800)
        m, rem = divmod(rem, 30)
        s, rem = divmod(rem, .5)
        self.time_label = Label(self.font, 32, "{}:{:02}:{:02}".format(h, m, int(s)),
                                          "gray20", {"topleft": (SCREEN_SIZE[0] - 120, 10)})
                                          
    def update(self):
        self.time_left -= 1
        if self.time_left <= 0:
            self.ended = True
        self.make_time_label()
        for competitor in self.competitors:
            competitor.update(self)
        fish_counts = Counter([x.name for x in self.fishes])
        for fish in self.fish_mins:
            if fish_counts[fish] < self.fish_mins[fish]:
                self.fishes.append(FISH_CLASSES[fish](self.water_rect))

        
                
