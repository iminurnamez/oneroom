import pygame as pg
from .. import tools, prepare
from ..components.labels import Label, GroupLabel as GLabel, Blinker

class TitleScreen(tools._State):
    def __init__(self):
        super(TitleScreen, self).__init__()
        self.next = "INTRO"
        screen = pg.display.get_surface().get_rect()
        font = prepare.FONTS["SnowtopCaps"]
        self.labels = []
        one = GLabel(self.labels, font, 256, "ONE", "lightblue",
                                {"center": (screen.centerx, screen.top + 150)})
        room = GLabel(self.labels, font, 256, "ROOM", "lightblue",
                                {"center": (screen.centerx, screen.top + 450)})
        shack = GLabel(self.labels, font, 256, "SHACK", "lightblue",
                                {"center": (screen.centerx, screen.top + 750)})
        self.blinker = Blinker(font, 48, "Press Enter to continue", "dodgerblue",
                                        {"midbottom": (screen.centerx, screen.bottom - 50)},
                                        500)
        pg.mixer.music.load(prepare.MUSIC["icenoise"])
        pg.mixer.music.play(-1)
        self.persist["quitting"] = False
        
    def get_event(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RETURN:
                self.done = True
            
    def update(self, surface, keys, dt):
        self.draw(surface, dt)
        
    def draw(self, surface, dt):
        surface.fill(pg.Color("gray90"))
        for label in self.labels:
            label.draw(surface)
        self.blinker.draw(surface, dt)