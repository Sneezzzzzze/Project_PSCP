'''Scrolling Background'''
import pygame
from pygame.locals import *
pygame.init()
    #Part 1 Background
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
ground_img = pygame.image.load('img/Sprite-0004.png')

#class Pipe(pygame.Sprite):
    #def __init__(self, x, y):
        #pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.image.load('img/pipe.png')
        #self.rect = self.image.get_rect()
        #self.rect.topleft = [x, y]
#btm_pipe = Pipe(300, int(screen_height / 2))

run = True
while run:
    clock.tick(fps)

    screen.blit(bg, (0, 0))

    #pip_group.draw(screen)
    #pipe_group.update()
    screen.blit(ground_img, (ground_scroll, 0))
    ground_scroll -= scroll_speed

    if abs(ground_scroll) > 540:
        ground_scroll = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()

#------------------------------------------------------------------

    #Part 2 Sprite Animation
