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
cloud_speed = 0.3
grass_scroll = 0
grass_speed = 3
flying = False
game_over = False

bg = pygame.image.load('img/background.png')
bg_cloud = pygame.image.load('img/cloud.png')
bg_sea = pygame.image.load('img/sea.png')
bg_grass = pygame.image.load('img/grass.png')

class Moai(pygame.sprite.Sprite):
    def __init__(self, x, y):
        """create moai sprite"""
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        for i in range(-2, 3):
            img = pygame.image.load(f'img/moai{abs(i)}.png')
            self.images.append(img)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.garvity = 0
        self.clicked = False

    def update(self):
        """animation moai sprite"""
        if flying == True:
            #garvity
            self.garvity += 0.5
            if self.garvity > 10: #moai speed falling
                self.garvity = 10
            if self.rect.bottom < 587: #touch grass position
                self.rect.y += int(self.garvity)

        if game_over == False:
            #moai jump
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                self.garvity = -7
            if pygame.mouse.get_pressed()[0] == 1:
                self.clicked = False

            #maoi gif
            self.counter += 1
            speed_animation = 3
            if self.counter > speed_animation:
                self.counter = 0
                self.index += 1
                if self.index >= len(self.images):
                    self.index = 0
            self.image = self.images[self.index]
            
            #rotate the moai
            self.image = pygame.transform.rotate(self.images[self.index], self.garvity * -1)
        else:
            self.image = pygame.transform.rotate(self.images[self.index], -90)

moai_group = pygame.sprite.Group()

flappy = Moai(60, 275)

moai_group.add(flappy)

run = True
while run:
    clock.tick(fps)

    screen.blit(bg, (0, 0))

    screen.blit(bg_sea, (0, 0))
    
    screen.blit(bg_cloud, (cloud_scroll, 0))
    cloud_scroll -= cloud_speed
    
    screen.blit(bg_grass, (grass_scroll, 25))

    moai_group.draw(screen)
    moai_group.update()
    
    #check moai touch grass
    if flappy.rect.bottom > 587:
        game_over = True
        flying = False
    
    if game_over == False: #glass stop
        grass_scroll -= grass_speed
        if abs(grass_scroll) > 540:
            grass_scroll = 0
    if abs(cloud_scroll) > 540:
        cloud_scroll = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and flying == False and game_over == False:
            flying = True

    pygame.display.update()

pygame.quit()
