import OLED
import time
import analogSense as ans
import actuators as act
import digitalSense as dgs
import urequests
import network

endpoint = "https://script.google.com/macros/s/AKfycbwnLffb68kQJ8lS2AZCdUZr8J4f87gVmvNmW-OKEexoAm1WXCwFU5FZMawbp8DRhhN4UA/exec"

#connect to wifi
WIFI_SSID = "Xiaomi 14k" #ใช้ของตัวเองนะ
WIFI_PASS = "qa123456" #ใช้ของตัวเองนะ

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    
    if not wlan.isconnected():
        print("Connecting to Wifi..")
        wlan.connect(WIFI_SSID, WIFI_PASS)
        while not wlan.isconnected():
            time.sleep(1)
            print("Waiting for connection...")
    print("Connected IP:", wlan.ifconfig()[0])

connect_wifi()
#ฟังก์ชั้นในการส่งข้อมูล
def send_to_sheet(moisture_percent, soil_status, air_temp, air_humid):
    try:
        url = (endpoint + f"?moisture={moisture_percent}&status={soil_status}&temp={air_temp}&humid={air_humid}")
        r = urequests.get(url)
        r.close()
        print("sent to google sheet")
    except Exception as e:
        print("Error sending to sheet:", e)

act.relayOff(1)

while True:
    soil = ans.moisture()
    air = dgs.dht11()
    moisture_percent = soil['percent']
    air_temp = air['temperature']
    air_humid = air['humidity']
    if moisture_percent > 60:
          soil_status = "toowet"
          act.relayOff(1)
    elif moisture_percent > 40:   
          soil_status = "normal"
          act.relayOff(1)
    else:
          soil_status = "toodry"
          act.relayOn(1)

    #ส่งขึ้น google sheet
    send_to_sheet(moisture_percent, soil_status, air_temp, air_humid)
    OLED.show_3_line(f'moisture: {moisture_percent} %',f'status: {soil_status}','')
    time.sleep(2)
    OLED.show_3_line(f'Temperature: {air_temp} C',f'Humidity: {air_humid} %','')
    time.sleep(2)
    
