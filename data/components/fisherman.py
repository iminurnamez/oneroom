from itertools import cycle
from collections import OrderedDict, defaultdict
import pygame as pg
from .. import prepare
from ..components.labels import Label, Blinker
from ..components.fishingrod import FishingRod
from ..components.beers import GutLight


class Fisherman(object):
    def __init__(self, bottomleft, name="YOU"):
        screen = pg.display.get_surface().get_rect()
        self.name = name
        self.image = prepare.GFX["fisherman"]
        self.rect = self.image.get_rect(bottomleft=bottomleft)
        arm = prepare.GFX["beerarm"]
        drink_cycle = [pg.transform.rotate(arm, x) for x in range(0, 60, 2)]
        drink_cycle = drink_cycle + drink_cycle[::-1]
        drink_cycle = cycle(drink_cycle)
        self.arm_images  = {"Fishing": cycle([prepare.GFX["arm"]]),
                                       "Drinking": drink_cycle}
        self.state = "Fishing"
        self.arm_image = next(self.arm_images[self.state])
        self.shoulder_pos = self.rect.left + 30, self.rect.top + 49
        
        self.arm_rect = self.arm_image.get_rect(center=self.shoulder_pos)
        self.elapsed = 0.0
        self.font = prepare.FONTS["weblysleekuisb"]
        self.bac = 0.0
        self.bac_label = Label(self.font, 32, "BAC: {:.2f}".format(self.bac),
                                         "dodgerblue", {"topleft": (0, 30)})        
        self.hand_pos = (self.rect.left + 60, self.rect.top + 58)
        self.cooler_images = {"Drinking": prepare.GFX["cooleropen"],
                                         "Fishing": prepare.GFX["coolershut"]}
        self.cooler_rect = self.cooler_images[self.state].get_rect(
                                    bottomleft=(self.rect.left, self.rect.bottom))
                                            
        
        
        self.fishing_rod = FishingRod(self.hand_pos)
        self.creel = OrderedDict([("Black Crappie", []),
                                             ("White Crappie", []),
                                             ("Yellow Perch", []),
                                             ("White Perch", []),
                                             ("Pickerel", []),
                                             ("Bass", []),
                                             ("Brook Trout", []),
                                             ("Lake Trout", []),
                                             ("Salmon", []),
                                             ("Pike", [])])
        self.stats = {"caught": {k:[0, 0] for k in self.creel.keys()},
                           "winnings": defaultdict(int),
                           "prizes": defaultdict(int)
                           }
        self.cash = 0.0
        self.cash_label = Label(self.font, 32, "${:.2f}".format(self.cash), "dodgerblue",
                                          {"topleft": (0, 0)})
        self.beer = GutLight()
        self.stupor_label = Blinker(prepare.FONTS["SnowtopCaps"], 64, "Drunken Stupor",
                                               "dodgerblue", {"center": screen.center}, 400)
                                               
    def flip_state(self):
        if self.state == "Fishing":
            self.state = "Drinking"
            self.elapsed = 0.0
            self.rod = FishingRod(self.hand_pos)
            
        elif self.state == "Drinking":
            self.state = "Fishing"
        self.arm_image = next(self.arm_images[self.state])
        self.arm_rect = self.arm_image.get_rect(center=self.shoulder_pos)
        
    def update(self, keys, dt, fishes, sturgeons, water):
        msg = None
        self.bac = max(0.0, self.bac - .00002)
        self.elapsed += dt
        if self.state == "Fishing":
            if self.elapsed >= 35:
                pass
            bac = self.bac
            if keys[pg.K_LEFT]:
                self.fishing_rod.extend_rod("left", bac)
            elif keys[pg.K_RIGHT]:
                self.fishing_rod.extend_rod("right", bac)
            
            
            if not self.fishing_rod.fish_on:            
                if keys[pg.K_UP]:
                    self.fishing_rod.reel("up", bac)
                elif keys[pg.K_DOWN]:
                    self.fishing_rod.reel("down", bac)
            msg = self.fishing_rod.update(fishes, sturgeons, self, water)
        
        elif self.state == "Drinking":
            self.bac += .0002            
            while self.elapsed >= 35:
                self.elapsed -= 35
                self.arm_image = next(self.arm_images[self.state])
                self.arm_rect=self.arm_image.get_rect(center=self.shoulder_pos)
        self.bac_label = Label(self.font, 32, "BAC: {:.2f}".format(self.bac), "dodgerblue", {"topleft": (0, 30)})
        self.cash_label = Label(self.font, 32, "${:.2f}".format(self.cash), "dodgerblue",
                                          {"topleft": (0, 0)})
        return msg
        
    def draw(self, surface, dt):
        surface.blit(self.cooler_images[self.state], self.cooler_rect)
        surface.blit(self.image, self.rect)
        surface.blit(self.arm_image, self.arm_rect)
        self.cash_label.draw(surface)
        self.bac_label.draw(surface)
        if self.state == "Fishing":
            self.fishing_rod.draw(surface)
        if self.bac > .3:
            self.stupor_label.draw(surface, dt)
        
        