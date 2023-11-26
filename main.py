import time
from machine import Pin, ADC
import dht

#กำหนดให้ Pin 2 เป็น output
led_pin = Pin(2, Pin.OUT)

#กำหนด pin ที่ใช้สื่อสารกับ dht
sensorDHT = dht.DHT11(Pin(23))

#กำหนด pin ที่ใช้สื่อสารกับ moisture sensor
adcMoisture = ADC(Pin(34))
adcMoisture.atten(ADC.ATTN_11DB)

#กำหนด pin ที่ใช้สื่อสารกับ relay
relay_pin = Pin(12, Pin.OUT)

def beep():
    led_pin.value(1)
    time.sleep(0.1)
    led_pin.value(0)
    time.sleep(0.1)
    
def temp_humid():
    try:
        #วัดค่าความชื้น และอถหภูมิของอากาศ
        sensorDHT.measure()
        #เอาเฉพาะอุณหภูมิ
        temperature = sensorDHT.temperature()
        #เอาเฉพาะความชื้น
        humidity = sensorDHT.humidity()
        #print(f'อุณหภูมิ: {temperature} องศาเซลเซียส, ความชื้นสัมพัทธ์: {humidity} %')
        return [temperature,humidity]
    except Exception as e:
        #print(f'error reading sensor data: {e}')
        return f'error reading sensor data: {e}'
    
def read_moisture():
    moisture_value = adcMoisture.read()
    return moisture_value

def relay_on():
    relay_pin.value(1)

def relay_off():
    relay_pin.value(0)

#ต้องมี  try
try:
    #โปรแกรมเริ่มทำงานตรงนี้
    a = 0
    while True:
        print(a)
        a += 1
        time.sleep(0.1)
        beep()
        th = temp_humid()
        currentTemp = th[0]
        currentHumidity = th[1]

        print(f'อุณหภูมิ: {currentTemp} องศาเซลเซียส, ความชื้นสัมพัทธ์: {currentHumidity} %')
        
        if currentTemp >= 20 and currentTemp <= 25 :
            print(f'{currentTemp} องศาฯ อุณหภูมิเหมาะสม')
        elif currentTemp < 20:
            print(f'{currentTemp} องศาฯ เย็นเกินไป ควรเปิด Heater')
        else:
            print(f'{currentTemp} องศาฯ ร้อนเกินไป ควรเปิดพัดลมระบายอากาศ')
        
        if currentHumidity >= 50 and currentHumidity <=70:
            print(f'{currentHumidity} % ความชื้นปกติ')
            
        elif currentHumidity < 50:
            print(f'{currentHumidity} % ความชื้นต่ำเกินไป ควรพ่นหมอก')
            
        else:
            print(f'{currentHumidity} % ความชื้นสูงเกินไป ควรเปิดพัดลมระบายอากาศ')
            
        
        moisture = read_moisture()
        revisedMoisture = 4095-moisture
        percentMoisture = revisedMoisture/4095*100
        
        
        if percentMoisture < 40:
            print(f'{percentMoisture} % ความชื้นของดินต่ำ ควรเปิดปั๊มน้ำ')
            relay_on()
        else:
            print(f'{percentMoisture} % ความชื้นของดินปกติ ควรปิดปั๊มน้ำ')
            relay_off()


#มี try ต้องมี except
except KeyboardInterupt:
    pass