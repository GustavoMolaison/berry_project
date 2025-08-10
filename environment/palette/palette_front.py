import numpy as np
import pygame as pg


    
class palette_viz():
    def __init__(self, palette):
    
        self.texture = pg.image.load('environment\palette\img_palette\palette.png')
        self.texture = pg.transform.scale(self.texture, (80, 80))
        self.gap_y = 0
        self.show = False

        self.palette = palette
        self.palette_size = (80, 80)

    def draw_palette(self, screen, spot, x, y):
    
        # if spot == 1:
        #     gap_y = 0
        # if spot % 6 == 0:
        #     gap_y += 90
        # gap_x = 90 * ((spot-1) - (spot-1) // 5 * 5)

        self.palette_x = x
        self.palette_y = y
        self.screen = screen
        
        screen.blit(self.texture, (self.palette_x, self.palette_y))
        self.rect = pg.Rect(self.palette_x, self.palette_y, *self.palette_size)
        
    def show_info(self):
       
        if self.show:
           pg.draw.rect(self.screen, (255, 255, 255), (self.palette_x + 80, self.palette_y, 80, 150))