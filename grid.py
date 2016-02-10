import copy
import pygame


class Grid:
    def __init__(self, height=64, width=64):
        self.height = height
        self.width = width
        self.grid = _construct_grid(height, width)
        self.block_size = 10

    def draw(self, screen):
        for x, y in _enumerate_coordinates(self.grid):
            self._draw_cell(screen, x, y)

    def _draw_cell(self, screen,  x, y, color=(0, 0, 0)):
        if self.grid[y][x]:
            rect = (x * self.block_size, y * self.block_size, self.block_size, self.block_size)
            pygame.draw.rect(screen, color, rect)

    def update(self):
        new_grid = copy.deepcopy(self.grid)

        for x, y in _enumerate_coordinates(self.grid):
            adjacent_count = sum(self._get_adjacent_cells(x, y))
            if adjacent_count == 3:
                new_grid[y][x] = True
            elif adjacent_count == 2 and self.grid[y][x]:
                new_grid[y][x] = True
            else:
                new_grid[y][x] = False

        self.grid = new_grid

    def _get_adjacent_cells(self, x, y):
        x_increments, y_increments = [0], [0]
        x_increments.append(-1) if x != 0 else None
        x_increments.append(1) if x != (self.height - 1) else None
        y_increments.append(-1) if y != 0 else None
        y_increments.append(1) if y != (self.width - 1) else None

        neighbors = []
        for x_inc in x_increments:
            for y_inc in y_increments:
                if not x_inc and not y_inc:
                    continue
                neighbors.append(self.grid[y + y_inc][x + x_inc])
        return neighbors

    def handle_click(self, mouse_pos):
        cell_x, cell_y = self._get_cell_pos(mouse_pos[0], mouse_pos[1])
        self._toggle_cell(cell_x, cell_y)

    def _get_cell_pos(self, pix_x, pix_y):
        # convert from pixel x/y to cell grid x/y
        return int(pix_x / self.block_size), int(pix_y / self.block_size)

    def _toggle_cell(self, cell_x, cell_y):
        current_val = self.grid[cell_y][cell_x]
        if current_val:
            self.grid[cell_y][cell_x] = False
        else:
            self.grid[cell_y][cell_x] = True


def _construct_grid(height, width):
    return [[False] * width for i in range(height)]


def _enumerate_coordinates(grid):
    for y, row in enumerate(grid):
        for x, v in enumerate(row):
            yield x, y
