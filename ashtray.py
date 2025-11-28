"""
Handles ashtray input
"""
import time, threading
import dht11

class Ashtray:
    
    def __init__(self, pin):
        self.sensor = dht11.DHT11(pin)
        self.stop_flag = threading.Event()
        self.temp_thresh = 27 # TODO: take inital temp reading so boy isn't always screaming on a hot summer day
    
    def detect_temp_change(self, queue):
        self.stop_flag.clear()
        
        while True:
            if self.stop_flag.is_set():
                break
            
            result = self.sensor.read()

            if result.is_valid():
                if result.temperature > self.temp_thresh:
                    queue.put(True)
                    time.sleep(10)
            time.sleep(1)
    
    def stop_all(self):
        self.stop_flag.set()
    
    def teardown(self):
        self.stop_all()
        