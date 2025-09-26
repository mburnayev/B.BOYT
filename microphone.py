"""
File for microphone class: handles input collection

Written for Python 3.11.2
Author: Misha Burnayev
"""

import pyaudio
import wave

FORMAT = pyaudio.paInt16
CHANNELS = 1
FPS = 44100


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
        for i in range(0, int(FPS / 1024 * 5)):
            data = stream.read(1024)
            frames.append(data)
        
        stream.stop_stream()
        stream.close()
        
        wf = wave.open("mic_output.wav", "wb")
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(self.p.get_sample_size(FORMAT))
        wf.setframerate(FPS)
        wf.writeframes(b''.join(frames))
        wf.close()
    
    def teardown(self):
        self.p.terminate()


    def toString(self):
        return f"Microphone stats: TBD"