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

    def play(self, sfx, loop):
        print("sfx playing...")
        self.stop_flag.clear()
        
        if sfx not in self.sound_cache:
            self.sound_cache[sfx] = self.mixer.Sound(sfx)
        
        sound = self.sound_cache[sfx]
    
        while True:
            print("in sfx inner loop")

            if self.stop_flag.is_set():
                sound.stop()
                break

            playing = sound.play()

            while playing.get_busy():
                if self.stop_flag.is_set():
                    sound.stop()
                    break
                time.sleep(0.1)
            
            if loop == False:
                break
    
    def stop_all(self):
        self.stop_flag.set()
        self.mixer.stop()
        
    def teardown(self):
        self.mixer.quit()
        self.mixer = None
