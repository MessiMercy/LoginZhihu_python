from urllib import request, parse
from bs4 import BeautifulSoup
zhihuUrl = "http://www.zhihu.com/"
with request.urlopen(zhihuUrl) as res:
    data = res.read()
page = data.decode("utf-8")
bs = BeautifulSoup(page,"html.parser")
xsrf = bs.input["value"]
email = "XXXXX@qq.com"
password = "XXX"
remember_me = "true"

loginData = parse.urlencode([("_xsrf",xsrf),("email",email),("password",password),("remember_me",remember_me)])

req = request.Request("http://www.zhihu.com/login/email")
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req, data=loginData.encode("UTF-8")) as log:
    print("status code is:",log.status)
    for k, v in log.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', log.read().decode('utf-8'))