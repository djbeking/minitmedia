import requests
import time
from bs4 import BeautifulSoup
import datetime

authenticate_url = "https://middleware.shqiptv.com/?token=1Nv3n3Ncna&get=authenticate&mac=c4:4e:ac:17:51:a9"
data_url = "https://mw.bestvideostreaming.is/albapptv/?t=l_k&i=%s&os=8&mac=c4:4e:ac:17:51:a9"

# Authentifizierung abrufen
requests.get(authenticate_url)

# 2 Sekunden warten
time.sleep(2)

response = requests.get(data_url)
soup = BeautifulSoup(response.content, "html.parser")

sendernamen = [s.text for s in soup.find_all("c")]
streaming_urls = [s.text for s in soup.find_all("s")]

with open("albapptv_playlist.m3u", "w") as file:
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file.write("# Liste wurde am: " + current_time + " geladen.\n")
    file.write("#EXTM3U\n")
    for i in range(len(sendernamen)):
        file.write("#EXTINF:-1," + sendernamen[i] + "\n")
        file.write("#EXTVLCOPT:http-user-agent=stagefright/1.2 (Linux;Android 7.1.2)\n")
        file.write(streaming_urls[i] + "\n")

print("M3U-Playlist in albapptv_playlist.m3u gespeichert.")
