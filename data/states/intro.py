import pygame as pg
from .. import tools, prepare
from ..components.tournament import Tournament
from ..components.tournaments import TOURNAMENTS
from ..components.labels import GroupLabel as GLabel, Blinker


class Intro(tools._State):
    def __init__(self):
        super(Intro, self).__init__()
        screen = pg.display.get_surface().get_rect()
        font = prepare.FONTS["weblysleekuil"]
        snow_font = prepare.FONTS["SnowtopCaps"]
        self.labels = []
        title = GLabel(self.labels, snow_font, 96, "One Room Shack", "lightblue",
                                   {"midtop": (screen.centerx, screen.top + 20)})
        top = title.rect.bottom + 30
        left = 560
        lines = ["The cooler's well-stocked and there's wood in the stove so",
                    "grab a beer and pull up a bucket - it's ice fishing season!",
                    "YOU'll be competing in ice-fishing derbies to win as",
                    "much cash as you can before the season ends."]
        for line in lines:
            label = GLabel(self.labels, font, 32, line, "dodgerblue",
                                         {"topleft": (left, top)})
            top = label.rect.bottom + 3
        top += 20    
        fishing = GLabel(self.labels, font, 48, "Catching Fish", "dodgerblue", 
                                       {"midtop": (screen.centerx, top)})
        top = fishing.rect.bottom + 10
        fish_lines = ["Keep the end of your fishing line close to a fish's mouth until",
                           "the fish takes the bait. Drinking beer that a fish likes will make",
                           "them more likely to bite, but also makes controlling your fishing",
                           "rod more difficult."]
        for fish_line in fish_lines:
            fline = GLabel(self.labels, font, 32, fish_line, "dodgerblue",
                                        {"topleft": (left, top)})
            top = fline.rect.bottom + 3
        top += 20
        fc_title = GLabel(self.labels, font, 48, "Fishing Controls", "dodgerblue",
                                        {"midtop": (screen.centerx, top)})
        top = fc_title.rect.bottom + 10                                        
        controls = [("UP / DOWN", "Let out / take in fishing line"),
                         ("LEFT / RIGHT", "Retract / extend fishing rod"),
                         ("SPACE", "Switch between drinking and fishing"),
                         ("ENTER", "Open Menu"),
                         ("ESCAPE", "Quit")]
        left1 = 860
        left2 = 960
        for control_pair in controls:
            key = GLabel(self.labels, font, 32, control_pair[0], "dodgerblue", 
                                       {"topright": (left1, top)})
            use = GLabel(self.labels, font, 32, control_pair[1], "dodgerblue", 
                                       {"topleft": (left2, top)})                                       
            top = use.rect.bottom + 10
        
        self.blinker = Blinker(snow_font, 32, "Press Enter to continue", "dodgerblue",
                                       {"midbottom": (screen.centerx, screen.bottom - 20)}, 650)
        
    def startup(self, persistent):
        self.persist = persistent
        
    def get_event(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RETURN:
                self.done = True
                self.persist["tournament"] = Tournament(pg.Rect(0, 0, 10, 10), **TOURNAMENTS[0])
                self.next = "TOURNAMENT_INFO"
                
    def update(self, surface, keys, dt):
        self.draw(surface, dt)
        
    def draw(self, surface, dt):
        surface.fill(pg.Color("gray90"))
        for label in self.labels:
            label.draw(surface)
        self.blinker.draw(surface, dt)