import requests
from requests.structures import CaseInsensitiveDict
import time

print(" .________.             ______                           ")
time.sleep(0.1)
print(" |__    __|  __ ____   |   .  |__    _____ ____  ____    ")
time.sleep(0.1)
print("    |  |  |_|  |  __|  |   |  |  |  |  .  |   _||  __|   ")
time.sleep(0.1)
print("    |  |   _   |  __|  |   ___|  |_ |  _  |  |_ |  __|   ")
time.sleep(0.1)
print("    |__|__| |__|____|  |__|   |____||_| |_|____||____|   ")
time.sleep(0.1)
print("             CREATED BY: black-hot-pepper              \n")
time.sleep(0.1)

print("   \033[0;37;44mI'm not responsible for the misuse of the tool\033[m")
print("\033[1;30;44mNão me responsabilizo pelo uso indevido da ferramenta\033[m \n")

def DoIt():
    print("Put the IP adress:")
    IP = input(str("\033[1;34m[*]\033[m "))

    def Locate(ip):
        url = f"https://api.ipbase.com/v2/info?ip={ip}&apikey=iTrFZ0u3KNdyHX8fMX2Z1iFSRRkEBLDYEHiPIneO"
        req = requests.get(url)
        req_str = str(req)
        if req_str == '<Response [200]>':
            pass
        else:
            print("\033[1;45mAn error has occurred, please restart the program...\033[m")
        req_dic = req.json()
        
        print("\033[1;34mWaiting for location information...\033[m \n")
        time.sleep(3)
        
        
        #print(req_dic['data'])
        CITY = req_dic['data']['location']['city']['name']
        REGION = req_dic['data']['location']['region']['name']
        COUNTRY = req_dic['data']['location']['country']['alpha2']
        WIFI_CONNECTION = req_dic['data']['connection']['isp']
        WIFI_ORGANIZATION = req_dic['data']['connection']['organization']
        LAT = req_dic['data']['location']['latitude']
        LON = req_dic['data']['location']['longitude']
        TIME = req_dic['data']['timezone']['current_time']

        weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid=100e5db8f22f34f0b3d05c8de8882535"

        req = requests.get(weather_url)
        req_dic = req.json()
        sensação = req_dic['main']['feels_like'] - 273.15
        press = req_dic['main']['pressure']
        humidity = req_dic['main']['humidity']
        temp = req_dic['main']['temp'] - 273.15

        print("=" * 60)
        print("\033[1;30mLOCATION INFO:\033[m \n")
        print(f"\033[1;33mCITY:\033[m             |   \033[1;32m{CITY}\033[m")
        print(f"\033[1;33mREGION:\033[m           |   {REGION}")
        print(f"\033[1;33mCOUNTRY:\033[m          |   {COUNTRY}")
        print(f"\033[1;33mLATITUDE:\033[m         |   {LAT}")
        print(f"\033[1;33mLONGITUDE:\033[m        |   {LON}")
        print(f"\033[1;33mCURRENT_TIME:\033[m     |   {TIME}")

        print("\n\033[1;30mNETWORK INFO:\033[m \n")
        print(f"\033[1;33mIP_ADRESS:\033[m        |   \033[1;32m{IP}\033[m")
        print(f"\033[1;33mWIFI_CONNECTION:\033[m  |   {WIFI_CONNECTION}")
        print(f"\033[1;33mWIFI_ORGANIZATION:\033[m|   {WIFI_ORGANIZATION}")

        print("\n\033[1;30mWEATHER INFO:\033[m \n")
        print(f"\033[1;33mTEMPERATURE:\033[m      |   {round(temp)}°C")
        print(f"\033[1;33mHUMIDITY:\033[m         |   {humidity}%")
        print(f"\033[1;33mATM:\033[m              |   {press} Pa")

        print("=" * 60)
    Locate(IP)
DoIt()