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
    i1 = interpreter.Interpreter()

    while(input("Enter input: ") != "q"):
        mic_input = m1.record()
        tokens = i1.parse_speech(mic_input)
        print(tokens)
    
    # TODO: add speech recognition model here,
    # and control logic based on parsed speech

    # s1.play("mic_output.wav")
    
    # Cleanup
    os.remove("mic_output.wav")
    m1.teardown()
    s1.teardown()

if __name__ == "__main__":
    main()