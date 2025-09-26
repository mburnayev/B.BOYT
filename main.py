"""
BBOYT core script, handles microphone, speaker, and model interactions, and handles control flow between the aformentioned modules

Written for Python 3.11.2
Author: Misha Burnayev
"""

import os
import microphone, speaker

def main():
    print("--- Main active ---")
    m1 = microphone.Microphone()
    mic_input = m1.record()
    
    # TODO: add speech recognition model here,
    # and control logic based on parsed speech

    s1 = speaker.Speaker()
    s1.play("mic_output.wav")
    
    # Cleanup
    os.remove("mic_output.wav")
    m1.teardown()
    s1.teardown()

if __name__ == "__main__":
    main()