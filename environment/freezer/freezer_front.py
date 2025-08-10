import pygame as pg


class freezer_viz():
    def __init__(self, capacity: tuple, freezer):
       self.freezer = freezer

       pg.init()
       self.screen = pg.display.set_mode((1600, 900))
       pg.display.set_caption("Freezer Simulation")
       self.clock = pg.time.Clock()


       # === self.GRID CONFIG ===
       self.ROWS, self.COLS = capacity[0], capacity[1]
       self.CELL_SIZE = 90

       # === STATE ===
       self.grid = [[0 for _ in range(self.COLS)] for _ in range(self.ROWS)] # 0 = free, 1 = occupied
       self.temperature = 5.0
       self.cooling_on = True


       

    
    def draw_grid(self):
       for row in range(self.ROWS):
         for col in range(self.COLS):
            x, y = col * self.CELL_SIZE, row * self.CELL_SIZE
            color = (200, 220, 255) if self.grid[row][col] == 0 else (255, 0, 0)
            pg.draw.rect(self.screen, color, (x, y, self.CELL_SIZE, self.CELL_SIZE))
            pg.draw.rect(self.screen, (50,50,50), (x, y, self.CELL_SIZE, self.CELL_SIZE), 1)


    def draw_storage(self, x = 960, y = 170 ):
        pg.draw.rect(self.screen, (100, 150, 190), (950, 150, 500, 200), 10)
        taken_space = []
        for idx, palette in enumerate(self.freezer.palettes_to_take):
           
           if idx > 9:
               print(f"Too many palettes: {idx + 1}")
               break
           if  (x, y) in taken_space:
            #   x += 90 * ((idx) - (idx) // 5 * 5)
              x += 90 

              if idx +1 == 1:
                 y = 0
              if (idx + 1) % 6 == 0:
                 y += 90
                 x = 960
         #   print(f'idx: {idx}, x: {x}, y: {y}')
           palette.viz.draw_palette(self.screen, idx + 1, x, y)
           taken_space.append((palette.viz.palette_x, palette.viz.palette_y))
       
    def draw_status(self):
       font = pg.font.SysFont(None, 30)
       temp_text = font.render(f"Temp: {self.temperature}°C", True, (255, 255, 255))
       state_text = font.render(f"Cooling: {'ON' if self.cooling_on else 'OFF'}", True, (255, 255, 255))
       self.screen.blit(temp_text,(905, 50))
       self.screen.blit(state_text, (905, 80))



    # === TOGGLE CELL ON CLICK ===
    def handle_mouse(self):
      mx, my = pg.mouse.get_pos()
      col, row = mx // self.CELL_SIZE, my // self.CELL_SIZE
      if 0 <= row < self.ROWS and 0 <=  col < self.COLS:
         self.grid[row][col] = 1 - self.grid[row][col]




    # === MAIN LOOP ===
    def Main_loop(self):
     running = True
     inside_start_time = None
     show_info = False
     while running:
       
       self.draw_grid()
       self.draw_storage()
       self.draw_status()
       self.clock.tick(30)
       for palette in self.freezer.palettes_to_take:
          palette.viz.show_info()
       
       pg.display.flip()
          
       dt = self.clock.tick(60) / 1000  # Delta time in seconds
       self.screen.fill((30,30,30))

       for event in pg.event.get():
          if event.type == pg.QUIT:
            running = False

         #  print(f'xd: {len(self.freezer.palettes_to_take)}')
          for palette in self.freezer.palettes_to_take:
            #  print(f"Palette space xd?")
             pos = pg.mouse.get_pos()
             if palette.viz.rect.collidepoint(pos):
                print(f"Mouse over palette space")
                if inside_start_time is None:
                   
                   inside_start_time = pg.time.get_ticks()
                else:
                  
                   elapsed_time = (pg.time.get_ticks() - inside_start_time) / 1000
                   if elapsed_time > 1:
                       print("Mouse inside for 1.5 seconds!")
                       inside_start_time = None # 1 second threshold
                       palette.viz.show = True
             else:
                       palette.viz.show = False    
          
            
          if event.type == pg.KEYDOWN:
            if event.key == pg.K_c:
                self.cooling_on = not self.cooling_on
          
          elif event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1: # Left click
               pos = pg.mouse.get_pos()
               self.handle_mouse()
            elif event.button == 3: # Right click
               print(f"Right Mouse clicked at: {pos}")
    
    # update_self.temperature()
      #  self.draw_grid()
      #  self.draw_storage()
      #  self.draw_status()
      #  for idx, palette in enumerate(self.freezer.palettes_to_take):
      #      palette.run_viz(self.screen, idx + 1)
      #  pg.display.flip()
      #  self.clock.tick(30)

    pg.quit()