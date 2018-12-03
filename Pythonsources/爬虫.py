import urllib.request
import random

#####简单的#####
# # ua_headers 为了伪装浏览器, User-Agent 是爬虫与反爬虫斗争的第一步
# ua_headers = {
#         "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
# }
# #构造一个请求对象
# request = urllib.request.Request("http://www.baidu.com/", headers=ua_headers)
#
# #向指定的url发送请求，返回一个服务器响应文件对象
# response = urllib.request.urlopen(request)
#
# #读出这个对象然后转成字符串，并实例化它。
# html = response.read().decode()
#
# print("返回状态码：",response.getcode(),
#       "返回实际URL：",response.geturl(),
#       "返回信息：",response.info(),
#       html)

url = "http://www.baidu.com/"

UA_list = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Safari/68.0.3440.106 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) IE/68.0.3440.106 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/68.0.3440.106 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) 360/68.0.3440.106 Safari/537.36",
]

random_UA = random.choice(UA_list)

request1 = urllib.request.Request(url)

request1.add_header("User-Agent",UA_list)

print(request1.get_header("User-agent"))

response = urllib.request.urlopen(request1)

html = response.read().decode()

print(html)





