"""
Handles BBOYT audio output

Written for Python 3.13.5
Author: Misha Burnayev
"""
import time, threading, pygame

class Speaker:

    def __init__(self):
        self.mixer = pygame.mixer
        self.mixer.init()
        self.stop_flag = threading.Event()
        self.sound_cache = {}
    
    def preload(self, sfxs):
        print("--- Preloading audio tracks ---")
        for sfx in sfxs:
            self.sound_cache[sfx] = self.mixer.Sound(sfx)

    def play(self, sfx, loop):
        self.stop_flag.clear()
        
        sound = self.sound_cache[sfx]
    
        while True:
            if self.stop_flag.is_set():
                sound.stop()
                break

            playing = sound.play()

            while playing.get_busy():
                if self.stop_flag.is_set():
                    sound.stop()
                    break
                time.sleep(0.05)
            
            if not loop:
                break
    
    def stop_all(self):
        self.stop_flag.set()
        self.mixer.stop()
        
    def teardown(self):
        self.stop_all()
        self.sound_cache.clear()
        self.mixer.quit()
        self.mixer = None
