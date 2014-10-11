import pygame as pg
from .. import tools, prepare
from ..components.labels import GroupLabel, Blinker


class TournamentInfo(tools._State):
    def __init__(self):
        super(TournamentInfo, self).__init__()
        self.next = "FISHING"
        
    def startup(self, persistent):
        self.persist = persistent
        self.tournament = self.persist["tournament"]
        
        screen = pg.display.get_surface().get_rect()
        font = prepare.FONTS["weblysleekuisl"]
        bold = prepare.FONTS["weblysleekuisb"]
        snow_font = prepare.FONTS["SnowtopCaps"]
        self.labels = []
        tourney = self.tournament
        title = GroupLabel(self.labels, snow_font, 64, tourney.name,
                                    "dodgerblue", {"midtop": (screen.centerx, screen.top + 25)})
        time_label = GroupLabel(self.labels, font, 32, "Time Limit: {} hours".format(tourney.time_left/1800),
                                             "dodgerblue", {"midtop": (screen.centerx, title.rect.bottom + 5)})                                             
        catch_label = GroupLabel(self.labels, bold, 32, "Catch Limits", "dodgerblue",
                                              {"midtop": (screen.centerx, time_label.rect.bottom + 5)})
        
        top = catch_label.rect.bottom + 10
        limits = list(tourney.catch_limits.items())
        old_top = top
        for fish, limit in limits[:len(limits) - (len(limits) // 2)]:
            fish_label = GroupLabel(self.labels, font, 24, fish, "dodgerblue",
                                                {"midtop": (screen.centerx - 150, top)})
            limit_label = GroupLabel(self.labels, font, 24, "{}".format(limit), "dodgerblue",
                                                 {"midtop": (screen.centerx - 50, top)})
            top = fish_label.rect.bottom
        top = old_top    
        for fish, limit in limits[len(limits) - (len(limits) // 2):]:
            fish_label = GroupLabel(self.labels, font, 24, fish, "dodgerblue",
                                                {"midtop": (screen.centerx + 80, top)})
            limit_label = GroupLabel(self.labels, font, 24, "{}".format(limit), "dodgerblue",
                                                 {"midtop": (screen.centerx + 180, top)})
            top = fish_label.rect.bottom
        
        
        top += 15 
        
        if len(tourney.prizes) > 3:
            old_top = top
            centerx = screen.centerx - 300
            for prize in tourney.prizes[:len(tourney.prizes) - (len(tourney.prizes)//2)]:
                prize_title = GroupLabel(self.labels, bold, 28, prize.name, "dodgerblue",
                                                {"midtop": (centerx, top)})
                top = prize_title.rect.bottom
                for amount in prize.prize_amounts:
                    amount_label = GroupLabel(self.labels, font, 20, "${}".format(amount), "dodgerblue", 
                                                             {"midtop": (centerx, top)})
                    top = amount_label.rect.bottom
                top += 15
            top = old_top
            centerx = screen.centerx + 300
            for prize in tourney.prizes[len(tourney.prizes) - (len(tourney.prizes)//2):]:
                prize_title = GroupLabel(self.labels, bold, 28, prize.name, "dodgerblue",
                                                {"midtop": (centerx, top)})
                top = prize_title.rect.bottom
                for amount in prize.prize_amounts:
                    amount_label = GroupLabel(self.labels, font, 20, "${}".format(amount), "dodgerblue", 
                                                             {"midtop": (centerx, top)})
                    top = amount_label.rect.bottom
                top += 15
            
        else:
            for prize in tourney.prizes:
                prize_title = GroupLabel(self.labels, bold, 28, prize.name, "dodgerblue",
                                                    {"midtop": (screen.centerx, top)})
                top = prize_title.rect.bottom
                for amount in prize.prize_amounts:
                    amount_label = GroupLabel(self.labels, font, 20, "${}".format(amount), "dodgerblue", 
                                                             {"midtop": (screen.centerx, top)})
                    top = amount_label.rect.bottom
                top += 15
            
        self.blinker = Blinker(snow_font, 32, "Press Enter to start derby", "dodgerblue",
                                       {"midbottom": (screen.centerx, screen.bottom - 30)}, 600)
                                       
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