"""
Handles ashtray input
"""
import time, threading
import Adafruit_DHT

class Ashtray:
    
    def __init__(self, pin):
        self.pin = pin
        self.sensor = Adafruit_DHT.DHT11
        self.stop_flag = threading.Event()
        self.temp_thresh = 30
    
    def detect_temp_change(self, queue):
        self.stop_flag.clear()
        
        while True:
            if self.stop_flag.is_set():
                break
            
            humidity, temperature = Adafruit_DHT.read_retry(self.sensor, self.pin)

            if temperature is not None:
                print(f"Temp: {temperature}°C, Humidity: {humidity}%")
                
                if temperature > self.temp_thresh:
                    print("temp input detected!")
                    queue.put(True)
                    time.sleep(5)
            time.sleep(2)
    
    def stop_all(self):
        self.stop_flag.set()
    
    def teardown(self):
        self.stop_all()
        