import pygame as pg
from .. import tools, prepare
from ..components.labels import GroupLabel, Blinker


class CreelScreen(tools._State):
    def __init__(self):
        super(CreelScreen, self).__init__()
        self.next = "MENU"
        screen = pg.display.get_surface().get_rect()
        self.window = pg.Rect(0, 0, 600, 700)
        self.window.center = screen.center
        
        
    def startup(self, persistent):
        self.persist = persistent
        self.fisherman = self.persist["fisherman"]
        self.tournament = self.persist["tournament"]
        self.labels = []
        font = prepare.FONTS["weblysleekuisb"]
        snow_font = prepare.FONTS["SnowtopCaps"]
        species = GroupLabel(self.labels, font, 24, "Species", "dodgerblue",
                                        {"midtop": (self.window.left + 70, self.window.top + 20)})
        weight_label = GroupLabel(self.labels, font, 24, "Weights", "dodgerblue",
                                                {"midtop": (self.window.left + 300, self.window.top + 20)})
        limit_label = GroupLabel(self.labels, font, 24, "Catch Limit", "dodgerblue",
                                             {"midtop": (self.window.left + 520, self.window.top + 20)})
        top = self.window.top + 100
        for fish_name in self.fisherman.creel:
            name = GroupLabel(self.labels, font, 16, fish_name, "dodgerblue",
                                          {"midtop": (species.rect.centerx, top)})
            weights = ["{:.2f}".format(x.weight/16.0) for x in self.fisherman.creel[fish_name]]
            weight = GroupLabel(self.labels, font, 16, "{}".format(weights).strip("[]").replace("'", ""),
                                           "dodgerblue", {"midtop": (weight_label.rect.centerx, top)})
            limit = GroupLabel(self.labels, font, 16, "{}/{}".format(len(weights), self.tournament.catch_limits[fish_name]),
                                        "dodgerblue", {"midtop": (limit_label.rect.centerx, top)})
            top += 50
        self.blinker = Blinker(snow_font, 32, "Press Enter to close", "dodgerblue",
                                       {"midbottom": (self.window.centerx, self.window.bottom - 20)}, 550)
                                       
    def get_event(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RETURN:
                self.done = True            
    
    def update(self, surface, keys, dt):
        self.draw(surface, dt)
    
    
    def draw(self, surface, dt):
        pg.draw.rect(surface, pg.Color("gray90"), self.window)
        pg.draw.rect(surface, pg.Color("dodgerblue"), self.window, 3)
        for label in self.labels:
            label.draw(surface)
        self.blinker.draw(surface, dt)
        
        
    
            