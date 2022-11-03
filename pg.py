import pygame
from sys import exit

class Display:
    def __init__(self, w, h):
        
        pygame.init()
        self.resolution = (w, h)
        self.screen = pygame.display.set_mode(self.resolution)
        pygame.display.set_caption(f"res: {w}, {h}")
        self.fps = 60
        self.clock = pygame.time.Clock()
        self.frame = 0
    
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
        
    
    def update_screen(self):
        self.screen.fill((40, 200 , self.frame % 255))
        pygame.display.flip()