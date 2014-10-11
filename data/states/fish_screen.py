import pygame as pg
from .. import tools, prepare
from ..components.labels import GroupLabel, Blinker
from ..components.fish import FISH_CLASSES

class FishScreen(tools._State):
    def __init__(self):
        super(FishScreen, self).__init__()
        self.next = "MENU"
        screen = pg.display.get_surface().get_rect()
        self.window = pg.Rect(0, 0, 600, 700)
        self.window.center = screen.center
        water_rect = pg.Rect(0, 0, 10, 10)
        self.fishes = [FISH_CLASSES[x](water_rect) for x in FISH_CLASSES]
        self.labels = []
        font  = prepare.FONTS["weblysleekuisl"]
        italic_font = prepare.FONTS["weblysleekuisbi"]
        snow_font = prepare.FONTS["SnowtopCaps"]
        species = GroupLabel(self.labels, italic_font, 24, "Species", "dodgerblue",
                                        {"midtop": (self.window.left + 260, self.window.top + 20)})
        weight = GroupLabel(self.labels, italic_font, 24, "Average Weight", "dodgerblue",
                                       {"midtop": (self.window.left + 460, self.window.top + 20)})
        self.icons = []
        y = self.window.top + 100
        for fish in self.fishes:
            icon = fish.images[-1]
            icon_rect = icon.get_rect(center=(self.window.left + 80, y))
            self.icons.append((icon, icon_rect))
            name = GroupLabel(self.labels, font, 20, fish.name, "gray40", 
                                          {"center": (species.rect.centerx, y)})
            avg_weight = (sum(fish.weight_range) / 2) / 16.0
            weight_label = GroupLabel(self.labels, font, 20, "{:.2f}".format(avg_weight), "gray40",
                                                    {"center": (weight.rect.centerx, y)})
            y += 50
        self.blinker = Blinker(snow_font, 32, "Press Enter to close", "dodgerblue",
                                       {"midbottom": (self.window.centerx, self.window.bottom - 20)},
                                       550)
            
    def startup(self, persistent):
        self.persist = persistent
    
    
    def get_event(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RETURN:
                self.done = True            
    
    def update(self, surface, keys, dt):
        self.draw(surface, dt)
    
    def draw(self, surface, dt):
        pg.draw.rect(surface, pg.Color("gray90"), self.window)
        pg.draw.rect(surface, pg.Color("dodgerblue"), self.window, 3)
        for icon in self.icons:
            surface.blit(icon[0], icon[1])
        for label in self.labels:
            label.draw(surface)
        self.blinker.draw(surface, dt)
        
    