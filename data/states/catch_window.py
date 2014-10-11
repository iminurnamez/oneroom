import pygame as pg
from .. import tools, prepare
from ..components.labels import GroupLabel


class CatchWindow(tools._State):
    def __init__(self):
        super(CatchWindow, self).__init__()
        self.next = "FISHING"
        self.font = prepare.FONTS["weblysleekuisl"]
        screen = pg.display.get_surface().get_rect()
        self.window = pg.Rect(0, 0, 400, 100)
        self.window.center = screen.center
    
    def startup(self, persistent):
        
        self.persist = persistent
        
        self.fish = self.persist["fish"]
        self.fisherman = self.persist["fisherman"]
        self.tournament = self.persist["tournament"]
        man = self.fisherman
        tourney = self.tournament
        self.labels = []
        fish_label = GroupLabel(self.labels, self.font, 18, 
                            "You caught a {:.2f} lb. {}".format(self.fish.weight/16.0, self.fish.name),
                            "gray40", {"midtop": (self.window.centerx, self.window.top + 10)})

        self.catchable = True
        if len(man.creel[self.fish.name]) >= tourney.catch_limits[self.fish.name]:
            self.catchable = False
            label1 = GroupLabel(self.labels, self.font, 18, "You've already caught the limit for this fish",
                                           "gray40", {"midtop": fish_label.rect.midbottom})
            label2 = GroupLabel(self.labels, self.font, 18, "Press Space to continue", "gray40",
                                          {"midtop": label1.rect.midbottom})            
        else:
            keep_label = GroupLabel(self.labels, self.font, 18, "Press Enter to keep or Space to throw back",
                                                 "gray40", {"midtop": fish_label.rect.midbottom})
            keep_label.rect.bottom += 10
                                                 
    def get_event(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RETURN:
                if self.catchable:
                    self.fisherman.creel[self.fish.name].append(self.fish)
                    self.fisherman.stats["caught"][self.fish.name][0] += 1
                    self.fisherman.stats["caught"][self.fish.name][1] += self.fish.weight
                    self.done = True
            elif event.key == pg.K_SPACE:
                self.done = True
    
    def update(self, surface, keys, dt):
        self.draw(surface)
        
    def draw(self, surface):
        pg.draw.rect(surface, pg.Color("gray90"), self.window)
        pg.draw.rect(surface, pg.Color("dodgerblue"), self.window, 3)
        for label in self.labels:
            label.draw(surface)
        
        