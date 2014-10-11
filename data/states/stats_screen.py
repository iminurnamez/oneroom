import pygame as pg
from .. import tools, prepare
from ..components.labels import GroupLabel as GLabel, Blinker


class StatsScreen(tools._State):
    def __init__(self):
        super(StatsScreen, self).__init__()
        self.next = "MENU"
        screen = pg.display.get_surface().get_rect()
        self.window = pg.Rect(0, 0, 600, 700)
        self.window.center = screen.center
        
    def startup(self, persistent):
        self.persist = persistent
        font = prepare.FONTS["weblysleekuisl"]
        bold = prepare.FONTS["weblysleekuisb"]
        snow_font = prepare.FONTS["SnowtopCaps"]
        stats = self.persist["fisherman"].stats
        self.labels = []
        top = self.window.top + 20
        tw = GLabel(self.labels, bold, 24, "Total Winnings", "dodgerblue",
                           {"midtop": (self.window.centerx, top)})
        top = tw.rect.bottom + 5
        total = GLabel(self.labels, bold, 20, "${}".format(self.persist["fisherman"].cash), "dodgerblue",
                           {"midtop": (self.window.centerx, top)})
        top = total.rect.bottom + 10
        caught = GLabel(self.labels, bold, 24, "Fish Caught", "dodgerblue",
                           {"midtop": (self.window.centerx, top)})
        top = caught.rect.bottom + 10
        for fish_name in stats["caught"]:
            name =  GLabel(self.labels, font, 20, fish_name, "dodgerblue",
                           {"topleft": (self.window.left + 100, top)})
            num = GLabel(self.labels, font, 20, "{}".format(stats["caught"][fish_name][0]), "dodgerblue",
                           {"topleft": (self.window.left + 300, top)})
            weight = GLabel(self.labels, font, 20, "{:.2f} lbs".format(stats["caught"][fish_name][1]/16.0), "dodgerblue",
                           {"topleft": (self.window.left + 500, top)})
            top = weight.rect.bottom + 5
        tot_fish = sum([stats["caught"][f][0] for f in stats["caught"]])
        tot_weight = sum([stats["caught"][f][1] for f in stats["caught"]])/16.0        
        total_name = GLabel(self.labels, bold, 20, "Total", "dodgerblue",
                           {"topleft": (self.window.left + 100, top)})
        total_fish = GLabel(self.labels, bold, 20, "{}".format(tot_fish), "dodgerblue",
                           {"topleft": (self.window.left + 300, top)})              
        total_weight = GLabel(self.labels, bold, 20, "{:.2f} lbs".format(tot_weight), "dodgerblue",
                           {"topleft": (self.window.left + 500, top)})
        if self.persist["quitting"]:
            self.blinker = Blinker(snow_font, 32, "Enter to quit or Esc to Cancel".format(), "dodgerblue",
                           {"midbottom": (self.window.centerx, self.window.bottom - 20)}, 550)
        else:
            self.blinker = Blinker(snow_font, 32, "Press Enter to Continue", "dodgerblue",
                                            {"midbottom": (self.window.centerx, self.window.bottom - 20)}, 550)
                                            
    def get_event(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RETURN:
                if self.persist["quitting"]:
                    self.quit = True
                    self.done = True
                else:
                    self.done = True
            elif event.key == pg.K_ESCAPE:
                self.done = True
                            
    def update(self, surface, keys, dt):
        self.draw(surface, dt)
        
        
    def draw(self, surface, dt):
        pg.draw.rect(surface, pg.Color("gray90"), self.window)
        pg.draw.rect(surface, pg.Color("dodgerblue"), self.window, 3)
        for label in self.labels:
            label.draw(surface)
        self.blinker.draw(surface, dt)