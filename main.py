"""
BBOYT control flow core, handles interactions between peripherals and interpreter

Written for Python 3.13.5
Author: Misha Burnayev
"""
import os, threading, time
from queue import Queue
import RPi.GPIO as GPIO
# suppress PyGame version and hello messages
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

import microphone, speaker, interpreter, ashtray

def kill_sfx(thread, speaker):
    if thread and thread.is_alive():
        speaker.stop_all()
        thread.join(timeout = 1.0)
    return None

def main():
    print("--- Configuration ---")
    # pin and digital I/O setup
    GPIO.setmode(GPIO.BCM)
    dht11_pin = 4 # GPIO4 - pin 7
    motor_pin = 17 # GPIO17 - pin 11
    
    GPIO.setup(motor_pin, GPIO.OUT)
    GPIO.output(motor_pin, GPIO.LOW)
    
    mic = microphone.Microphone()
    spkr = speaker.Speaker()
    tray = ashtray.Ashtray(dht11_pin)
    
    # cache audio for reduced overhead when called later
    sfx_list = ["./sfx/start.mp3", "./sfx/v4_Faith.wav", "./sfx/monkey.mp3", "./sfx/radio.mp3", "./sfx/pain.mp3"]
    spkr.preload(sfx_list)
    
    vosk_path = os.path.expanduser("~/Downloads/B.BOYT/vosk-model-small-en-us-0.15")
    intp = interpreter.Interpreter(vosk_path)
    tokens = None
    confirm_mode = False
    music_thread = None
    sensing_queue = Queue()
    
    print("--- Main active ---")
    # verbally notify users that bot is online
    spkr.play(sfx_list[0], False)
    
    # spawn separate thread for ashtray temperature sensing
    ashtray_thread = threading.Thread(target = tray.detect_temp_change, args = (sensing_queue,), daemon = False)
    ashtray_thread.start()
    
    while True:
        try:
            ashtray_triggered = False
            if not sensing_queue.empty():
                sensing_queue.get()
                ashtray_triggered = True
            
            if ashtray_triggered:
                confirm_mode = False
                music_thread = kill_sfx(music_thread, spkr)
                spkr.play(sfx_list[4], False)
                continue

            print("--- Recording audio ---")
            audio_data = mic.record()
            tokens = intp.parse_speech(audio_data)
            
            if not tokens:
                continue
            
            if "boy" in tokens:
                confirm_mode = True
                music_thread = kill_sfx(music_thread, spkr)                    
                spkr.play(sfx_list[1], False)
                continue

            if confirm_mode:
                if "beer" in tokens:
                    confirm_mode = False
                    print("beer mode")
                    GPIO.output(motor_pin, GPIO.HIGH)
                    # sleep for the amount of time necessary to dispense beverage
                    time.sleep(1)
                    GPIO.output(motor_pin, GPIO.LOW)
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
    tray.teardown()
    mic.teardown()
    spkr.teardown()
    intp.teardown()
    GPIO.output(motor_pin, GPIO.LOW)
    GPIO.cleanup()
    print("--- Program Shutdown ---")

if __name__ == "__main__":
    main()
