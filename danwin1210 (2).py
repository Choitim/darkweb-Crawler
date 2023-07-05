
from stem.control import Controller
from stem import Signal
import requests, time, sqlite3, os, time
from bs4 import BeautifulSoup
PROXIES = {
        "http" : "socks5h://127.0.0.1:9150",
        "https" : "socks5h://127.0.0.1:9150"    
}

DB_PATH = "darkweb5.db"
        
    
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

def getALinks(html, url):
    links = []
    soup = BeautifulSoup(html, "html.parser")
    print(url)
    src = url
    try:
        src_title = soup.select_one('title').text    
    except:
        src_title = ""
    con = sqlite3.connect(DB_PATH)
    cursor = con.cursor()
    for a in soup.find_all("a"):
        try:
            href = a["href"]
        except:
            continue
        dst_text = a.text
        if len(dst_text) == 0:
            dst_text = ""
        if href.endswith(".onion") or ".onion/" in href:
            print(src, src_title, href, dst_text)
            cursor.execute("INSERT INTO OnionRelationiship values(?, ?, ?, ?)", \
                (src, src_title, href, dst_text))
            try:                
                cursor.execute("INSERT INTO CrawlerTarget values(?);", (href,))
            except Exception as e:
                print(e)
                pass
            links.append(href)
        time.sleep(1)
    con.commit()
    con.close()
    return links

def getHTML(url):
    print(url)
    while True:
        try:
            r = requests.get(url, proxies = PROXIES)
            r.close()
            time.sleep(1)
            break
        except:
            before_ip = getTorIp()
            torIpReset(before_ip)
            continue
    links = getALinks(r.content, url)
    print("\t", links)
    for link in links:
        while True:
            try:
                r_ = requests.get(link, proxies=PROXIES)
                r_.close()
                break
            except:
                before_ip = getTorIp()
                torIpReset(before_ip)
                continue
        links_ = getALinks(r_.content, link)
        
    file_name = url.split("?")[-1]
    fd = open(".\\html\\" + file_name + ".html", "wb")
    fd.write(r.content)
    fd.close()

def dbInit():
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
    con = sqlite3.connect(DB_PATH)
    print(DB_PATH)
    cursor = con.cursor()
    cursor.execute("CREATE TABLE CrawlerTarget(onion Text PRIMARY KEY);")
    cursor.execute("CREATE TABLE OnionRelationiship(src Text, src_title Text, dst Text, dst_text Text);")
    
    con.close()    
    return 

dbInit()
cat = 1 
while True:
    url = "https://onions.danwin1210.de/?cat=" + str(cat) + "&pg=0"
    getHTML(url)
    cat += 1
    if cat > 21:
        break