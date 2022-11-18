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

bg = pygame.image.load('img/Sprite-0003.png')
cloud = pygame.image.load('img/Sprite-0004.png')

run = True
while run:
    clock.tick(fps) #slow cloud speed (time)
    screen.blit(bg, (0, 0)) #sky background
    screen.blit(cloud, (ground_scroll, 0)) #cloud background
    ground_scroll -= scroll_speed
    if abs(ground_scroll) > 540: #loop scrolling
        ground_scroll = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
