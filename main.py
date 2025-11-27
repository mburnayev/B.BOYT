"""
BBOYT control flow core, handles interactions between peripherals and interpreter

Written for Python 3.13.5
Author: Misha Burnayev
"""
import os, threading
from queue import Queue
import RPi.GPIO as GPIO
# suppress PyGame version and hello messages
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

import microphone, speaker, interpreter, ashtray

def main():
    print("--- Setup ---")
    GPIO.setmode(GPIO.BCM)
    # use 7th pin (GPIO4) for digital input and 11th pin (GPIO17) for digital output
    motor_pin = 17
    
    GPIO.setup(motor_pin, GPIO.OUT)
    
    mic = microphone.Microphone()
    spkr = speaker.Speaker()
    tray = ashtray.Ashtray(dht11_pin)
    
    # cache audio for reduced overhead when called later
    sfx_list = ["./sfx/start.mp3", "./sfx/v4_Faith.wav", "./sfx/monkey.mp3", "./sfx/radio.mp3", "./sfx/pain.mp3"]
    spkr.preload(sfx_list)
    
    vosk_path = os.path.expanduser("~/Downloads/B.BOYT/vosk-model-small-en-us-0.15")
    intp = interpreter.Interpreter(vosk_path)
    confirm_mode = False
    music_thread = None
    ashtray_thread = None
    sensing_queue = Queue()
    
    print("--- Main active ---")
    # verbally notify users that bot is online
    spkr.play(sfx_list[0], False)
    
    # spawn separate thread for ashtray temperature sensing
    ashtray_thread = threading.Thread(target = tray.detect_temp_change, args = (sensing_queue), daemon = True)
    ashtray_thread.start()
    
    while True:
        try:
            print("--- Recording audio ---")
            audio_data = mic.record()
            tokens = intp.parse_speech(audio_data)
            if not tokens:
                continue
            
            if "boy" in tokens or sensing_queue.get() == True:
                if music_thread and music_thread.is_alive():
                    spkr.stop_all()
                    music_thread.join(timeout = 1.0)
                    music_thread = None
    
                if sensing_queue.get() is None:
                    confirm_mode = False
                    spkr.play(sfx_list[4], False)
                else:
                    confirm_mode = True
                    spkr.play(sfx_list[1], False)
                continue

            if confirm_mode:
                if "beer" in tokens:
                    confirm_mode = False
                    print("beer mode")
                    GPIO.output(motor_pin, GPIO.HIGH)
                    # Sleep for the amount of time necessary to dispense beverage
                    # time.sleep(10)
                    continue

                elif "monkey" in tokens:
                    confirm_mode = False
                    music_thread = threading.Thread(target = spkr.play, args = (sfx_list[2], False), daemon = True)
                    music_thread.start()
                    continue

                elif "music" in tokens:
                    confirm_mode = False
                    music_thread = threading.Thread(target = spkr.play, args = (sfx_list[3], True), daemon = True)
                    music_thread.start()
                    continue
                
            elif "banana" in tokens:
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
