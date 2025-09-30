"""
BBOYT core script, handles microphone, speaker, and model interactions, and handles control flow between the aformentioned modules

Written for Python 3.11.2
Author: Misha Burnayev
"""
import os
import microphone, speaker, interpreter

def main():
    print("--- Main active ---")
    m1 = microphone.Microphone()
    s1 = speaker.Speaker()
    vosk_path = os.path.expanduser("~/Downloads/B.BOYT/vosk-model-small-en-us-0.15")
    i1 = interpreter.Interpreter(vosk_path)

    while(1):
        m1.record()
        tokens = i1.parse_speech("mic_output.wav")
        print(f"Interpreted speech: {tokens}")
        
        if "quit" in tokens:
            break
        
        elif "boy" in tokens:
            s1.play("v4_Faith.wav")


    print("--- Cleanup ---")
    os.remove("mic_output.wav")
    m1.teardown()
    s1.teardown()
    i1.teardown()
    
    print("--- Program Shutdown ---")

if __name__ == "__main__":
    main()