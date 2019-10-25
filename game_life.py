import random
import pygame
from pygame.locals import *

class GameOfLife:
    def __init__(self, width=640, height=480, cell_size=10, speed=10):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        # Устанавливаем размер окна
        self.screen_size = width, height
        # Создание нового окна
        self.screen = pygame.display.set_mode(self.screen_size)
        # Вычисляем количество ячеек по вертикали и горизонтали
        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size
        # Скорость протекания игры
        self.speed = speed

    def draw_grid(self):
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'), (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'), (0, y), (self.width, y))

    def run(self):
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Game of Life')
        self.screen.fill(pygame.Color('white'))
        s1 = self.cell_list()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
            self.draw_grid()
            self.draw_cell_list(s1)
            self.draw_grid()
            pygame.display.flip()
            s1 = self.update_cell_list(s1)
            clock.tick(self.speed)
        pygame.quit()

    def cell_list(self, randomize=True):
        if randomize:
            s = [[random.randint(0, 1) for i in range(self.cell_height)] for j in range(self.cell_width)]
        else:
            s = [[0 for i in range(self.cell_height)] for j in range(self.cell_width)]
            print('Введите колическтво клеток: ', end='')
            n = int(input())
            print("Введите координаты (x, y): ", end='')
            for k in range(n):
                x = int(input())
                y = int(input())
                s[y][x] = 1
        return s

    def draw_cell_list(self, rects):
        for i in range(self.cell_width):
            for j in range(self.cell_height):
                if rects[i][j] == 1:
                    pygame.draw.rect(self.screen, pygame.Color('purple'), (i*self.cell_size, j*self.cell_size, self.cell_size, self.cell_size))
                else:
                    pygame.draw.rect(self.screen, pygame.Color('white'), (i*self.cell_size, j*self.cell_size, self.cell_size, self.cell_size))

    def get_neighbours(self, cell):
        neig = list()
        if cell[0] != 0:
            neig += [[cell[0] - 1, cell[1]]]
        if cell[0] != 0 and cell[1] != 0:
            neig += [[cell[0] - 1, cell[1] - 1]]
        if cell[0] != 0 and cell[1] != self.cell_height - 1:
            neig += [[cell[0] - 1, cell[1] - 1]]
        if cell[0] != self.cell_width - 1:
            neig += [[cell[0] + 1, cell[1]]]
        if cell[0] != self.cell_width - 1 and cell[1] != 0:
            neig += [[cell[0] + 1, cell[1] - 1]]
        if cell[0] != self.cell_width - 1 and cell[1] != self.cell_height - 1:
            neig += [[cell[0] + 1, cell[1] + 1]]
        if cell[1] != self.cell_height - 1:
            neig += [[cell[0], cell[1] + 1]]
        if cell[1] != 0:
            neig += [[cell[0], cell[1] - 1]]
        return neig

    def update_cell_list(self, cell_list):
        s1 = [[0 for i in range(self.cell_height)] for j in range(self.cell_width)]
        for i in range(self.cell_width):
            for j in range(self.cell_height):
                sp = self.get_neighbours([i, j])
                num = 0
                for ii in sp:
                    # print(ii)
                    if cell_list[ii[0]][ii[1]] == 1:
                        num += 1
                if cell_list[i][j] == 1:
                    if num == 2 or num == 3:
                        s1[i][j] = 1
                else:
                    if num == 3:
                        s1[i][j] = 1
        return s1


if __name__ == '__main__':
    game = GameOfLife(600, 600, 30, 15)

    game.run()
