from machine import Pin
import time

# Setup relay module
relay_pin = Pin(12, Pin.OUT)  # Replace with the actual digital pin you connected the relay to

# Function to turn the relay on
def relay_on():
    relay_pin.value(1)

# Function to turn the relay off
def relay_off():
    relay_pin.value(0)

# Main loop
while True:
    try:
        # Turn the relay on
        relay_on()
        print('Relay is ON')
        time.sleep(2)

        # Turn the relay off
        relay_off()
        print('Relay is OFF')
        time.sleep(2)

    except Exception as e:
        print(f'Error controlling relay module: {e}')

    time.sleep(2)  # Adjust the delay based on your application requirements
