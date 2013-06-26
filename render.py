# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *

from sys import exit

import time

cols = [38, 70, 102, 134, 166, 199, 231, 263, 295, 328, 360, 392, 424, 456, 489, 521, 553, 585, 618, 650, 682]
rows = [37, 69, 101, 134, 166, 198, 230, 263, 295, 327, 359, 391, 424, 456, 488, 520, 553, 585, 617, 649, 682]

class Window():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((960, 720), 0, 32)
        pygame.display.set_caption("五子棋 by Alvaro")
        self.background = pygame.image.load("source/background.png").convert()
        self.board = pygame.image.load("source/board.png").convert()
        self.next_font = pygame.image.load("source/next.png").convert_alpha()
        self.mark_list = []
        self.control = Control()
        self.run()
        
    def run(self):
        next = pygame.image.load("source/mark_black.png").convert_alpha()
        self.screen.blit(self.background, (0,0))
        self.screen.blit(self.board, (720,0))
        self.screen.blit(self.next_font, (820,40))
        self.screen.blit(next, (785,43))
        pygame.display.update()
        while True:
            event = pygame.event.wait()
            if event.type == QUIT:
                exit()
            if event.type == MOUSEBUTTONDOWN:
                posx, posy = pygame.mouse.get_pos()
                temp = self.place(posx, posy)
                if temp == False or self.control.matrix[temp[0]][temp[1]][0] != 0:
                    continue
                
                if len(self.mark_list)%2 == 0:
                    mark_image = 'source/mark_black.png'
                    mark_next = 'source/mark_white.png'
                    player = 1
                else:
                    mark_image = 'source/mark_white.png'
                    mark_next = 'source/mark_black.png'
                    player = -1

                self.mark_list.append((pygame.image.load(mark_image).convert_alpha(), (cols[temp[0]] - 13, rows[temp[1]] - 13)))
                next = pygame.image.load(mark_next).convert_alpha()
                self.screen.blit(next, (785,43))
                self.screen.blit(self.mark_list[-1][0], self.mark_list[-1][1])
                pygame.display.update()
                if self.control.addOne(temp[0], temp[1], player, len(self.mark_list)) == True:
                    break
        self.screen.blit(self.board, (720,0))
        if player == 1:
            victory = pygame.image.load("source/victory_black.png").convert_alpha()
        elif player == -1:
            victory = pygame.image.load("source/victory_white.png").convert_alpha()
        self.screen.blit(victory, (790,100))
        pygame.display.update()
        while True:
            event = pygame.event.wait()
            if event.type == QUIT:
                exit()
            else:
                time.sleep(0.1)
                continue
            
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
        self.matrix = [[(0, -1) for i in range(21)] for j in range(21)]
        
    def addOne(self, x, y, player, step):
        self.matrix[x][y] = (player, step)
        return self.checkVictory(x, y)
        
    def checkVictory(self, x, y):
        player = self.matrix[x][y][0]
        check = [0 for t in range(9)]
        for j in range(y-1, y+2):
            for i in range(x-1, x+2):
                if i > 20 or i < 0 or j > 20 or j < 0:
                    continue
                dir = (j-y+1)*3+(i-x+1)
                if i == x and j == y:
                    continue
                if self.matrix[i][j][0] == player:
                    check[dir] += 1
                    if self.checkDirection(i, j, dir, check) == True:
                        print 'player'+str(player)+'win'
                        return True
            
        return False

    def checkDirection(self, x, y, dir, check):
        dir_next = (x - 1 + dir%3, y - 1 + dir/3)
        if check[dir] + check[8 - dir] == 4:
            return True
        elif dir_next[0] > 20 or dir_next[0] < 0 or dir_next[1] > 20 or dir_next[1] < 0:
            return False
        elif self.matrix[dir_next[0]][dir_next[1]][0] == self.matrix[x][y][0]:
            check[dir] += 1
            return self.checkDirection(dir_next[0], dir_next[1], dir, check)
        else:
            return False
if __name__ == '__main__':
    ss = Window()