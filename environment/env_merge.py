import numpy as np
import pygame as pg
from freezer.freezer_back import freezer
from palette.palette_back import blueberry_palette

class magazine():
    def __init__(self):
        pass

    def initialize(self, freezer):
        self.freezer = freezer_env
        # self.palette = blueberry_palette(crates_amount={'thick': 5}, palette_weight=20.0, weight_brutto=50.0, temperature=3.0, freezer = self.freezer)
        # self.palette.run_viz(self.freezer.screen)
        self.freezer.add_palette(blueberry_palette(crates_amount={'thick': 5}, palette_weight=20.0, weight_brutto=50.0, temperature=3.0, freezer = self.freezer))
        self.freezer.add_palette(blueberry_palette(crates_amount={'thick': 5}, palette_weight=20.0, weight_brutto=50.0, temperature=3.0, freezer = self.freezer))
        self.freezer.add_palette(blueberry_palette(crates_amount={'thick': 5}, palette_weight=20.0, weight_brutto=50.0, temperature=3.0, freezer = self.freezer))
        self.freezer.add_palette(blueberry_palette(crates_amount={'thick': 5}, palette_weight=20.0, weight_brutto=50.0, temperature=3.0, freezer = self.freezer))
        # self.freezer.add_palette(blueberry_palette(crates_amount={'thick': 5}, palette_weight=20.0, weight_brutto=50.0, temperature=3.0, freezer = self.freezer))
        # self.freezer.add_palette(blueberry_palette(crates_amount={'thick': 5}, palette_weight=20.0, weight_brutto=50.0, temperature=3.0, freezer = self.freezer))
        
        
        
        
        # print(len(self.freezer.palettes_to_take))
        # quit()
        self.freezer.run_viz()

freezer_env = freezer(capacity=(10, 10))
mag = magazine()
mag.initialize(freezer_env)