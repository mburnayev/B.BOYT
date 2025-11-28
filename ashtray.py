"""
Handles ashtray input
"""
import time, threading
import dht11

class Ashtray:
    
    def __init__(self, pin):
        self.sensor = dht11.DHT11(pin)
        self.stop_flag = threading.Event()
        self.temp_thresh = 25
    
    def detect_temp_change(self, queue):
        self.stop_flag.clear()
        
        while True:
            if self.stop_flag.is_set():
                break
            
            r = self.sensor.read()

            if r.is_valid():
                print(f"Temperature: {r.temperature} C")
                if r.temperature > self.temp_thresh:
                    print("temp input detected!")
                    queue.put(True)
                    time.sleep(5)
            time.sleep(2)
    
    def stop_all(self):
        self.stop_flag.set()
    
    def teardown(self):
        self.stop_all()
        