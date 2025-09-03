import pygame as pg
import numpy as np

class freezer_viz():
    def __init__(self, capacity: tuple, freezer):
       self.freezer = freezer

       pg.init()
       self.screen = pg.display.set_mode((1600, 900))
       pg.display.set_caption("Freezer Simulation")
       self.clock = pg.time.Clock()

       self.CELL_SIZE = 90
       
       
       
       

      # === TEXTURES ===
       self.pallete_texture = pg.image.load('environment\palette\img_palette\palette.png')
       self.pallete_texture = pg.transform.scale(self.pallete_texture, (self.CELL_SIZE -3, self.CELL_SIZE -3))


       

    
    def draw_grid(self):
       color = (200, 220, 255)
       for row in range(self.freezer.ROWS):
         for col in range(self.freezer.COLS):
            x, y = row * self.CELL_SIZE, col * self.CELL_SIZE
            

            if self.freezer.grid[row][col] == 100:
               pg.draw.rect(self.screen, color, (x, y, self.CELL_SIZE, self.CELL_SIZE))
               pg.draw.rect(self.screen, (30, 30, 30), (x, y, self.CELL_SIZE, self.CELL_SIZE), 1)
            else: 
               # print(' before x, y', x, y)
               self.freezer.palettes_whole[self.freezer.grid[row][col]].viz.draw_palette(self.screen, x, y)


    def draw_storage(self, x = 960, y = 170, p_idx =None):
        pg.draw.rect(self.screen, (100, 150, 190), (950, 150, 500, 200), 10)
        taken_space = []
        for idx, palette in enumerate(self.freezer.palettes_to_take):
        
           
           if idx > 9:
               print(f"Too many palettes: {idx + 1}")
               break
           if  (x, y) in taken_space:
           
              x += 90 

              if idx +1 == 1:
                 y = 0
              if (idx + 1) % 6 == 0:
                 y += 90
                 x = 960
         #   print(f'idx: {idx}, x: {x}, y: {y}')
           palette.viz.draw_palette(self.screen, x, y)
           taken_space.append((palette.viz.palette_x, palette.viz.palette_y))
       
    def draw_status(self):
       font = pg.font.SysFont(None, 30)
       temp_text = font.render(f"Temp: {self.freezer.temperature}°C", True, (255, 255, 255))
       state_text = font.render(f"Cooling: {'ON' if self.freezer.cooling_on else 'OFF'}", True, (255, 255, 255))
       self.screen.blit(temp_text,(905, 50))
       self.screen.blit(state_text, (905, 80))





    # === MAIN LOOP ===
    def Main_loop(self):
     running = True
     inside_start_time = None
     show_info = False
     last_pallette_idx = None
     self.picked_palette = None
     action_log = {'PALETTE': 0, 'GRID_SQUARE': 0, 'LEFT_C' : 0, 'HOLD' : 0}
     while running:
       self.screen.fill((30, 30, 30))
       self.draw_grid()
       self.draw_storage()
       self.draw_status()
       self.clock.tick(30)
      
      #  pg.display.flip()
       action_log = {'PALETTE': 0, 'GRID_SQUARE': 0, 'LEFT_C' : 0, 'HOLD' : action_log['HOLD']}
       for event in pg.event.get():
         # action_log = {'PALETTE': 0, 'GRID_SQUARE': 0, 'LEFT_C' : 0, 'HOLD' : 0}
         if event.type == pg.MOUSEBUTTONDOWN:
              action_log['LEFT_C'] = 1
              pos = pg.mouse.get_pos()


              for palette in self.freezer.palettes_whole:
                  if palette.viz.rect.collidepoint(pos):
                     action_log['PALETTE'] = palette
                    

                  square = pos[0] // self.CELL_SIZE, pos[1] // self.CELL_SIZE
                  if square in np.ndindex(self.freezer.grid.shape):
                    action_log['GRID_SQUARE'] = square
         
         pos = pg.mouse.get_pos()
         hovering_palette = None
         for palette in self.freezer.palettes_whole:
            if palette.viz.rect.collidepoint(pos):
              hovering_palette = palette
              break

         if hovering_palette:
             if inside_start_time is None:
                 inside_start_time = pg.time.get_ticks()
             else:
                 elapsed_time = (pg.time.get_ticks() - inside_start_time) / 1000
                 if elapsed_time > 0.5:
                   action_log['HOLD'] = 1
                   action_log['PALETTE'] = hovering_palette
         else:
            inside_start_time = None
            action_log['HOLD'] = 0

            
         # for palette in self.freezer.palettes_whole:
            
         #       pos = pg.mouse.get_pos()
         #       if palette.viz.rect.collidepoint(pos):
               
         #        if inside_start_time is None:
                   
         #           inside_start_time = pg.time.get_ticks()
         #        else:
                  
         #           elapsed_time = (pg.time.get_ticks() - inside_start_time) / 1000
         #           if elapsed_time > 0.5:
         #               print('Mouse inside for 0.5 seconds!')
         #               inside_start_time = None # 1 second threshold
         #               action_log['HOLD'] = 1
         #               action_log['PALETTE'] = palette

         # pos = pg.mouse.get_pos()
         # if not any(palette.viz.rect.collidepoint(pos) for palette in self.freezer.palettes_whole):
         #                #  print('xdd')
         #                 action_log['HOLD'] = 0
                  


             
                  
                  
         print(action_log['HOLD'])

         self.freezer.recieve_input(action_log)

              
         if event.type == pg.QUIT:
                   running = False
         
         pg.display.flip()











      #  for palette in self.freezer.palettes_whole:
      #     palette.viz.show_info()
       
      #  pg.display.flip()
          
      #  dt = self.clock.tick(60) / 1000  # Delta time in seconds
      #  self.screen.fill((30,30,30))

      #  for event in pg.event.get():
      #     if event.type == pg.QUIT:
      #       running = False

      #    #  print(f'xd: {len(self.freezer.palettes_to_take)}')
      #     for palette in self.freezer.palettes_whole:
      #       #  print(f"Palette space xd?")
      #        pos = pg.mouse.get_pos()
      #        if palette.viz.rect.collidepoint(pos):
      #          #  print(f"Mouse over palette space")
      #           if inside_start_time is None:
                   
      #              inside_start_time = pg.time.get_ticks()
      #           else:
                  
      #              elapsed_time = (pg.time.get_ticks() - inside_start_time) / 1000
      #              if elapsed_time > 0.5:
      #                #   print("Mouse inside for 1.5 seconds!")
      #                  inside_start_time = None # 1 second threshold
      #                  palette.viz.show = True
      #        else:
      #                  palette.viz.show = False    
          
            
      #     if event.type == pg.KEYDOWN:
      #       if event.key == pg.K_c:
      #           self.cooling_on = not self.cooling_on
          
      #     elif event.type == pg.MOUSEBUTTONDOWN:
      #       if event.button == 1: # Left click
      #          pos = pg.mouse.get_pos()
      #          self.grid_handle(self.picked_palette)
               
      #          for idx, palette in enumerate(self.freezer.palettes_to_take):
      #            pos = pg.mouse.get_pos()
      #            if palette.viz.rect.collidepoint(pos):
                    
      #             #   print('ok')
      #               palette.chosen = not palette.chosen
      #               last_pallette_idx = idx

                    
      #            self.picked_palette = None
      #            for palette in self.freezer.palettes_to_take:
      #                if palette.chosen:
      #                   self.picked_palette = palette

                    
               # for palette in self.freezer.palettes_to_take:
               #    print(palette.chosen)
                   
                  
            # elif event.button == 3: # Right click
               # print(f"Right Mouse clicked at: {pos}")
    
    # update_self.temperature()
      #  self.draw_grid()
      #  self.draw_storage()
      #  self.draw_status()
      #  for idx, palette in enumerate(self.freezer.palettes_to_take):
      #      palette.run_viz(self.screen, idx + 1)
      #  pg.display.flip()
      #  self.clock.tick(30)

    pg.quit()