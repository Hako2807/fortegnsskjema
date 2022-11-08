import pygame
from sys import exit
import math
import numpy
import time

COLOR = (255, 255, 255)

def draw_dashed_line(surf, color, start_pos, end_pos, width=1, dash_length=10):
    x1, y1 = start_pos
    x2, y2 = end_pos
    dl = dash_length
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)

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
        self.w = w
        self.h = h

        self.resolution = (self.w, self.h)
        self.screen = pygame.display.set_mode(self.resolution)
        pygame.display.set_caption(f"res: {w}, {h}")
        self.fps = 60
        self.clock = pygame.time.Clock()
        self.frame = 0

        self.calc = calcs
        self.font = pygame.font.Font("assets/computer_classic.ttf", 20)
        self.min_x = 100
        self.max_x = self.w - self.min_x
        self.numbers = self.calc.factors

        self.function_text = calcs.function_text
        self.fconst = self.calc.factors[0]
        self.factors = sorted(self.calc.factors[1::])
        
    
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.image.save(self.screen, f"assets/{int(time.time() % 10000)}fortegnsskjema.png")
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
        cse = [i for i in self.factors]
        cse.append(self.fconst)
        x_vals = self.calculate_start_end(100, self.max_x, sorted(cse))
        print(x_vals)


   
        self.screen.fill((46, 50, 51))

        self.screen.blit(self.font.render(f"Fortegnsskjema for f(x) = {self.function_text}", True, (22, 160, 230)), (10, 15))

        for i in x_vals:
            self.print_to_screen(i[0], (i[1], 50))
        
        
        self.print_to_screen("x ", (20, 75))
        pygame.draw.line(self.screen, COLOR, (self.min_x - 20, 90), (self.max_x + 20, 90))
        self.print_to_screen("<", (self.min_x - 28, 77))
        self.print_to_screen(">", (self.max_x + 15, 77))

        if self.fconst != 0 or self.fconst != 1:
            self.print_to_screen(str(self.fconst), (20, 140))

        for i in range(1, len(self.factors)):
            if i < len(self.factors) - 1:
                self.show_row(i, self.factors[i + 1], x_vals)
            else:
                self.show_row(i, self.factors[i], x_vals)
        
        pygame.display.flip()

    def calculate_start_end(self, x1, x2, numbers):
        difference = x2 - x1
        dv = numbers[-1] - numbers[0]
        if dv == 0: dv = 1
        space = difference / dv
        print(difference, space, dv)

        l = [[str(i), i * space + x1 + difference/2] for i in numbers]
        return l

    def show_row(self, index, x0, xvals):
        if x0 > 0:
            self.print_to_screen(f"x - {x0}", (20, 140 + index*50))
        elif x0 < 0:
            self.print_to_screen(f"x + {-x0}", (20, 140 + index*50))
        else: 
            self.print_to_screen(f"x", (20, 140 + index*50))
        self.paint_line(index, x0, xvals)
    
    def paint_line(self, index, x0, xvals):
        for i in range(len(xvals)):
            if i < len(xvals) - 1:
                if float(xvals[i][0]) < x0:
                    draw_dashed_line(self.screen, COLOR, (float(xvals[i][1]), 140 + index * 50), (float(xvals[i + 1][1]), 140 + index * 50), dash_length= 5)
                elif float(xvals[i][0]) > x0:
                    pygame.draw.line(self.screen, COLOR, (float(xvals[i][1]), 140 + index * 50), (float(xvals[i + 1][1]), 140 + index * 50))
                else:
                    self.print_to_screen("0", (float(xvals[i][1]), 140 + index * 50 - 10))
                    if float(xvals[i][0]) + 0.1 < x0:
                        draw_dashed_line(self.screen, COLOR, (float(xvals[i][1]) + 15, 140 + index * 50), (float(xvals[i + 1][1]), 140 + index * 50), dash_length= 5)
                    elif float(xvals[i][0]) + 0.1 > x0:
                        pygame.draw.line(self.screen, COLOR, (float(xvals[i][1]) + 15, 140 + index * 50), (float(xvals[i + 1][1]), 140 + index * 50))


            else: 
                if float(xvals[i][0]) < x0:
                    draw_dashed_line(self.screen, COLOR, (float(xvals[i][1]), 140 + index * 50), (self.max_x, 140 + index * 50), dash_length=5)
                elif float(xvals[i][0]) > x0:
                    pygame.draw.line(self.screen, COLOR, (float(xvals[i][1]), 140 + index * 50), (self.max_x, 140 + index * 50))
