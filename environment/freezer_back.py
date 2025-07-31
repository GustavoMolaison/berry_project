import numpy as np
from freezer_front import freezer_viz

crates_W = {'thick': 1}

class freezer():
    def __init__(self, capacity: tuple):
       self.capacity = capacity
       self.viz = freezer_viz(self.capacity)
       self.temperature = freezer_viz.temperature
       self.cooling_on = freezer_viz.cooling_on

    def state(self):
        # Initialize the state of the freezer
        self.grid = self.viz.grid

    def run_viz(self):
         self.viz.Main_loop()
        

class blueberry_palette():
    def __init__(self, crates_amount: dict, palette_weight: float, weight_brutto : float, temperature: float):
        self.creates_amount = crates_amount
        self.crates_weight = crates_weight
        self.palette_weight = palette_weight
        self.weight_brutto = weight_brutto
        self.temperature = temperature
        crates_weight = [crates_W[key] * value for key, value in crates_amount]
        self.netto = self.weight_brutto - self.palette_weight -  np.sum(crates_weight)
        
freezer_env = freezer(capacity=(10, 10))
freezer_env.run_viz()