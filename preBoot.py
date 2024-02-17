import analogSense




#Mian Program
try:
    while True:
        soil = analogSense.moisture()
        print(f'moisture: {soil["percent"]}')
        

except KeyboardInterupt:
        pass

