import requests
proxies = {
    'http' : 'socks5h://127.0.0.1:9150',
    'https' : 'socks5h://127.0.0.1:9150'
}
#response = requests.get('http://5mct7rdyskl7gthnq66yy3owg4cozrqvzygyfit6ne4miwcjjjxshgqd.onion',
#                        proxies=proxies
#            )
response = requests.get("https://www.naver.com", proxies=proxies)
for line in response.content.decode("utf-8").split("\n"):
    print(line)