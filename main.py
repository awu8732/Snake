# window goes down - y increase, goes right - x increase
# surfaces:
# rect(surface, color, (x, y, width, height))
# circle(surface, color, position, radius, width = 0)
# ellipse(surface, color, (x, y, width, height))
# line(surface, color, start_pos, end_pos)

# basic colors:
# black = (0,0,0)   white = (255,255,255)
# blue = (0,0,255)  green = (0,255,0)
# red = (255,0,0)   purple = (153,50,204)
# orange=(255,97,3) yellow = (255,255,0)

red = (255,0,0)
best_score = [1]

import pygame
import random
from classes import Cube
from classes import Snake
import tkinter as tk
from tkinter import messagebox

pygame.init()

def drawGrid(w, rows, surface):
    sizeBtwn = w // rows

    x = 0
    y = 0
    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn

        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, w))
        pygame.draw.line(surface, (255, 255, 255), (0, y), (w, y))

def redrawWindow(surface):
    global rows, width, snake, snack, best_score
    surface.fill((0, 0, 0))
    snake.draw(surface)
    snack.draw(surface)
    drawGrid(width, rows, surface)

    score = pygame.font.SysFont('comicsancs', 20, True, False)
    text = score.render('Score: ' + str(len(snake.body)), 1, (255, 0, 0))
    surface.blit(text, (400, 0))
    text_bscore = pygame.font.SysFont('comicsancs', 20, True)
    text2 = text_bscore.render('Best Score: ' + str(best_score[0]), 1, (255, 0, 0))
    surface.blit(text2, (275,0))

    pygame.display.update()


def randomSnack(rows, item):
    positions = item.body

    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        if len(list(filter(lambda z: z.pos == (x, y), positions))) > 0:
            continue
        else:
            break

    return (x, y)

def message_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass

def main():
    global width, rows, snake, snack
    width = 500
    rows = 20
    win = pygame.display.set_mode((width, width))
    snake = Snake((255, 0, 0), (10, 10))
    snack = Cube(randomSnack(rows, snake), color=(0, 255, 0))
    flag = True


    clock = pygame.time.Clock()

    while flag:
        pygame.time.delay(25)
        clock.tick(12)
        snake.move()
        if snake.body[0].pos == snack.pos:
            snake.addCube()
            snack = Cube(randomSnack(rows, snake), color=(0, 255, 0))

        for x in range(len(snake.body)):
            if snake.body[x].pos in list(map(lambda z: z.pos, snake.body[x + 1:])):
                print('Score: ', len(snake.body))
                if len(snake.body) > best_score[0]:
                    best_score.pop(0)
                    best_score.append(len(snake.body))
                message_box('You Lost!', 'Play again...')
                snake.reset((10, 10))
                break

        redrawWindow(win)



    pass


main()

