"""
BBOYT control flow core, handles interactions between peripherals and interpreter

Written for Python 3.13.5
Author: Misha Burnayev
"""
import os, threading
# suppress PyGame version and hello messages
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

import microphone, speaker, interpreter

def main():
    print("--- Main active ---")
    mic = microphone.Microphone()
    spkr = speaker.Speaker()
    # cache audio for reduced overhead when called later
    spkr.preload([
        "start.mp3",
        "v4_Faith.wav",
        "monkey.mp3",
        "radio.mp3"
    ])
    
    vosk_path = os.path.expanduser("~/Downloads/B.BOYT/vosk-model-small-en-us-0.15")
    intp = interpreter.Interpreter(vosk_path)
    confirm_mode = False
    music_thread = None

    spkr.play("start.mp3", False)
    while True:
        try:
            print("--- Recording audio ---")
            audio_data = mic.record()
            tokens = intp.parse_speech(audio_data)
            if not tokens:
                continue
            
            if "boy" in tokens:
                if music_thread and music_thread.is_alive():
                    spkr.stop_all()
                    music_thread.join(timeout = 1.0)
                    music_thread = None
                confirm_mode = True
                spkr.play("v4_Faith.wav", False)
                continue

            if confirm_mode:
                if "beer" in tokens:
                    confirm_mode = False
                    print("beer mode")
                    # TODO add GPIO output to send activation signal to motor
                    # Sleep for the amount of time necessary to dispense beverage
                    # time.sleep(10)
                    continue

                elif "monkey" in tokens:
                    confirm_mode = False
                    music_thread = threading.Thread(target = spkr.play, args = ("monkey.mp3", False), daemon = True)
                    music_thread.start()
                    continue

                elif "music" in tokens:
                    confirm_mode = False
                    music_thread = threading.Thread(target = spkr.play, args = ("radio.mp3", True), daemon = True)
                    music_thread.start()
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
