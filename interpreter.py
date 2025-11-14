"""
Vosk speech recognition model for interpreting audio data

Written for Python 3.13.5
Author: Misha Burnayev
"""
import vosk, json

FPS = 16000

class Interpreter:
    
    def __init__(self, model_path):
       # Suppress verbose output
       vosk.SetLogLevel(-1)
       self.model = vosk.Model(model_path)
       self.grammar = '["boy", "beer", "monkey", "music", "[unk]"]'

    def parse_speech(self, audio_bytes):        
        rec = vosk.KaldiRecognizer(self.model, FPS, self.grammar)
        rec.AcceptWaveform(audio_bytes)
        result = json.loads(rec.FinalResult())
        
        detected = result.get("text", "").strip().lower()
        
        keywords = ["boy", "beer", "monkey", "music"]
        if detected in keywords:
            return detected
        
        return None

    def teardown(self):
        self.model = None
