from machine import Pin,PWM
import time

sg90 = PWM(Pin(32, mode=Pin.OUT))
sg90.freq(50)
snd = 18

def tone(pin, frequency, duration_ms):
    p = PWM(Pin(pin))
    p.freq(frequency)
    p.duty(512)
    time.sleep_ms(duration_ms)
    p.deinit()


while True:
    sg90.duty(40)
    time.sleep(1)
    tone(snd, 800, 50)
    sg90.duty(90)
    time.sleep(1)
    sg90.duty(108)
    time.sleep(1)
