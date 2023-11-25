"""
Connect the photoresistor to one of the analog pins on the ESP32 (e.g., GPIO 34). Connect a resistor in series with the photoresistor to create a voltage divider.
"""

from machine import ADC, Pin
import time


# Setup analog pin
adc = ADC(Pin(26))  # Replace with the actual analog pin you connected the sensor to

# Main loop
try:
    while True:
        try:
            # Read analog value from the photoresistor
            analog_value = adc.read()
    
            # Print the analog value
            print(f'Analog Value: {analog_value}')
    
        except Exception as e:
            print(f'Error reading sensor data: {e}')
    
        time.sleep(2)  # Adjust the delay based on your application requirements
except KeyboardInterupt:
    pass
