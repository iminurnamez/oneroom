import os
from collections import OrderedDict
import pygame as pg
from . import tools



ORIGINAL_CAPTION = "One Room Shack"
DEBUG = False

pg.mixer.pre_init(44100, -16, 1, 512)
pg.init()


SCREEN_SIZE = (1920, 1080)
os.environ['SDL_VIDEO_CENTERED'] = "TRUE"
pg.mouse.set_visible(False)
pg.display.set_caption(ORIGINAL_CAPTION)

SCREEN = pg.display.set_mode(SCREEN_SIZE, pg.FULLSCREEN)
SCREEN_RECT = SCREEN.get_rect()

    
#Resource loading (Fonts and music just contain path names).
FONTS = tools.load_all_fonts(os.path.join("resources", "fonts"))
MUSIC = tools.load_all_music(os.path.join("resources", "music"))
SFX   = tools.load_all_sfx(os.path.join("resources", "sound"))
GFX   = tools.load_all_gfx(os.path.join("resources", "graphics"))
