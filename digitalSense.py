import dht
import machine
import time


# Setup sensor
sensor = dht.DHT11(machine.Pin(23))  # Replace with the GPIO pin you connected the sensor to
time.sleep(1)

def dht11():
    
    try:
        # Read sensor data
        sensor.measure()
        
        temperature = sensor.temperature()
        humidity = sensor.humidity()

        #Print sensor data
        #print(f'Temperature: {temperature}°C, Humidity: {humidity}%')
        
        return {"temperature": temperature, "humidity": humidity, "error": None}

    except Exception as e:
        #print(f'Error reading sensor data: {e}')
        return {"error": e}


