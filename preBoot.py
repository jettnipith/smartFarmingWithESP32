import analogSense
import digitalSense
import actuators

#Mian Program
try:
    while True:
        soil = analogSense.moisture()
        air = digitalSense.dht11()
        #prevent error from dht11
        if air["error"] is None:
            print(f'moisture: {soil["percent"]}')
            print(f'temp: {air["temperature"]}')
            print("----------")
            if soil["percent"] < 5:
                actuators.relayOn(1)
            else:
                actuators.relayOff(1)
except KeyboardInterupt:
        pass
