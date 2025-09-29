"""
File for OpenAI Whisper speech parsing model

Written for Python 3.11.2
Author: Misha Burnayev
"""
import os
import wave, json
import vosk

class Interpreter:
    
    def __init__(self, model_path):
        # Suppress verbose output
        vosk.SetLogLevel(-1)
        self.model = vosk.Model(model_path)

    def parse_speech(self, audio):
        try:
            wf = wave.open(wav_file_path, "rb")
        except FileNotFoundError:
            print(f"WAV file not found: {wav_file_path}")
            return None
        
        sample_rate = wf.getframerate()
        rec = vosk.KaldiRecognizer(model, sample_rate)
        
        while True:
            # Read all frames from 5 second clip
            data = wf.readframes(44100)
            if len(data) == 0:
                break
        
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                if result['text']:
                    results.append(result['text'])
                    print(f"Recognized: {result['text']}")
    
        final_result = json.loads(rec.FinalResult())
        if final_result['text']:
            results.append(final_result['text'])
            print(f"Final: {final_result['text']}")
        
        wf.close()
        return ' '.join(results)
    
    def teardown(self):
        pass
    
    def toString(self):
        return f"Interpreter stats: TBD"