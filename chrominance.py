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
        midi_events = i.read(10)
        print "MIDI note is " + str(midi_events[0][0][1])
        print dir(midi_events)
        # convert them into pygame events.
        midi_evs = pygame.midi.midis2events(midi_events, i.device_id)

        mono = pygame.font.SysFont("monospace", 15)
        label = mono.render(str(midi_events[0][0][1], 1, (255,255,0))
        screen.blit(label, (100, 100))

        for m_e in midi_evs:
                event_post( m_e )

pygame.init()
pygame.font.init()
pygame.midi.init()
input_id = pygame.midi.get_default_input_id()
i = pygame.midi.Input( input_id )

#MBAir: 1440x900
#Ubu: 1920x1080
screen = pygame.display.set_mode((1440,900),pygame.FULLSCREEN)

background = pygame.Surface(screen.get_size())
background = background.convert()
r = 2
g = 2
b = 2
d = 1
clock = pygame.time.Clock()

while 1:

    handleMIDIEvents(i, screen)
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
