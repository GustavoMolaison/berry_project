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

        self.viz = palette_viz(self)

        self.chosen = False

    def run_viz(self, screen, spot, gap_x=0, gap_y=0):
        self.viz.draw_palette(screen, spot, gap_x=0, gap_y=0)
