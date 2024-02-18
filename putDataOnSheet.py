import analogSense
import digitalSense
import actuators
import urequests
import json
import network
import time




# Google Sheets API endpoint
ENDPOINT = "https://sheets.googleapis.com/v4/spreadsheets/1hO0fLDFaOZE8xihYqYdIOMfc5n5klWppvdve08du2Hg/values/'Sheet1'!A1:append?valueInputOption=RAW"
#ENDPOINT = "https://sheets.googleapis.com/v4/spreadsheets1hO0fLDFaOZE8xihYqYdIOMfc5n5klWppvdve08du2Hg:batchUpdate"

access_token = "ya29.c.c0AY_VpZipLjxIVFTDLMYQcsfwG7frh5zUu8cajMS09kY4ISBfmwPFNebHch2Bmfzog-aUIQpVTH16rxx6pHEzLA2rKoSLm3CcfRoL64EQP5rBfXQmO7jR-_3hDsxJkmPrAMRCtk2_CLuqm1lBNJHGTJ9gL2_MsI9hir4JT_hfBKde0yF3dvoXBRed_gA7jZnjOnCfYJ0Ope1rfLe7pukpU6Aooo17rcaX9EkOtlhh9qN8PB0dQK30XLagcHDs40cLqLOrblSPzYWEH8wrAj_v98cXwAZaHnD8VbkfISBBYbvWJ_xj1h2GgjI__EGKc0XRaYv6SfMEqvOpU6KCkmXjFw6emi1-hxiYqifofhRPXI_SY2qHcVT8bhAE384PXmq1Qo46upig6Sgqdf4jSf46wMfi7yVbkfsR-wW57Fvw4aXlYZixbmfqkZ6xzjdM0nV0O3hpnlpZ4wlj4r1sUWB7Jsmqx58FpB8_0SwIzzQIlBiJ9Fgc0BWYYOtOF6xz-BOF6Y2hY-nMt0ixm7VYMSWcO2j5IuYxMaiUV1z3tjVeXFsWlR5Oo914OpU6F-W_dBvnv-qY4s5ejR4VeBtOUqdunqWwYRdUkgoUZWRYmj1f0yfuuzdWjd_Vxpq80x6y213nU7ewM5Ol33tyigaoctIUaBVpWQnwlulJmUm7o02Q5B1iuOXUYR3bgtM2zjdYm-05u7-_jvsYJrz3ngu8u4S1qgIp06OtzIOpgMzZ7ekZXtfmtxSkVf-XsOwe3hrvOVgVu3ks5j2Zr1o8IBZgnd8bYUewhnbd58I34dQaQScwxqFJ3wptIun3mpOUz_jwbIFa_gds6bxfh-vstymcpWgwSmQ7JtUYxO298XQIX6Ywi-051W172z9WqOSazk8I2jbFblBgv-_s75mOgfMz4Z6ppZbFJ8QBz89YzQQpdeFo1wa-ctd8ZUt_8e92q51h90phc2BIuXg0usW_1ab4uY6IFsyuSj5oRFm0nXR_Ijim-ZgSqVVvSVsU4qu"

# Load your Google API credentials from a JSON file
with open('cred.json') as f:
    credentials = json.load(f)
    

    


# Function to connect to Wi-Fi
def connect_wifi(ssid, password):
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('Connecting to WiFi...')
        sta_if.active(True)
        sta_if.connect(ssid, password)
        while not sta_if.isconnected():
            pass
    print('Connected to WiFi:', ssid)

# Function to update data in Google Sheets
def update_google_sheet(data):
    
    #access_token = get_access_token()
    
    if access_token:
        headers = {'Authorization': 'Bearer ' + access_token}
        payload = {'values': [data]}
        response = urequests.post(ENDPOINT, headers=headers, json=payload)
        if response.status_code == 200:
            print("Data updated successfully!")
        else:
            print("Failed to update data:", response.text)



#Mian Program
try:
    # Connect to WiFi
    wifi_ssid = "SawanKalok_WiFi"
    wifi_password = ""
    connect_wifi(wifi_ssid, wifi_password)
    print("OK1")
    
    # Example usage
    data_to_update = ['New data', 'To be updated']
    print("OK2")
    update_google_sheet(data_to_update)
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
