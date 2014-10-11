from itertools import cycle

import pygame as pg
from .. import prepare, tools
from ..components.bgrounds import Water, Ice, Sky, Forest, TinyShack, SmallShack, MediumShack
from ..components.fisherman import Fisherman
from ..components.shack import Shack
from ..components.fishingrod import FishingRod
from ..components.fish import BlackCrappie, WhiteCrappie, YellowPerch, WhitePerch, BrookTrout, LakeTrout, Pike, Salmon
from ..components.tournaments import TOURNAMENTS
from ..components.tournament import Tournament


class Fishing(tools._State):
    def __init__(self):
        super(Fishing, self).__init__()
        self.fps = 60
        self.elapsed = 0.0
        self.screen_rect = pg.display.get_surface().get_rect()
        self.water = Water(pg.Rect(0, 400, self.screen_rect.width, self.screen_rect.height - 400))
        self.sky = Sky(pg.Rect(0, 0, self.screen_rect.width, self.water.rect.top))
        self.ice = Ice(pg.Rect(0, self.water.rect.top, self.screen_rect.width, 32))
        self.forest = Forest(self.ice.rect.topleft)
        self.shacks = [TinyShack(self.ice.rect) for _ in range(7)]
        self.shacks.extend([SmallShack(self.ice.rect) for _ in range(5)])
        self.shacks.extend([MediumShack(self.ice.rect) for _ in range(3)])
        self.shack = Shack((self.screen_rect.centerx, self.ice.rect.top))
        self.fisherman = Fisherman((self.shack.rect.left + 30, self.shack.rect.bottom))
        self.tournament_cycle = cycle(TOURNAMENTS)
        tourney = next(self.tournament_cycle)
        self.tournament = Tournament(self.water.rect, **tourney)

            
    def startup(self, persistent):
        self.persist = persistent
        if not self.tournament.started:
            self.shacks = [TinyShack(self.ice.rect) for _ in range(7)]
            self.shacks.extend([SmallShack(self.ice.rect) for _ in range(5)])
            self.shacks.extend([MediumShack(self.ice.rect) for _ in range(3)])
            stats = self.fisherman.stats
            cash = self.fisherman.cash
            self.fisherman = Fisherman((self.shack.rect.left + 30, self.shack.rect.bottom))
            self.fisherman.stats = stats
            self.fisherman.cash = cash
            self.tournament.started = True            
            
    def get_event(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                self.done = True
                self.persist["tournament"] = self.tournament
                self.persist["fisherman"] = self.fisherman
                self.persist["quitting"] = True
                self.next = "STATS_SCREEN"
            elif event.key == pg.K_RETURN:
                self.persist["tournament"] = self.tournament
                self.persist["fisherman"] = self.fisherman
                self.done = True
                self.next = "MENU"                
            elif event.key == pg.K_SPACE:
                self.fisherman.flip_state()
                
    def update(self, surface, keys, dt):
        self.elapsed += dt
        while self.elapsed >= 1000.0 / self.fps:
            self.elapsed -= 1000.0 / self.fps
            self.tournament.update()
            for fish in self.tournament.fishes:
                fish.update(self.water.rect)
            for sturgeon in self.tournament.sturgeons:
                sturgeon.update(self.water.rect)
            msg = self.fisherman.update(keys, dt, self.tournament.fishes, self.tournament.sturgeons, self.water)
            if msg:
                if msg[0] == "CATCH_WINDOW":
                    self.done = True
                    self.next = "CATCH_WINDOW"
                    self.persist["fish"] = msg[1]
                    self.persist["fisherman"] = self.fisherman
                    self.persist["tournament"] = self.tournament
            if self.tournament.ended:
                self.persist["fisherman"] = self.fisherman
                self.persist["tournament"] = self.tournament
                tourney = next(self.tournament_cycle)
                self.tournament = Tournament(self.water.rect, **tourney)
                self.persist["next tournament"] = self.tournament
                self.next = "LEADERBOARD"
                self.done = True
        self.draw(surface, dt)
        
    def draw(self, surface, dt):
        surface.fill((0,0,0))
        self.water.draw(surface)
        self.sky.draw(surface)
        self.ice.draw(surface)
        self.forest.draw(surface)
        for shack in self.shacks:
            shack.draw(surface)
        self.shack.draw(surface, dt)
        for fish in self.tournament.fishes:
            fish.draw(surface)          
        for sturgeon in self.tournament.sturgeons:
            sturgeon.draw(surface)
        self.fisherman.draw(surface, dt)
        self.tournament.time_label.draw(surface)