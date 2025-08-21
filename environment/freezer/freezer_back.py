import numpy as np
import pygame as pg
from .freezer_front import freezer_viz



class freezer():
    def __init__(self, capacity: tuple):
       self.capacity = capacity
       self.viz = freezer_viz(self.capacity, self)
       self.temperature = 5
       self.cooling_on = True
       self.screen = self.viz.screen
       self.ROWS, self.COLS = capacity[0], capacity[1]
       self.grid = np.full((self.ROWS, self.COLS), 100, dtype=int) # 0 = free, 1 = occupied
       self.palettes_to_take = []
       self.palettes_whole = []
       self.chosen_palette = None

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

    def grid_handle(self, square):
      
         if self.chosen_palette != None:
           if self.chosen_palette.chosen:
            print(f"Grid square clicked: {square}")
            self.grid[(square[0], square[1])] = self.palettes_whole.index(self.chosen_palette)

            self.chosen_palette.placed = not self.chosen_palette.placed
            self.chosen_palette.chosen = False
            if self.chosen_palette in self.palettes_to_take:
              self.palettes_to_take.remove(self.chosen_palette)

    def recieve_input(self, event): # event  -> dictionary
        if event['PALETTE'] != 0:
           event['PALETTE'].recieve_input(event)
        
        if event['PALETTE'] == 0 and event['LEFT_C'] == 1:
            
            if event['GRID_SQUARE'] != 0:
               
                self.grid_handle(event['GRID_SQUARE'])
            
        
if __name__ == "__main__":
  freezer_env = freezer(capacity=(10, 10))
  freezer_env.run_viz()