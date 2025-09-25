import pygame
import time

class Speaker:

    def __init__(self):
        pass

    def play(self, sfx):
        pygame.mixer.init()
        sound = pygame.mixer.Sound(sfx)
        playing = sound.play()

        while playing.get_busy():
            time.sleep(0.1)
        
        pygame.mixer.quit()

    def toString(self):
        return f"Speaker stats: TBD"