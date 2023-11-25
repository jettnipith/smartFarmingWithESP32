from machine import ADC, Pin
from time import sleep

# Define the analog pin for the moisture sensor
moisture_pin = 34  # You may need to change this based on your ESP32 pin configuration

# Create ADC object
adc = ADC(Pin(moisture_pin))
adc.atten(ADC.ATTN_11DB)  # Set attenuation level to 11dB for full 3.3V range

def read_moisture():
    # Read analog value from the moisture sensor
    moisture_value = adc.read()

    # Map the analog value to a percentage (adjust the range if needed)
    moisture_percentage = (moisture_value / 4095) * 100

    return moisture_value, moisture_percentage

while True:
    moisture_value, moisture_percentage = read_moisture()

    print("Moisture Value:", moisture_value)
    print("Moisture Percentage:", moisture_percentage, "%")

    sleep(1)  # You can adjust the sleep time according to your needs
