from stem.control import Controller
from stem import Signal
import requests, time
proxies = {
    "http" : "socks5h://127.0.0.1:9150",
    "https" : "socks5h://127.0.0.1:9150"    
}
r = requests.get("http://ip-api.com/line", proxies = proxies)
r.close()
for line in r.content.decode("utf-8").split("\n"):
    print(line)
controller = Controller.from_port(port = 9151)
controller.authenticate(password="####")
controller.signal(Signal.NEWNYM)
time.sleep(5)
r = requests.get("http://ip-api.com/line", proxies = proxies)
r.close()
for line in r.content.decode("utf-8").split("\n"):
    print(line)


