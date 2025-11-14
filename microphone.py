"""
Creates microphone stream to capture audio, returns bytearray of audio data

Written for Python 3.13.5
Author: Misha Burnayev
"""
import pyaudio

FORMAT = pyaudio.paInt16
CHANNELS = 1
FPS = 16000

class Microphone:

    def __init__(self):
        self.p = pyaudio.PyAudio()

    def record(self):
        stream = self.p.open(format = FORMAT,
                    channels = CHANNELS,
                    rate = FPS,
                    input = True,
                    frames_per_buffer = 1024)
        
        frames = []
        # take input for 2 seconds
        for i in range(0, int(FPS / 1024 * 2)):
            data = stream.read(1024)
            frames.append(data)
        
        stream.stop_stream()
        stream.close()
        
        return b"".join(frames)
    
    def teardown(self):
        self.p.terminate()
        self.p = None
