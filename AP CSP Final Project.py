import pygame
import tkinter as tk
from tkinter import messagebox
import random
import math

pygame.init()

winSize = 640

win = pygame.display.set_mode((winSize, winSize))
pygame.display.set_caption("Snake")

run = True

x = 40
y = 40
gridSize = 40

xVel = 0
yVel = 0

white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

bloccList = []
score = 0


class Snacc:
   def __init__(self, color):
       self.color = color
       self.xSnacc = random.randint(1, winSize / gridSize - 2) * gridSize
       self.ySnacc = random.randint(1, winSize / gridSize - 2) * gridSize

   def draw(self):
       pygame.draw.rect(win, self.color, (self.xSnacc, self.ySnacc, gridSize, gridSize))


class Blocc:
   def __init__(self, color):
       self.color = color
       self.xBlocc = random.randint(0, winSize / gridSize - 1) * gridSize
       self.yBlocc = random.randint(0, winSize / gridSize - 1) * gridSize

   def add(self):
       bloccList.append((self.xBlocc, self.yBlocc, gridSize, gridSize))


def drawBlocc(bloccInfo):
   pygame.draw.rect(win, red, (bloccInfo))


def message_box(subject, content):
   root = tk.Tk()
   root.attributes("-topmost", True)
   root.withdraw()
   messagebox.showinfo(subject, content)
   try:
       root.destroy()
   except:
       pass


snacc = Snacc(green)

while run:
   pygame.time.delay(100)
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           run = False
   keys = pygame.key.get_pressed()

   if keys[pygame.K_LEFT]:
       xVel = -gridSize
       yVel = 0
   elif keys[pygame.K_RIGHT]:
       xVel = gridSize
       yVel = 0
   elif keys[pygame.K_UP]:
       yVel = -gridSize
       xVel = 0
   elif keys[pygame.K_DOWN]:
       yVel = gridSize
       xVel = 0

   if x <= 0 or x >= 600 or y <= 0 or y >= 600:
       xVel, yVel = 0, 0
       message_box("You Lost!!!", "Quit and run to try again! Your score was " + str(score))
       run = False

   if x == snacc.xSnacc and y == snacc.ySnacc:
       snacc = Snacc(green)
       score += 1
       blocc = Blocc(red)
       if blocc.xBlocc == snacc.xSnacc and blocc.yBlocc == snacc.ySnacc:
           blocc = Blocc(red)
           blocc.add()
           time = 10
       else:
           blocc.add()
           time = 10
   for coord in bloccList:
       if (x, y, 40, 40) == (coord):
           xVel, yVel = 0, 0
           message_box("You Lost!!!", "Quit and run to try again! Your score was " + str(score))
           run = False

   x += xVel
   y += yVel

   win.fill((0, 0, 0))


   snacc.draw()


   for coord in bloccList:
       drawBlocc(coord)


   pygame.draw.rect(win, white, (x, y, gridSize, gridSize))

   pygame.display.update()

pygame.quit()

