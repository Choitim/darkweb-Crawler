from stem.control import Controller
from stem import Signal
import requests, time
PROXIES = {
        "http" : "socks5h://127.0.0.1:9150",
        "https" : "socks5h://127.0.0.1:9150"    
}
        
    
def getTorIp():
    # 토르 네트워킹을 위한 프록시 설정, protocol은 
    # socks5 - 로컬 이름 확인이 있는 SOCKS5를 의미합니다.
    # socks5h - 프록시 이름이 확인되는 SOCKS5를 의미합니다.
    # https://jung-max.github.io/2022/02/09/Linux-libcurl%20Proxies/
    # 현재 토르 네트워크의 아이피를 확인하기 위한 코드
    r = requests.get("http://ip-api.com/line", proxies = PROXIES)
    r.close()
    print(r.content.decode("utf-8").split("\n"))
    return r.content.decode("utf-8").split("\n")[-2].strip()
    
def torIpReset(before_ip):
    count = 1
    while True:
        ### 토르네트워크의 제어포트를 통해 tor network 리셋을 하여 ip를 다시 받는다.
        controller = Controller.from_port(port = 9151)
        controller.authenticate(password="1234")
        controller.signal(Signal.NEWNYM)        
        # 아이피가 바뀌였는지 여부를 다시 확인
        current_ip = getTorIp()
        print(count, before_ip, current_ip)
        if before_ip == current_ip:
            count += 1
            continue
        return current_ip

def getHTML(url):
    if not url.startswith("http://"):
        url = "http://" + url
    r = requests.get(url, proxies = PROXIES)
    r.close()
    if url.startswith("http://"):
        url_ = url[7:]
    elif url.startswith("https://"):
        url_ = url[8:]
    fd = open(url_ + ".html", "wb")
    fd.write(r.content)
    fd.close()


    
#before_ip = getTorIp()
#current_ip = torIpReset(before_ip)
getHTML("http://juhanurmihxlp77nkq76byazcldy2hlmovfu2epvl5ankdibsot4csyd.onion")

