#代理--步骤
#参数是一个字典{'类型':'代理ip:端口号'}
#proxy_support = urllib.request.ProxyHandler({})
#定制、创建一个opener
#opener = urllib.request.build_opener(proxy_support)
#安装opener
#urllib.request.install_opener(opener)
#调用opener
#operner.open(url)

import urllib.request

url = 'http://www.whatismyip.com.tw'

proxy_support = urllib.request.ProxyHandler({'http':'183.146.213.56:80'})

opener = urllib.request.build_opener(proxy_support)

urllib.request.install_opener(opener)

response = urllib.request.urlopen(url)

html = response.read().decode('utf-8')

print(html)
