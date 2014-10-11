import pygame as pg
from .. import tools, prepare
from ..components.labels import Label, Blinker


class Leaderboard(tools._State):
    def __init__(self):
        super(Leaderboard, self).__init__()
        self.font = prepare.FONTS["weblysleekuil"]
        self.italic = prepare.FONTS["weblysleekuili"]
        self.snow_font = prepare.FONTS["SnowtopCaps"]
        self.next = "MENU"
        
    def startup(self, persistent):
        self.persist = persistent
        screen_rect = pg.display.get_surface().get_rect()
        self.window = pg.Rect(0, 0, 600, 700)
        self.window.center = screen_rect.center
        self.tournament = self.persist["tournament"]
        self.fisherman = self.persist["fisherman"]
        if self.tournament.ended:
            name_text = "{} Results".format(self.tournament.name)
            self.final = True
            self.next = "TOURNAMENT_INFO"
        else:
            name_text = self.tournament.name
            self.final = False
            self.next = "MENU"
        self.name_title = Label(self.snow_font, 32, name_text, "lightblue",
                                          {"midtop": (self.window.centerx, self.window.top + 5)})
       
        top = self.name_title.rect.bottom + 2
        for prize in self.tournament.prizes:
            prize.update(self.fisherman, self.tournament, (self.window.centerx, top), self.final)
            top += (len(prize.prize_amounts) * 25) + 30
        self.blinker = Blinker(self.snow_font, 32, "Press Enter to close",
                                       "dodgerblue", {"midbottom": (self.window.centerx,
                                                                                self.window.bottom - 15)},
                                        500)
        
            
    def get_event(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RETURN:
                if self.final:
                    self.next = "TOURNAMENT_INFO"
                    self.persist["tournament"] = self.persist["next tournament"]
                self.done = True
    
    def update(self, surface, keys, dt):
        self.draw(surface, dt)
        
    def draw(self, surface, dt):
        pg.draw.rect(surface, pg.Color("gray90"), self.window)
        pg.draw.rect(surface, pg.Color("dodgerblue"), self.window, 3)
        self.name_title.draw(surface)
        for prize in self.tournament.prizes:
            prize.draw(surface)
        self.blinker.draw(surface, dt)