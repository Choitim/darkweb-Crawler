import requests

proxies = {
    'http' : 'socks5://127.0.0.1:9150',
    'https': 'socks://127.0.0.1:9150'
}

response = requests.get("http://ip-api.com/line", proxies=proxies)

for line in response.content.decode("utf-8").split("\n"):
    print(line)
