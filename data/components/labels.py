import pygame as pg

from .. import prepare

                   
import pygame as pg

LOADED_FONTS = {}
                   
class _Label(object):
    '''Parent class all labels inherit from. Color arguments can use color names
       or an RGB tuple. rect_attributes should be a dict with keys of
       pygame.Rect attribute names (strings) and the relevant position(s) as values.'''
    def __init__(self, font_path, font_size, text, text_color, rect_attributes,
                         bground_color=None):
        if (font_path, font_size) not in LOADED_FONTS:
            LOADED_FONTS[(font_path, font_size)] = pg.font.Font(font_path,
                                                                                             font_size)
        f = LOADED_FONTS[(font_path, font_size)]    
        if bground_color is not None:
            self.text = f.render(text, True, pg.Color(text_color),
                                         pg.Color(bground_color))
        else:
            self.text = f.render(text, True, pg.Color(text_color))
        self.rect = self.text.get_rect(**rect_attributes)

    def draw(self, surface):
        surface.blit(self.text, self.rect)


class Label(_Label):
    '''Creates a surface with text blitted to it (self.text) and an associated
       rectangle (self.rect). Label will have a transparent background if
       bground_color is not passed to __init__.'''
    def __init__(self, font_path, font_size, text, text_color, rect_attributes,
                         bground_color=None):
        super(Label, self).__init__(font_path, font_size, text, text_color,
                                                rect_attributes, bground_color)

       
class GroupLabel(Label):                             
    '''Creates a Label object which is then appended to group.'''
    def __init__(self, group, font_path, font_size, text, text_color,
                         rect_attributes, bground_color=None):
        super(GroupLabel, self).__init__(font_path, font_size, text, text_color,
                                                        rect_attributes, bground_color)
        group.append(self)


class Blinker(Label):
    """A blinking label"""
    def __init__(self, font_path, font_size, text, text_color, rect_attributes,
                         blink_frequency, bground_color=None):
        super(Blinker, self).__init__(font_path, font_size, text, text_color,
                                                  rect_attributes, bground_color)
        self.frequency = blink_frequency
        self.elapsed = 0.0
        self.on = False
        
    def draw(self, surface, dt):
        self.elapsed += dt
        if self.elapsed >= self.frequency:
            self.elapsed -= self.frequency
            self.on = not self.on
        if self.on:    
            surface.blit(self.text, self.rect)

            
class Button(object):
    def __init__(self, left, top, width, height, label):
        self.rect = pg.Rect(left, top, width, height)
        label.rect.center = self.rect.center
        self.label = label
        self.selected = False
        
    def draw(self, surface):
        pg.draw.rect(surface, pg.Color("gray90"), self.rect)
        border = self.rect.inflate(16, 18)
        border.top = self.rect.top - 6
        pg.draw.rect(surface, pg.Color("gray90"), border)
        color = "lightblue" if self.selected else "dodgerblue"
        pg.draw.rect(surface, pg.Color(color), self.rect, 3)
        pg.draw.rect(surface, pg.Color(color), border, 4)
        points = [(self.rect.topleft, border.topleft),
                      (self.rect.topright, border.topright),
                      (self.rect.bottomleft, border.bottomleft),
                      (self.rect.bottomright, border.bottomright)]
        for pair in points:
            pg.draw.line(surface, pg.Color(color), pair[0], pair[1], 2)        
        self.label.draw(surface)
       
       
class PayloadButton(Button):
    def __init__(self, left, top, width, height, label, payload):
        super(PayloadButton, self).__init__(left, top, width, height, label)
        self.payload = payload

        