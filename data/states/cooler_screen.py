from collections import deque
import pygame as pg
from .. import tools, prepare
from ..components.labels import Label
from ..components.beers import (GutLight, Gutweiser, Porter, IPA, Stout,
                                                   Lager, Steineken)
                                                   
                                                  
class CoolerScreen(tools._State):
    def __init__(self):
        super(CoolerScreen, self).__init__()
        self.font = prepare.FONTS["weblysleekuil"]
        self.winter_font = prepare.FONTS["SnowtopCaps"]
        self.next = "MENU"
        self.screen_rect = pg.display.get_surface().get_rect()
        self.window = pg.Rect(0, 0, 600, 700)
        self.window.center = self.screen_rect.center
        self.instruct = Label(self.winter_font, 28, "UP/DOWN to navigate, ENTER to select",
                                      "dodgerblue", {"midtop": (self.window.centerx, self.window.top + 30)})
        self.beers = [GutLight(), Gutweiser(), Porter(), IPA(), Stout(), Lager(), Steineken()]
        top = self.instruct.rect.bottom + 50
        self.beer_rects = [pg.Rect(self.window.left, top + (y * 80), self.window.width, 80)
                                   for y in range(len(self.beers))]
        
    def startup(self, persistent):
        self.persist = persistent
        self.fisherman = self.persist["fisherman"]
        for rect, beer in zip(self.beer_rects, self.beers):
            beer.icon_rect.center = (rect.left + 25, rect.centery)
            beer.name_label.rect.midleft = (rect.left + 55, rect.centery)
            top = rect.top + 20
            for label in beer.descriptions:
                label.rect.topleft = (rect.left + 280, top)
                top = label.rect.bottom
        self.beer_cycle = deque(self.beers)
        self.current_beer = self.beer_cycle[0]
        self.rect_cycle = deque(self.beer_rects)
        self.current_rect = self.rect_cycle[0]

    def get_event(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_DOWN:
                self.beer_cycle.rotate(-1)
                self.current_beer = self.beer_cycle[0]
                self.rect_cycle.rotate(-1)
                self.current_rect = self.rect_cycle[0]
            elif event.key == pg.K_UP:
                self.beer_cycle.rotate(1)
                self.current_beer = self.beer_cycle[0]
                self.rect_cycle.rotate(1)
                self.current_rect = self.rect_cycle[0]
            elif event.key == pg.K_RETURN:
                self.fisherman.beer = self.current_beer
                self.done = True

    def update(self, surface, keys, dt):
        self.draw(surface)
        
    def draw(self, surface):
        pg.draw.rect(surface, pg.Color("gray90"), self.window)
        pg.draw.rect(surface, pg.Color("dodgerblue"), self.window, 3)
        self.instruct.draw(surface)
        for beer in self.beers:
            beer.draw(surface)
        pg.draw.rect(surface, pg.Color("dodgerblue"), self.current_rect, 2)