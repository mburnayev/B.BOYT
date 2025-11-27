"""
Handles ashtray input
"""
import time, threading
import RPi.GPIO as GPIO

class Ashtray:
    
    def __init__(self):
        self.GPIO.setmode(GPIO.BCM)
        dht11_pin = 7
        self.GPIO.setup(dht11_pin, GPIO.IN)
    
    def detect_temp_change(self, queue):
        while True:
            if self.GPIO.input(dht11_pin) == GPIO.HIGH:
                queue.put(True)
                time.sleep(5)
    
    def teardown(self)
        self.active_flag.clear()
        