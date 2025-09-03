import numpy as np
from .palette_front import palette_viz
crates_W = {'thick': 1}

class blueberry_palette():
    def __init__(self, crates_amount: dict, palette_weight: float, weight_brutto : float, temperature: float,freezer):
        self.crates_amount = crates_amount
        self.palette_weight = palette_weight
        self.weight_brutto = weight_brutto
        self.temperature = temperature
        self.crates_weight = [crates_W[key] * value for key, value in crates_amount.items()]
        self.netto = self.weight_brutto - self.palette_weight -  np.sum(self.crates_weight)
        self.freezer = freezer
        self.placed = False
        self.viz = palette_viz(self)
        self.grid = None

        self.chosen = False

    def run_viz(self, screen, spot, gap_x=0, gap_y=0):
        self.viz.draw_palette(screen, spot, gap_x=0, gap_y=0)

    def recieve_input(self, event): # event  -> dictionary
        # Handle input events for the palette
        if event['LEFT_C'] == 1:
            print(f'self.chosen before: {self.chosen}')
            print(f'self.freezer.chosen_palette before: {self.freezer.chosen_palette}')
            self.chosen = not self.chosen
            
            if self.freezer.chosen_palette != None:
                   self.freezer.chosen_palette.chosen = False
                   self.freezer.chosen_palette = None
            self.freezer.chosen_palette = self if self.chosen else self.freezer.chosen_palette

            print(f'self.chosen after: {self.chosen}')
            print(f'self.freezer.chosen_palette after: {self.freezer.chosen_palette}')
           
