from urllib import request, parse
import json,


url = "http://api.ebopay.cn:8001/message/list"
header = {
    "Host":"api.ebopay.cn:8001",
    "Connection":"keep-alive",
    # "Content-Length":"28",
    #Upgrade-Insecure-Requests: 1
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Referer":"http://api.ebopay.cn:8001/",
    "Accept-Language":"zh-CN,zh;q=0.9",
    "Cookie":"rememberMe=9zAMbYEL+ijIFYV9JhS26F+7FKxUnlzY+i0c+n7yeVZiyIeE6vk17rLj9EPH6HnONrgYbM356RUsscjyecgkZksWy3yb54oxyEevGwjnjY22zh9iOV31/SnmaZaBFGq4PIc32ZZDHwPwDyvseefPiMS5bl1T2hF3mmmoag/qn7i9W2kupUrhitmfoNOGT7mEFgfxfTxvaTEMk94EMLUy0x9LQ/GTazKD2lDOYSV6bdgdc/2z++hD936vwf3fISG3wL0MYBKvppiWIwRG742ojm7vnZL8OmKb1gjdhi5Id9KFmIe/YoB3qngU3MN5eQIxO9yTwT1bqYSvpTHiHMNwb0i9LWSANZxBOv+QeCd9/nwVyb8LOttUXM7pMnF1J0bmboMcly4/APhu/4MCjbd1jAwr37MnS3MBMND11R+boH3dEeYHrsyvBu9r3UkrGNnImu3TFhH1Eo8FF3agXgg4fmJE/j8SKki/mwiRKLRiCgZbXSatry+vPM4KTBYsRHS8r/c9w3R88kubMWisidTQOZ8EjAiALFSkFPhdp9bLGNNaNSoi6BBmsUx1B0ElybIgdaJJL2r05MSvJDabRiu6fMjDOkaecXgfux1BNIRPYYM7yeRcAxwZZoxxxWdUGx9chUlWl2AjR9eaxGzklqzNIk0gNsooVraffXBTazzjVnEYRV1rt/xhRRsLq81drEhP9zABgvm4VWJsuME+4/8qXvXx/BMyi1qKUbyNzzceigETxNvhhYJloGADIdCRLbOs2ofuHk4OVmAqklWU7O5uszAnHrKMWd2kReMLoKx8NtxWxMO+MIg+KFHpi8jKcqU0WaQys1nAOcvuhczgbWEYPJC/6MmhtvCPQM72sXCPsJB+fVNYW3iELz3pKlSmPgSWQ8avbtXcimhD49v9lgrBjE2aIerVaaabjeeF/agaW5OjjkBPQYuLXRWywgdowNIw2LavlFgg7d8pIsAdi0be4FfI5aDHzGJwgtgqt8z4Mxe557fzNNS6kmavQmFKJsJUcZA+uRS14Q+UPSMyIN8pZqn3XPn2r7aXW7GGLUuQISOysWTCAzgvd8EVMFmWBHLc; shiroCookie=1dae0f6b-825a-43ad-9447-6919ab1558f2",
    #Accept-Encoding: gzip, deflate
}

formdata = {
    "order":"desc",
    "offset":"0",
    "limit":"9"
}
formdata1 = parse.urlencode(formdata).encode()
request1 = request.Request(url,data=formdata1,headers=header)

response = request.urlopen(request1)

html = response.read().decode()
# print(type(html),html,"---------------------------")
html1= json.loads(html)
# print(type(html1),html1)
verifycode = html1["rows"]
verifycode.reverse()
# print(verifycode)
iwant_dict = None
for i in verifycode:
    if i['mobile'] == '134****3009':
        iwant_dict = i

if iwant_dict == None:
    print('没找到')
else:
    print(iwant_dict['validateCode'])





