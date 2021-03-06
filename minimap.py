# Author:Stew
# Date:12/18/2020
# Description: This contains a class called minimap that creates a minimap

import pygame as pg
from stew_work import *
from main import *
from settings import *

minimap_size = 144

class Minimap(pg.sprite.Sprite):

    def __init__(self, game, x, y):
        self.num_blocks = dungeon.depth
        self.groups = game.all_sprites, game.minimap
        pg.sprite.Sprite.__init__(self, self.groups, Dungeon(14))
        self.x_cor = WIDTH - minimap_size
        self.y_cor = 0
        self.rectangle = pg.Rect(self.x_cor, self.y_cor, minimap_size, minimap_size)
        self.found_rooms = [(dungeon.get_start_room()[0], dungeon.get_start_room()[1])]
        self.color = BLUE

    def draw(self, surface):
        pg.draw.rect(surface,self.color,self.rectangle)



