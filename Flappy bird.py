'''Scrolling Background'''
import pygame
from pygame.locals import *
import random
from pygame import mixer
pygame.init()
clock = pygame.time.Clock()
fps = 60
width = 540
height = 700
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Moai\'s revenger')

#define font
font = pygame.font.SysFont('Bauhaus 93', 60) #change font size and font here

#define colours
color_txt = (0, 0, 0) #you guys can changencolour here

#define game variables
cloud_scroll = 0
cloud_speed = 0.3
grass_scroll = 0
grass_speed = 3
flying = False
game_over = False
pipe_gap = 180
pipe_frequency = 1500 #milliseconds
last_pipe = pygame.time.get_ticks() - pipe_frequency
score = 0
real_score = 0
pass_pipe = False


bg = pygame.image.load('img/background.png')
bg_cloud = pygame.image.load('img/cloud.png')
bg_sea = pygame.image.load('img/sea.png')
bg_grass = pygame.image.load('img/grass.png')
button_img = pygame.image.load('img/gameover.png')

mixer.init()
mixer.music.load('music/58337f2e15b9d5e6.wav')
mixer.music.set_volume(0.2)
mixer.music.play(10000)

def draw_text(text, font, text_col, x, y):
    '''draw text in game'''
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


def reset_game():
    pipe_group.empty()
    flappy.rect.x = 60
    flappy.rect.y = 275
    score = 0
    return score

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





class Pipe(pygame.sprite.Sprite):
    """creative pipe sprite"""
    def __init__(self, x , y, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/Sao.png')
        self.rect = self.image.get_rect()

        #position 1 is from the top, -1 is from the bottom
        if position == 1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x, y - int(pipe_gap / 2)] #with gap
        if position == -1:
            self.rect.topleft = [x, y + int(pipe_gap / 2)] #with gap
    def update(self):
        self.rect.x -= grass_speed
        if self.rect.right < 0:
            self.kill()

class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self):
        
        action = False

        #get mouse position
        pos = pygame.mouse.get_pos()
        
        #check if mouse is over the button
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                action = True

        #draw button
        screen.blit(self.image, (self.rect.x, self.rect.y))
        return action

moai_group = pygame.sprite.Group()
pipe_group = pygame.sprite.Group()
flappy = Moai(60, 275) #position of moai with x, y

moai_group.add(flappy)

#create restart button instance
button = Button(0, 0, button_img)

run = True
while run:
    clock.tick(fps)

    screen.blit(bg, (0, 0))

    screen.blit(bg_sea, (0, 0))
    
    screen.blit(bg_cloud, (cloud_scroll, 0))
    cloud_scroll -= cloud_speed
    

    moai_group.draw(screen)
    moai_group.update()
    pipe_group.draw(screen)

    #check the score
    if len(pipe_group) > 0:
        if moai_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.left and pass_pipe == False:
            pass_pipe = True
        if pass_pipe == True:
            score += 1/20
            if moai_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.right:
                #score += (1/9)
                pass_pipe = False
    draw_text('Score : '+ str(int(score)), font, color_txt, 40, 20)

    #check moai touch grass and check moai touch pipe
    if flappy.rect.bottom >= 587 or pygame.sprite.groupcollide(moai_group, pipe_group, False, False) or flappy.rect.top < 0:
        game_over = True
    #look for collosion

    if game_over == False and flying == True: #grass stop

        #generate new pipes
        time_now = pygame.time.get_ticks()
        if time_now - last_pipe > pipe_frequency:
            pipe_height = random.randint(-100, -10)
            btm_pipe = Pipe(width, int(height / 2) + pipe_height, -1)
            top_pipe = Pipe(width, int(height / 2) + pipe_height, 1)
            pipe_group.add(btm_pipe)
            pipe_group.add(top_pipe)
            last_pipe = time_now


        grass_scroll -= grass_speed
        if abs(grass_scroll) > 540:
            grass_scroll = 0

        pipe_group.update()

    if abs(cloud_scroll) > 540:
        cloud_scroll = 0
    
    if game_over == True:
        if button.draw() == True:
            game_over = False
            score = reset_game()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and flying == False and game_over == False:
            flying = True

    screen.blit(bg_grass, (grass_scroll, 25))
    pygame.display.update()

pygame.quit()
