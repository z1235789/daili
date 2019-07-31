import urllib.request
import random

url = 'http://www.whatismyip.com.tw'

ip_list = ['39.137.69.6:80',
           '212.64.51.13:8888',
           '39.137.69.7:80',
           '101.231.104.82:80',
           '106.14.82.38:8080',
           '36.25.243.50:80']

proxy_support = urllib.request.ProxyHandler({'http':'random.choice(ip_list)'})

opener = urllib.request.build_opener(proxy_support)
opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36')]

urllib.request.install_opener(opener)

response = urllib.request.urlopen(url)
html = response.read().decode('utf-8')

print(html)
