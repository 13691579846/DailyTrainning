# 随机数模块
import random
'''
print(random.randint(1,10)) # 1-10随机取一个数
print(random.randrange(0,10,2)) # 1-10 随机生成一个偶数
print(random.choice(['1','2','4','5'])) # 集合中随机选择一个数
print(random.random()) # 随机生成0-1的一个浮点数
'''
# 生成6位随机验证码
'''
def randomCode():
    numList = []
    for i in range(6):
        status = random.randint(1,3)
        if status == 1:
            number = random.randint(0,9)
            numList.append(str(number))
        elif status == 2:
            zimuxiao = random.randint(65, 90)
            numList.append(chr(zimuxiao))
        else:
            zimuda = random.randint(97,122)
            numList.append(chr(zimuda))
    code =''.join(numList)
    return code
code = randomCode()
print(code)
'''
# 日期和时间模块
'''
from datetime import date, datetime, timedelta
now = date.today()
print(now) # 当前日期
print(now.year) # 年
print(now.month) # 月
print(now.day) # 日
print(now.isoweekday()) # 第几周
print(now+timedelta(days=1)) # 当前日期+1天
print(now-timedelta(days=1)) # 当前日期-1天
print(now+timedelta(days=7)) # 当前日期+1周
nowDate = datetime.now()
print(nowDate) # 当前日期时间
print(nowDate.date()) # 当前日期
print(nowDate.time()) # 当前时间
'''
# 数据加密模块

import hashlib

md5 = hashlib.md5(b'xiaochao11520')
password = md5.hexdigest()
print(password)