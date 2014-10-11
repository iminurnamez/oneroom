import pygame as pg
from .. import tools, prepare
from ..components.labels import Label


class MessageWindow(tools._State):
    font = prepare.FONTS["Fixedsys500c"]
    def __init__(self):
        super(MessageWindow, self).__init__()
        screen_rect = pg.display.get_surface().get_rect()
        self.next = "FISHING"
        self.rect = pg.Rect(0,0,200, 120)
        self.rect.center = screen_rect.center
        
    def startup(self, persistent):
        self.persist = persistent    
        self.label = Label(self.font, 24, self.persist["message"],
                                  "navyblue", {"center": self.rect.center})
        
    def get_event(self, event):
        if event.type == pg.KEYDOWN:
            self.done = True
            
    def update(self, surface, keys, dt):
        self.draw(surface)
        
    def draw(self, surface):
        pg.draw.rect(surface, pg.Color("gray99"), self.rect)
        pg.draw.rect(surface, pg.Color("navyblue"), self.rect, 3)
        self.label.draw(surface)