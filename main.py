"""
BBOYT control flow core, handles interactions between peripherals and interpreter

Written for Python 3.13.5
Author: Misha Burnayev
"""
import os
# Suppress PyGame version and hello messages
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

import microphone, speaker, interpreter

def main():
    print("--- Main active ---")
    mic = microphone.Microphone()
    spkr = speaker.Speaker()
    vosk_path = os.path.expanduser("~/Downloads/B.BOYT/vosk-model-small-en-us-0.15")

    intp = interpreter.Interpreter(vosk_path)
    confirm_mode = False

    while(1):
        try:
            print("--- Recording audio ---")
            audio_data = mic.record()
            tokens = intp.parse_speech(audio_data)
            if tokens == None:
                continue
            print(f"Interpreted speech: {tokens}")
            
            if "boy" in tokens:
                confirm_mode = True
                spkr.play("v4_Faith.wav")
                continue

            if confirm_mode == True:
                if "beer" in tokens:
                    confirm_mode = False
                    print("beer mode")
                    # TODO add GPIO output to send activation signal to motor
                    # Sleep for the amount of time necessary to dispense beverage
                    # time.sleep(10)
                    continue

                elif "monkey" in tokens:
                    print("monkey mode")
                    confirm_mode = False
                    # TODO make speaker playing multithreaded
                    # spkr.play("monkey.mp3")
                    continue

                elif "music" in tokens:
                    print("music mode")
                    confirm_mode = False
                    # TODO make speaker playing multithreaded
                    # spkr.play("radio.mp3")
                    continue
                
            elif "quit" in tokens:
                break
        except KeyboardInterrupt:
            break

    print("--- Cleanup ---")
    mic.teardown()
    spkr.teardown()
    intp.teardown()
    print("--- Program Shutdown ---")

if __name__ == "__main__":
    main()
