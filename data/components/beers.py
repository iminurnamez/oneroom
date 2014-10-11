import pygame as pg
from .. import prepare
from ..components.labels import Label
from ..components.fish import FISH_CLASSES

class Beer(object):
    font = prepare.FONTS["weblysleekuisli"]
    bold_font = prepare.FONTS["weblysleekuisb"]
    
    def __init__(self, name, description, bonuses):
        self.name = name
        self.icon = prepare.GFX["".join(self.name.lower().split())]
        self.icon_rect = self.icon.get_rect()
        self.name_label = Label(self.bold_font, 20, self.name, "gray40",
                                            {"center": (0, 0)})
        self.descriptions = []
        for line in description:
            self.descriptions.append(Label(self.font, 16, line, "gray40",
                                                         {"center": (0, 0)}))
        self.bonuses = {name: bonus for name, bonus in zip(FISH_CLASSES.keys(), bonuses)}
        
    def draw(self, surface):
        surface.blit(self.icon, self.icon_rect)
        self.name_label.draw(surface)
        for description in self.descriptions:
            description.draw(surface)
        
        
class GutLight(Beer):
    def __init__(self):
        super(GutLight, self).__init__("Gut Light",
                                                    ["Crappie, Perch and Pickerel like this watery",
                                                     "brew. Salmon and Trout turn up their noses."],
                                                    [100, 100, 100, 100, 100, 20, 0, 0, 0, 10])
        

class Gutweiser(Beer):
    def __init__(self):
        super(Gutweiser, self).__init__("Gutweiser",
                                                      ["Bass can't resist the Monarch of Beers."],
                                                      [50, 50, 50, 50, 50, 150, 0, 0, 0, 20])


class Porter(Beer):
    def __init__(self):
        super(Porter, self).__init__("Sierra Madre Porter",
                                        ["Salmon, Trout and Pike all enjoy porter."],
                                        [0, 0, 0, 0, 10, 30, 80, 70, 50, 50])       


class IPA(Beer):
    def __init__(self):
        super(IPA, self).__init__("Toppy Header IPA",
                                        ["Salmon have been fawning over this",
                                         "hoppy brew since way before it was cool."],
                                        [0, 0, 0, 0, 20, 20, 80, 100, 20, 20])


class Stout(Beer):
    def __init__(self):
        super(Stout, self).__init__("Catfish Head Stout",
                                        ["Without a doubt, Pike like stout,",
                                         "but smaller fish will spit it out."],
                                        [0, 0, 0, 0, 0, 10, 50, 50, 70, 150])


class Lager(Beer):
    def __init__(self):
        super(Lager, self).__init__("Babbling Brook Lager",
                                        ["Brookies find this brew especially delicious."],
                                        [20, 20, 20, 20, 20, 20, 100, 10, 10, 10])


class Steineken(Beer):
    def __init__(self):
        super(Steineken, self).__init__("Steineken",
                                        ["Pickerel love this green-bottled import."],
                                        [30, 30, 30, 30, 150, 50, 20, 20, 0, 0])