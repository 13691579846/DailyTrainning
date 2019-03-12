import requests

url = 'http://www.lemfix.com'
ret = requests.get(url)
print(ret)
print(ret.status_code)
print(ret.headers)
print(ret.cookies)

url = 'http://116.22.24.150:8080/futureloan/mvc/api/member/register'
# parm = {'mobilephone':'18688'}
ret = requests.get(url)
print(ret.status_code)
