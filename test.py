from requests import get
import time


starttime = time.time()
while True:
    ip = get('https://api.ipify.org').content.decode('utf8')
    print(ip)
    time.sleep(5.0 - ((time.time() - starttime) % 5.0))
