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
cloud_scroll = 0
cloud_speed = 1
grass_scroll = 0
grass_speed = 3

bg = pygame.image.load('img/background.png')
bg_cloud = pygame.image.load('img/cloud.png')
bg_sea = pygame.image.load('img/sea.png')
bg_grass = pygame.image.load('img/grass.png')

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
    
    screen.blit(bg_sea, (0, 0))

    #pip_group.draw(screen)
    #pipe_group.update()
    screen.blit(bg_cloud, (cloud_scroll, 0))
    cloud_scroll -= cloud_speed
    
    screen.blit(bg_grass, (grass_scroll, 25))
    grass_scroll -= grass_speed


    if abs(cloud_scroll) > 540:
        cloud_scroll = 0
    if abs(grass_scroll) > 540:
        grass_scroll = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
