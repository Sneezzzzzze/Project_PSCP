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
bg = pygame.image.load('img/Sprite-0003.png')#Not work yet until we got all files.
ground_img = pygame.image.load('img/Sprite-0004.png')#this one too.
