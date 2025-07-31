import numpy as np
import pygame as pg
from freezer.freezer_back import freezer
from palette.palette_back import blueberry_palette

class magazine():
    def __init__(self):
        pass

    def initialize(self):
        self.freezer = freezer(capacity=(10, 10))
        self.palette = blueberry_palette(crates_amount={'thick': 5}, palette_weight=20.0, weight_brutto=50.0, temperature=3.0)
        # self.palette.run_viz(self.freezer.screen)
        self.freezer.add_palette(blueberry_palette(crates_amount={'thick': 5}, palette_weight=20.0, weight_brutto=50.0, temperature=3.0))
        self.freezer.add_palette(blueberry_palette(crates_amount={'thick': 5}, palette_weight=20.0, weight_brutto=50.0, temperature=3.0))
        self.freezer.add_palette(blueberry_palette(crates_amount={'thick': 5}, palette_weight=20.0, weight_brutto=50.0, temperature=3.0))
        self.freezer.add_palette(blueberry_palette(crates_amount={'thick': 5}, palette_weight=20.0, weight_brutto=50.0, temperature=3.0))
        self.freezer.add_palette(blueberry_palette(crates_amount={'thick': 5}, palette_weight=20.0, weight_brutto=50.0, temperature=3.0))
        self.freezer.add_palette(blueberry_palette(crates_amount={'thick': 5}, palette_weight=20.0, weight_brutto=50.0, temperature=3.0))
        self.freezer.add_palette(blueberry_palette(crates_amount={'thick': 5}, palette_weight=20.0, weight_brutto=50.0, temperature=3.0))
        self.freezer.add_palette(blueberry_palette(crates_amount={'thick': 5}, palette_weight=20.0, weight_brutto=50.0, temperature=3.0))
        self.freezer.add_palette(blueberry_palette(crates_amount={'thick': 5}, palette_weight=20.0, weight_brutto=50.0, temperature=3.0))
        self.freezer.add_palette(blueberry_palette(crates_amount={'thick': 5}, palette_weight=20.0, weight_brutto=50.0, temperature=3.0))
        
        
        
        # print(len(self.freezer.palettes_to_take))
        # quit()
        self.freezer.run_viz()


mag = magazine()
mag.initialize()