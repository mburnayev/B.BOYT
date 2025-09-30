"""
Handles verbal output by the BBOYT

Written for Python 3.11.2
Author: Misha Burnayev
"""
import time
import pygame

class Speaker:

    def __init__(self):
        self.mixer = pygame.mixer
        self.mixer.init()

    def play(self, sfx):
        sound = self.mixer.Sound(sfx)
        playing = sound.play()

        while playing.get_busy():
            time.sleep(0.1)
        
    def teardown(self):
        self.mixer.quit()
        self.mixer = None

    def toString(self):
        return f"Speaker stats: TBD"