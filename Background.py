'''Scrolling Background'''
import pygame
from pygame.locals import *
pygame.init()

clock = pygame.time.Clock()
fps = 60
width = 540
height = 700
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Moai\'s revenger')

#define game variables
ground_scroll = 0
scroll_speed = 4

#load img
<<<<<<< HEAD
bg = pygame.image.load('img/Sprite-0003')#Not work yet until we got all files.
ground_img = pygame.image.load('img/nothing.png')#this one too.
=======
bg = pygame.image.load('img/Sprite-0003.png')
ground_img = pygame.image.load('img/Sprite-0004.png')
>>>>>>> 2d4dea3ce4a34b1a5103abbe1dd126ae889d8f4e
