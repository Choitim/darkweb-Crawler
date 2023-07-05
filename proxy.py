from stem.control import Controller
from stem import Signal
import requests


# 토르 네트워킹을 위한 프록시 설정, protocol은
#socks5 - 로컬 이름 확인이 있는 SOCKS5를 의미합니다.
#https://jung-max.github.io/2022/02/09/Linux-libcurl%20proxies/
porxies = {
    "http": "socks5h://127.0.0.1:9150",
    "https": "socks5h://127.0.0.1:9150"
}
#현재 토르 네트워크의 아이피를 확인하기 위한 코드
r = requests.get("http://ip.api.com/line", proxies = proxies)
r.close()

for line in r.content.decode("utf-8").split("/n"):
    print(line)

#토르네트워크와 제어포트를 통해 tor network 리셋을 하여 ip를 받는다.

Controller = Controller.from_port(port = 9151)
Controller.authenticate(password = "####")
Controller.signal(Signal.NEWNYM)

#아이피가 바뀌었는지 여부를 다시 확인

r.requests.get("http://ip-api.com/line", proxies = proxies)
r.close()
for line in r.content.decode("utf-8").split("\n"):
    print(line)