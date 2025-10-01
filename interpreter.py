"""
File for Vosk speech recognition model

Written for Python 3.11.2
Author: Misha Burnayev
"""
import os, wave, json
import vosk

FPS = 44100
CHUNK_DURATION = 0.2

class Interpreter:
    
    def __init__(self, model_path):
        # Suppress verbose output
        vosk.SetLogLevel(-1)
        self.model = vosk.Model(model_path)

    def parse_speech(self, audio):
        try:
            wf = wave.open(audio, "rb")
        except FileNotFoundError:
            print(f"WAV file not found: {audio}")
            return None
        
        rec = vosk.KaldiRecognizer(self.model, FPS)
        chunk_frames = int(FPS * CHUNK_DURATION)
 
        results = []
        
        while True:
            data = wf.readframes(chunk_frames)
            if len(data) == 0:
                break
        
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                if result["text"]:
                    results.append(result["text"])
    
        final_result = json.loads(rec.FinalResult())
        if final_result["text"]:
            results.append(final_result["text"])
        
        wf.close()
        return " ".join(results)
    
    def teardown(self):
        self.model = None
