import pygame as pg
from .. import prepare
from .labels import Label, GroupLabel



class Prize(object):
    def __init__(self, name, prize_amounts, slot_width=450, slot_height=20):
        self.font = prepare.FONTS["weblysleekuil"]
        self.prize_amounts = prize_amounts
        self.slot_width = slot_width
        self.slot_height = slot_height
        self.name = name
        self.title = Label(self.font, 24, name, "dodgerblue", {"center": (0, 0)})
        
    def update(self, fisherman, tournament, midtop, final=False):
        self.labels = []
        leaders = self.get_leaders(fisherman, tournament)
        mt = midtop
        self.title.rect.midtop = mt
        mt = mt[0], self.title.rect.bottom + 5
        
        self.slots = []
        height = self.slot_height * len(self.prize_amounts)
        for y in range(mt[1], mt[1] + height, self.slot_height):
            self.slots.append(pg.Rect(mt[0] - (self.slot_width // 2), y, self.slot_width, self.slot_height))     
        for i, slotleader in enumerate(zip(self.slots, leaders)):
            slot, leader = slotleader
            name_label = GroupLabel(self.labels, self.font, 16, leader[0].name, "gray40",
                                                  {"midleft": (slot.left + 5, slot.centery)})
            try:
                fish_text = leader[1].name
            except AttributeError:
                fish_text = ""            
            fish_label = GroupLabel(self.labels, self.font, 16, fish_text,    
                                                "gray40", {"midleft": (slot.left + 180, slot.centery)})
            try:
                weight_text = "{:.2f}".format(leader[1].weight / 16.0)
            except AttributeError:
                weight_text = "{:.2f}".format(leader[1] / 16.0)
            weight_label = GroupLabel(self.labels, self.font, 16, weight_text,
                                                    "gray40", {"midleft": (slot.left + 320, slot.centery)})
            if final:
                if leader[0].name == fisherman.name:
                    fisherman.cash += self.prize_amounts[i]
                    fisherman.stats["prizes"][self.name] += 1
                    fisherman.stats["winnings"][tournament.name] += self.prize_amounts[i]
        for slot, amount in zip(self.slots, self.prize_amounts):
            money_label = GroupLabel(self.labels, self.font, 16, "${}".format(amount),
                                                    "gray40", {"center": (slot.right - 35, slot.centery)})
                                                    
    def draw(self, surface):
        self.title.draw(surface)
        for slot in self.slots:
            pg.draw.rect(surface, pg.Color("lightblue"), slot, 2)        
        for label in self.labels:
            label.draw(surface)
            
            
class BiggestFish(Prize):
    def __init__(self, prize_amounts):  
        super(BiggestFish, self).__init__("Biggest Fish", prize_amounts)
        
    def get_leaders(self, fisherman, tournament):
        weights = [0] * len(self.prize_amounts)
        leaders = []
        competitors = tournament.competitors + [fisherman]
        for c in competitors:
            for fish_name in c.creel:
                for fish in c.creel[fish_name]:
                    if fish.weight > min(weights):
                        weights.append(fish.weight)
                        weights = sorted(weights, reverse=True)[:-1]
                        leaders.append((c, fish))
                        if len(leaders) > len(self.prize_amounts):
                            leaders = sorted(leaders, key=lambda x: x[1].weight, reverse=True)[:-1]
        
        if leaders:
            leaders = sorted(leaders, key=lambda x: x[1].weight, reverse=True)
        return leaders
        
        
class BiggestTotal(Prize):
    def __init__(self, prize_amounts):
        super(BiggestTotal, self).__init__("Total", prize_amounts)
        
    def get_leaders(self, fisherman, tournament):
        totals = [0] * len(self.prize_amounts)
        competitors = tournament.competitors + [fisherman]
        leaders = []
        for c in competitors:
            total = 0
            for fish_name in c.creel:
                total += sum([x.weight for x in c.creel[fish_name]])
            if total > min(totals):
                totals.append(total)
                totals = sorted(totals, reverse=True)[:-1]
                leaders.append((c, total))                
                if len(leaders) > len(self.prize_amounts):
                    leaders = sorted(leaders, key=lambda x: x[1], reverse=True)[:-1]
        leaders = sorted(leaders, key=lambda x: x[1], reverse=True)
        return leaders
        
        
class BiggestSpecies(Prize):
    def __init__(self, species, prize_amounts):
        self.species = species
        name = "Biggest {}".format(self.species)
        super(BiggestSpecies, self).__init__(name, prize_amounts)
        
    def get_leaders(self, fisherman, tournament):
        weights = [0] * len(self.prize_amounts)
        leaders = []
        competitors = tournament.competitors + [fisherman]
        for c in competitors:
            for fish in c.creel[self.species]:
                if fish.weight > min(weights):
                    weights.append(fish.weight)
                    weights = sorted(weights, reverse=True)[:-1]
                    leaders.append((c, fish))
                    if len(leaders) > len(self.prize_amounts):
                        leaders = sorted(leaders, key=lambda x: x[1].weight, reverse=True)[:-1]
        leaders = sorted(leaders, key=lambda x: x[1].weight, reverse=True)
        return leaders
        
        
class BiggestTotalSpecies(Prize):
    def __init__(self, species, prize_amounts):
        self.species = species
        super(BiggestTotalSpecies, self).__init__("Total {}".format(species), prize_amounts)
        
    def get_leaders(self, fisherman, tournament):
        totals = [0] * len(self.prize_amounts)
        competitors = tournament.competitors + [fisherman]
        leaders = []
        for c in competitors:
            total = sum([x.weight for x in c.creel[self.species]])
            if total > min(totals):
                totals.append(total)
                totals = sorted(totals, reverse=True)[:-1]
                leaders.append((c, total))                
                if len(leaders) > len(self.prize_amounts):
                    leaders = sorted(leaders, key=lambda x: x[1], reverse=True)[:-1]
        leaders = sorted(leaders, key=lambda x: x[1], reverse=True)
        return leaders