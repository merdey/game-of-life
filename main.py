import pygame
import sys
import time

from grid import Grid




pygame.init()
screen = pygame.display.set_mode((640, 640))
pygame.display.set_caption("Game of Life")
fps_clock = pygame.time.Clock()

grid = Grid()
running = False
start_t = time.time()

while True:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            grid.handle_click(pygame.mouse.get_pos())
        elif event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if running:
        grid.update()
    elif time.time() - start_t > 10:
        running = True

    screen.fill((255, 255, 255))
    grid.draw(screen)
    pygame.display.update()

    fps_clock.tick(50)

