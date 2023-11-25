"""
Connect the signal wire of the servo motor to one of the PWM-capable pins on the ESP32 (e.g., GPIO 13)
"""

from machine import Pin, PWM
import time

# Setup servo motor
servo_pin = Pin(13, Pin.OUT)  # Replace with the actual PWM pin you connected the servo to
servo_pwm = PWM(servo_pin, freq=50)  # Set PWM frequency to 50 Hz (standard for servo motors)

# Function to move the servo to a specific angle
def move_servo(angle):
    duty_cycle = int(((angle / 180) * 1000) + 500)  # Convert angle to duty cycle
    servo_pwm.duty(duty_cycle)

# Main loop
while True:
    try:
        # Move the servo to different angles
        move_servo(0)    # Move to 0 degrees
        time.sleep(1)
        move_servo(90)   # Move to 90 degrees
        time.sleep(1)
        move_servo(180)  # Move to 180 degrees
        time.sleep(1)

    except Exception as e:
        print(f'Error controlling servo motor: {e}')

    time.sleep(2)  # Adjust the delay based on your application requirements
