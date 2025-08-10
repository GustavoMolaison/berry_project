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
  

    def draw_palette(self, screen, spot, x, y, c_idx):
    
        # if spot == 1:
        #     gap_y = 0
        # if spot % 6 == 0:
        #     gap_y += 90
        # gap_x = 90 * ((spot-1) - (spot-1) // 5 * 5)
        if not c_idx == None:
           if self.palette.chosen:
            for pallete in self.palette.freezer.palettes_to_take:
               if pallete.chosen and self.palette.freezer.palettes_to_take.index(pallete) != c_idx:
                    pallete.chosen = False
            
            
        if self.palette.chosen:
            # self.palette.chosen = False
            # for pallete in self.palette.freezer.palettes_to_take:
              
            #   if pallete.chosen:
            #      pallete.chosen = False
            # self.palette.chosen = True
        
            self.texture = pg.image.load('environment\palette\img_palette\palette_chosen.png')
            self.texture = pg.transform.scale(self.texture, (80, 80))
        else:
            self.texture = pg.image.load('environment\palette\img_palette\palette.png')
            self.texture = pg.transform.scale(self.texture, (80, 80))

        self.palette_x = x
        self.palette_y = y
        self.screen = screen
        
        screen.blit(self.texture, (self.palette_x, self.palette_y))
        self.rect = pg.Rect(self.palette_x, self.palette_y, *self.palette_size)
        
    def show_info(self):
        
        rect = pg.Rect(self.palette_x + 80, self.palette_y, 150, 150)
        font = pg.font.SysFont(None, 20)
        
        Brutto_surface = font.render(f"Brutto: {self.palette.weight_brutto} kg", True, (0, 0, 0))
        Palette_surface = font.render(f"Palette: {self.palette.palette_weight} kg", True, (0, 0, 0))
        temperature_surface = font.render(f"Temperature: {self.palette.temperature} C", True, (0, 0, 0))
        crates_string = ",".join(str(w) for w in self.palette.crates_weight)
        crates_weight_surface = font.render(f"Creates: {crates_string} kg", True, (0, 0, 0))
        netto_surface = font.render(f"Creates: {self.palette.netto} kg", True, (0, 0, 0))
        text_rect = (rect.x + 5, rect.y + 5)
       
        if self.show:
           pg.draw.rect(self.screen, (255, 255, 255), (self.palette_x + 80, self.palette_y, 150, 150))
           pg.draw.rect(self.screen, (100, 255, 255), rect, 3)
           self.screen.blit(Brutto_surface, (rect.x + 5, rect.y + 5))
           self.screen.blit(Palette_surface, (rect.x + 5, rect.y + 25))
           self.screen.blit(temperature_surface, (rect.x + 5, rect.y + 45))
           self.screen.blit(crates_weight_surface, (rect.x + 5, rect.y + 65))
           self.screen.blit(netto_surface, (rect.x + 5, rect.y + 85))