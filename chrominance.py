#! /usr/bin/env python
# Coding: utf-8

import pygame
import pygame.midi
from pygame.locals import *
from random import randrange

class Chrominance():

    event_get = pygame.event.get
    event_post = pygame.event.post

    oscillate = True
    r = 2
    g = 2
    b = 2
    d = 1

    def handleEvents(self):

        events = self.event_get()
        for e in events:
            if e.type in [QUIT]:
                quit()
            if e.type == KEYDOWN and e.key == K_ESCAPE:
               quit()
            if e.type in [pygame.midi.MIDIIN] and e.status != 248:

                # Mod wheel!
                if e.status == 176 and e.data1 == 1:
                    self.oscillate = False
                    self.r = min(e.data2 * 2 + 1, 254)
                    self.g = min(e.data2 * 2 + 1, 254)
                    self.b = min(e.data2 * 2 + 1, 254)

                # Cutoff knob!
                if e.status == 176 and e.data1 == 74:
                    self.oscillate = True
                    self.r = min(e.data2 * 2 + 1, 254)

                # Resonsance knob!
                if e.status == 176 and e.data1 == 71:
                    self.oscillate = True
                    self.g = min(e.data2 * 2 + 1, 254)

                # Resonsance knob!
                if e.status == 176 and e.data1 == 73:
                    self.oscillate = True
                    self.b = min(e.data2 * 2 + 1, 254)

                print str(e)
                label = self.mono.render(str(e.data2), 1, self.get_random_color())
                self.screen.blit(label, self.get_random_screen_location())

        if self.i.poll():
            midi_events = self.i.read(10)
            # convert them into pygame events.
            midi_evs = pygame.midi.midis2events(midi_events, self.i.device_id)

            for m_e in midi_evs:
                self.event_post( m_e )

    # def handleMIDIEvents(i, screen):
    #     if i.poll():
    #         midi_events = i.read(10)

    #         note = midi_events[0][0][1]
    #         if note == 0:
    #             return

    #         print midi_events[0]
    #         print midi_events
    #         print dir(midi_events)
    #         print '\n'

    #         # convert them into pygame events.
    #         midi_evs = pygame.midi.midis2events(midi_events, i.device_id)
    #         for m_e in midi_evs:
    #             event_post( m_e )

    #         mono = pygame.font.SysFont("monospace", 72)
    #         label = mono.render(str(midi_events[0][0][1]), 1, (255,255,0))
    #         screen.blit(label, (100, 100))

    def setup(self):

        pygame.init()
        pygame.fastevent.init()
        self.event_get = pygame.fastevent.get
        self.event_post = pygame.fastevent.post
        pygame.font.init()
        self.mono = mono = pygame.font.SysFont("monospace", 72)
        pygame.midi.init()
        input_id = pygame.midi.get_default_input_id()
        self.i = pygame.midi.Input( input_id, 60 )

        #MBAir: 1440x900
        #Ubu: 1920x1080

        self.x, self.y = pygame.display.list_modes()[0]
        print self.x, self.y
        self.screen = pygame.display.set_mode((self.x,self.y),pygame.FULLSCREEN)
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()

        self.clock = pygame.time.Clock()

    def run(self):
        while 1:

            self.background.fill((self.r, self.g, self.b))
            self.screen.blit(self.background, (0, 0))

            if self.oscillate:
                if self.r > 249 or self.b > 249 or self.g > 249:
                    self.d = self.d * -1
                if self.r < 2 or self.b <2 or self.g < 2:
                    self.d = self.d * -1
                self.r = self.r + self.d
                self.g = self.g + self.d
                self.b = self.b + self.d

            self.r = max(self.r, 0)
            self.g = max(self.g, 0)
            self.b = max(self.b, 0)

            self.r = min(self.r, 255)
            self.g = min(self.g, 255)
            self.b = min(self.b, 255)

            self.handleEvents()

            pygame.display.flip()
            self.clock.tick(60)

    def get_random_screen_location(self):
        return (randrange(self.x-1), randrange(self.y-1))

    def get_random_color(self):
        return (randrange(255), randrange(255), randrange(255))

if __name__ == '__main__':

    c = Chrominance()
    c.setup()
    c.run()


