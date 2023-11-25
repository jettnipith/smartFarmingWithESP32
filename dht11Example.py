"""
Assuming you are using a simple sensor like a temperature and humidity sensor (e.g., DHT11) connected to the GPIO pins:
"""

import dht
import machine
import time

# Setup sensor
sensor = dht.DHT11(machine.Pin(23))  # Replace with the GPIO pin you connected the sensor to

# Main loop
try:
    while True:
        try:
            # Read sensor data
            sensor.measure()
            temperature = sensor.temperature()
            humidity = sensor.humidity()
    
            # Print sensor data
            print(f'Temperature: {temperature}°C, Humidity: {humidity}%')
    
        except Exception as e:
            print(f'Error reading sensor data: {e}')
    
        time.sleep(1)  # Adjust the delay based on your application requirements
except KeyboardInterupt:
    pass
