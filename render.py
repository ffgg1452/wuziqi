# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *

from sys import exit

cols = [38, 70, 102, 134, 166, 199, 231, 263, 295, 328, 360, 392, 424, 456, 489, 521, 553, 585, 618, 650, 682]
rows = [37, 69, 101, 134, 166, 198, 230, 263, 295, 327, 359, 391, 424, 456, 488, 520, 553, 585, 617, 649, 682]

class Window():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((720, 720), 0, 32)
        pygame.display.set_caption("五子棋")
        self.background = pygame.image.load("source/background.png").convert()
        self.mark_list = []
        self.control = Control()
        self.run()
        
    def run(self):
        self.screen.blit(self.background, (0,0))
        pygame.display.update()
        while True:
            event = pygame.event.wait()
            if event.type == QUIT:
                exit()
            if event.type == MOUSEBUTTONDOWN:
                posx, posy = pygame.mouse.get_pos()
                temp = self.place(posx, posy)
                if temp == False:
                    continue
                
                if len(self.mark_list)%2 == 0:
                    mark_image = 'source/mark_black.png'
                    player = 1
                else:
                    mark_image = 'source/mark_white.png'
                    player = -1

                self.mark_list.append((pygame.image.load(mark_image).convert_alpha(), (cols[temp[0]] - 13, rows[temp[1]] - 13)))
                
                self.screen.blit(self.mark_list[-1][0], self.mark_list[-1][1])
                pygame.display.update()
                if self.control.addOne(temp[0], temp[1], player) != True:
                    break
 
            
    def place(self, x, y):
        col = -1
        row = -1
        for i in range(len(cols)):
            if x >= cols[i] - 10 and x <= cols[i] + 10:
                col = i
        for j in range(len(rows)):
            if y >= rows[j] - 10 and y <= rows[j] + 10:
                row = j
        if col >= 0 and row >= 0:
            return (col, row)
        else:
            return False
class Control():
    def __init__(self):
        self.matrix = [[0 for i in range(21)] for j in range(21)]
        
    def addOne(self, x, y, player):
        self.matrix[x][y] = player
        return not self.checkVictory(x, y)
        
    def checkVictory(self, x, y):
        return False

if __name__ == '__main__':
    ss = Window()