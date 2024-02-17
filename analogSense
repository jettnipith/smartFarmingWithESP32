"""
Connect the photoresistor to one of the analog pins on the ESP32 (e.g., GPIO 34). Connect a resistor in series with the photoresistor to create a voltage divider.
"""

from machine import ADC, Pin
import time


# Setup analog pin
adc = ADC(Pin(26))  # Replace with the actual analog pin you connected the sensor to


def moisture():
    try:
        # Read analog value from the photoresistor
        analog_value = adc.read()
        # Map the analog value to a percentage (adjust the range if needed)
        percent_voltage = (analog_value / 4095) * 100
        moisture_percentage = 100-percent_voltage
        # Print the analog value
        #print(f'Analog Value: {analog_value}')
        return {"analogVal":analog_value, "percent": moisture_percentage}
        
    except Exception as e:
        #print(f'Error reading sensor data: {e}')
        return e
    
