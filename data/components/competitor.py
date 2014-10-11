from random import randint, choice
import pygame as pg
from ..components.name_generator import generate_name
from ..components.fish import FISH_CLASSES


class Competitor(object):
    def __init__(self):
        self.name = generate_name()
        self.skill = randint(10, 100)
        self.creel = {k: [] for k in FISH_CLASSES}
                           
    def update(self, tournament):
        if randint(0, 120000) < self.skill:
            self.catch_fish(tournament)
            
    def catch_fish(self, tournament):
        fish_type = choice(["White Crappie", "Yellow Perch", "Pickerel",
                                     "Black Crappie", "White Perch", "Pickerel",
                                     "Bass", "Lake Trout",
                                     "Brook Trout", "Salmon", "Pike"])
        if len(self.creel[fish_type]) < tournament.catch_limits[fish_type]:
            self.creel[fish_type].append(FISH_CLASSES[fish_type](tournament.water_rect))
            

        
    