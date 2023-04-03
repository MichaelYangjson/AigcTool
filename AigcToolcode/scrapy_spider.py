from urllib import request

url = "http://httpbin.org/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763"}
req = request.Request(url=url, headers=headers)
res = request.urlopen(req)
html = res.read().decode("utf-8")
print(html)
