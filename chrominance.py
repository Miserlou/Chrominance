#! /usr/bin/python2.7
# coding: utf-8

import pygame
import pygame.midi
from pygame.locals import *

def handleEvents():
    for event in pygame.event.get():
        if event.type == QUIT:
           quit()
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
           quit()

pygame.init()
pygame.font.init()
pygame.midi.init()
input_id = pygame.midi.get_default_input_id()
i = pygame.midi.Input( input_id )

#MBAir: 1440x900
#Ubu: 1920x1080
screen = pygame.display.set_mode((1920,1080),pygame.FULLSCREEN)

background = pygame.Surface(screen.get_size())
background = background.convert()
r = 2
g = 2
b = 2
d = 1
clock = pygame.time.Clock()

while 1:

    handleEvents()

    background.fill((r, g, b))
    screen.blit(background, (0, 0))
    pygame.display.flip()

    if r > 249:
        d = d * -1
    if r < 2:
        d = d * -1
    r = r + d
    g = g + d
    b = b + d

    clock.tick(60)
