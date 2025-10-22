"""
File for Vosk speech recognition model

Written for Python 3.11.2
Author: Misha Burnayev
"""
import vosk, json

FPS = 44100
CHUNK_DURATION = 0.2

class Interpreter:
    
    def __init__(self, model_path):
        # Suppress verbose output
        vosk.SetLogLevel(-1)
        self.model = vosk.Model(model_path)

    def parse_speech(self, audio_bytes):        
        rec = vosk.KaldiRecognizer(self.model, FPS)
        chunk_size = int(FPS * CHUNK_DURATION * 2)
 
        results = []
        offset = 0
        
        while offset < len(audio_bytes):
            chunk = audio_bytes[offset:offset + chunk_size]
            offset += chunk_size
        
            if rec.AcceptWaveform(chunk):
                result = json.loads(rec.Result())
                if result["text"]:
                    results.append(result["text"])
    
        final_result = json.loads(rec.FinalResult())
        if final_result["text"]:
            results.append(final_result["text"])
        
        return " ".join(results)
    
    def teardown(self):
        self.model = None
