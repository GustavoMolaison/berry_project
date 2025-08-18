import numpy as np
import pygame as pg
from .freezer_front import freezer_viz



class freezer():
    def __init__(self, capacity: tuple):
       self.capacity = capacity
       self.viz = freezer_viz(self.capacity, self)
       self.temperature = self.viz.temperature
       self.cooling_on = self.viz.cooling_on
       self.screen = self.viz.screen
       self.grid = self.viz.grid
       self.palettes_to_take = []
       self.palettes_whole = []

    def state(self):
        # Initialize the state of the freezer 
        self.grid = self.viz.grid

    def run_viz(self):
         self.viz.Main_loop()

    def add_palette(self, palette):
        # Add a palette to the freezer
        self.palettes_to_take.append(palette)
        self.palettes_whole.append(palette)
         # Example placeholder for palette
        
        
if __name__ == "__main__":
  freezer_env = freezer(capacity=(10, 10))
  freezer_env.run_viz()