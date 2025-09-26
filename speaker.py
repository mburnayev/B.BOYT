"""
File for speaker class: handles verbal output

Written for Python 3.11.2
Author: Misha Burnayev
"""

import pygame
import time

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

    def toString(self):
        return f"Speaker stats: TBD"