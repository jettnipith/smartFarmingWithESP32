from machine import Pin
import time

# Setup relay module
relay_pin_1 = Pin(19, Pin.OUT)  # Replace with the actual digital pin you connected the relay to
relay_pin_2 = Pin(18, Pin.OUT)

def relayOn(targetChannel):
    if targetChannel == 1:
        relay_pin_1.value(1)
    elif targetChannel == 2:
        relay_pin_2.value(1)

def relayOff(targetChannel):
    if targetChannel == 1:
        relay_pin_1.value(0)
    elif targetChannel == 2:
        relay_pin_2.value(0)
        


    
