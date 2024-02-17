import analogSense
import digitalSense

#Mian Program
try:
    while True:
        soil = analogSense.moisture()
        air = digitalSense.dht11()
        if air["error"] is None:
            print(f'moisture: {soil["percent"]}')
            print(f'temp: {air["temperature"]}')
            print("----------")
        
        

except KeyboardInterupt:
        pass

