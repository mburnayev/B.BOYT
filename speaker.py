"""
Handles BBOYT audio output

Written for Python 3.13.5
Author: Misha Burnayev
"""
import time, pygame

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
