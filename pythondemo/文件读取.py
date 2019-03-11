# 读文件
"""
# 读取整个文件内容，文件指针在开头
'''
with open('常用模块.py', encoding='utf-8') as f:
    print(f.read())
'''
# 读全部内容 一行一行读 返回一个列表，文件指针在开头
'''
with open('常用模块.py', encoding='utf-8') as f:
    code = f.readlines()
    print(code)
# 读一行
'''
'''
# 读一行，文件指针在开头
with open('常用模块.py', encoding='utf-8') as f:
    code = f.readline()
    print(code)
'''
# 通过文件句柄读数据(推荐使用这种方式,防止数据量大，内存不够用)
'''
with open('常用模块.py', encoding='utf-8') as f:
    for code in f:
        print(code, end='')

'''
# 以r+（读写）模式读文件，文件指针在开头
with open('trainning.txt', 'r+', encoding='utf-8') as f:
    print(f.read())
    # f.write('test') # 可写

# 以rb模式读取文件，默认以二进制方式读，不能指定编码方式，指针在开头
with open('trainning.txt', 'rb') as f:
    print(f.read())
"""
# 写文件
"""
'''
# 以w（只读）模式写文件， 写入的文件内容会覆盖源文件的内用，指针在开头
with open('trainning.txt', 'w', encoding='utf-8') as f:
    f.write('trainning python')
    # print(f.read())# 报错，不可读
'''
# 以w+模式写文件，文件指针在开头覆盖原文内容
'''
with open('trainning.txt', 'w+',encoding='utf-8') as f:
    f.write('trainning text123小超')
'''
# 以wb的模式写文件
'''
with open('trainning.txt', 'wb') as f:
    f.write(b'xiaochao')
'''
# 以a+操作文件，文件指针在尾部
'''
with open('trainning.txt', 'a+',encoding='utf-8') as f:
    f.write('trainning text123小超')
'''

# 以r+写，操作指针在文件的开头，覆盖部分内容
'''
with open('trainning.txt', 'r+', encoding='utf-8') as f:
    f.write('123')
'''
"""
'''
# 读文件info.txt，将文件中的内容组合成字典，在追加到一个大列表中
def handleFile(filename):
    dicInfo={}
    iList=[]
    with open(filename, encoding='utf-8') as f:
        infoList = f.readlines()
        for info in infoList:
            info.strip(r'\n')
            l =info.split(',')
            for i in l:
                # :号分割， 分割一次
                dicInfo[i.split(':',1)[0]]=i.split(':',1)[1]
            iList.append(dicInfo)
    return iList
l = handleFile('./info')
print(l)
'''
