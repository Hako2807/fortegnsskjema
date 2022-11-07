import pygame
from sys import exit

COLOR = (255, 255, 255)

def draw_dashed_line(surf, color, start_pos, end_pos, width=1, dash_length=10):
    x1, y1 = start_pos
    x2, y2 = end_pos
    dl = dash_length

    if (x1 == x2):
        ycoords = [y for y in range(y1, y2, dl if y1 < y2 else -dl)]
        xcoords = [x1] * len(ycoords)
    elif (y1 == y2):
        xcoords = [x for x in range(x1, x2, dl if x1 < x2 else -dl)]
        ycoords = [y1] * len(xcoords)
    else:
        a = abs(x2 - x1)
        b = abs(y2 - y1)
        c = round(math.sqrt(a**2 + b**2))
        dx = dl * a / c
        dy = dl * b / c

        xcoords = [x for x in numpy.arange(x1, x2, dx if x1 < x2 else -dx)]
        ycoords = [y for y in numpy.arange(y1, y2, dy if y1 < y2 else -dy)]

    next_coords = list(zip(xcoords[1::2], ycoords[1::2]))
    last_coords = list(zip(xcoords[0::2], ycoords[0::2]))
    for (x1, y1), (x2, y2) in zip(next_coords, last_coords):
        start = (round(x1), round(y1))
        end = (round(x2), round(y2))
        pygame.draw.line(surf, color, start, end, width)


class Display:
    def __init__(self, w, h, calcs):
        
        pygame.init()
        self.resolution = (w, h)
        self.screen = pygame.display.set_mode(self.resolution)
        pygame.display.set_caption(f"res: {w}, {h}")
        self.fps = 60
        self.clock = pygame.time.Clock()
        self.frame = 0
        self.font = pygame.font.Font("assets/computer_classic.ttf", 20)
        self.function_text = calcs.function_text
    
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
    

    def tick(self):
        self.check_events()

        self.update_screen()
        self.frame += 1
        self.clock.tick(self.fps)
        
    
    def print_to_screen(self, text, pos):
        font_surf = self.font.render(text, True, COLOR)
        self.screen.blit(font_surf, pos)

    def update_screen(self):

   
        self.screen.fill((46, 50, 51))

       
        self.print_to_screen(f"f(x) = {self.function_text}", (10, 15))
        self.print_to_screen("x: " + 3 * " " + "-5" + 10 * " " + "0" + 10 * " " + "5", (10, 55))
        self.print_to_screen("x ", (10, 75))
        self.print_to_screen(10*"-" + "0" + 10 * "—", (15, 75))
        pygame.draw.line(self.screen, COLOR, (15, 95), (215, 95))
        draw_dashed_line(self.screen, COLOR, (220, 95), (420, 95), dash_length= 5)
        


        pygame.display.flip()

