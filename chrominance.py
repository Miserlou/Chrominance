#! /usr/bin/python2.7
# Coding: utf-8

import pygame
import pygame.midi
from pygame.locals import *

def handleEvents():
    for event in pygame.event.get():
        if event.type == QUIT:
           quit()
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
           quit()

def handleMIDIEvents(i, screen):
    if i.poll():
        midi_events = i.read(60)

        note = midi_events[0][0][1]
        if note == 0:
            return

        print midi_events[0]
        print midi_events
        print dir(midi_events)
        print '\n'

        # convert them into pygame events.
        midi_evs = pygame.midi.midis2events(midi_events, i.device_id)

        mono = pygame.font.SysFont("monospace", 72)
        label = mono.render(str(midi_events[0][0][1]), 1, (255,255,0))
        screen.blit(label, (100, 100))

pygame.init()
pygame.font.init()
pygame.midi.init()
input_id = pygame.midi.get_default_input_id()
i = pygame.midi.Input( input_id, 60 )

#MBAir: 1440x900
#Ubu: 1920x1080

x, y = pygame.display.list_modes()[0]
screen = pygame.display.set_mode((x,y),pygame.FULLSCREEN)

event_get = pygame.event.get
event_post = pygame.event.post

background = pygame.Surface(screen.get_size())
background = background.convert()
r = 2
g = 2
b = 2
d = 1
clock = pygame.time.Clock()

while 1:

    background.fill((r, g, b))
    screen.blit(background, (0, 0))

    if r > 249:
        d = d * -1
    if r < 2:
        d = d * -1
    r = r + d
    g = g + d
    b = b + d

    handleMIDIEvents(i, screen)
    handleEvents()

    pygame.display.flip()
    clock.tick(120)
