import pygame as pg


class freezer_viz():
    def __init__(self, capacity: tuple):

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
     while running:
       self.screen.fill((30,30,30))

       for event in pg.event.get():
          if event.type == pg.QUIT:
            running = False

          elif event.type == pg.KEYDOWN:
            if event.key == pg.K_c:
                self.cooling_on = not self.cooling_on

    
    # update_self.temperature()
       self.draw_grid()
       self.draw_status()
       pg.display.flip()
       self.clock.tick(30)

    pg.quit()