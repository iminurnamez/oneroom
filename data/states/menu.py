from collections import deque
import pygame as pg
from .. import tools, prepare
from ..components.labels import Label, PayloadButton


class Menu(tools._State):
    def __init__(self):
        super(Menu, self).__init__()
        font = prepare.FONTS["SnowtopCaps"]
        screen_rect = pg.display.get_surface().get_rect()
        self.window = pg.Rect(0, 0, 600, 700)
        self.window.center = screen_rect.center
        self.instruct = Label(font, 24, "UP/DOWN to navigate, ENTER to select",
                                      "dodgerblue", {"midtop": (self.window.centerx, self.window.top + 10)})
        buttons = [("Leaderboard", "LEADERBOARD"),
                         ("Cooler", "COOLER_SCREEN"),
                         ("Creel", "CREEL_SCREEN"),
                         ("Stats", "STATS_SCREEN"),
                         ("Fish", "FISH_SCREEN"),
                         ("Done", "FISHING")]
        self.buttons = []
        top = self.instruct.rect.bottom + 20
        for button in buttons:
            label = Label(font, 24, button[0], "dodgerblue", {"center": (0, 0)})
            self.buttons.append(PayloadButton(screen_rect.centerx - 80, top,
                                                                160, 60, label, button[1]))
            top += 100
        self.button_cycle = deque(self.buttons)
        self.button = self.button_cycle[0]
        self.button.selected = True        
            
    def startup(self, persistent):
        self.persist = persistent
        self.button_cycle = deque(self.buttons)
        self.button = self.button_cycle[0]
        self.button.selected = True
        
            
    def get_event(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_DOWN:
                self.button.selected = False
                self.button_cycle.rotate(-1)
                self.button = self.button_cycle[0]
                self.button.selected = True
            elif event.key == pg.K_UP:
                self.button.selected = False
                self.button_cycle.rotate(1)
                self.button = self.button_cycle[0]
                self.button.selected = True
            elif event.key == pg.K_RETURN:
                self.button.selected = False
                self.next = self.button.payload
                self.done = True

    def update(self, surface, keys, dt):
        self.draw(surface)
        
    def draw(self, surface):
        pg.draw.rect(surface, pg.Color("gray90"), self.window)
        pg.draw.rect(surface, pg.Color("dodgerblue"), self.window, 3)
        self.instruct.draw(surface)
        for button in self.buttons:
            button.draw(surface)
        