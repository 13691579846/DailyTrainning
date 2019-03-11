# 单线程
"""
import threading

def testThread1():
    print('i m thread 1')
def testThread2():
    print('i m thread 2')

def testThread3():
    print('i m thread 3')
# 自定义模拟多线程执行
def startThread(threadList):
    for th in threadList:
        th = threading.Thread(target=th())
        th.start()
if __name__=='__main__':
    # 单线程执行
    th = threading.Thread(target=testThread1())
    th.start()
    # 自定义模拟多线程执行
    startThread([testThread1,testThread2,testThread3])
"""
# 多线程执行
'''
其实python的并发并非绝对意义上的同时处理，因为启动线程是通过循环启动的，还是有先后顺序的
'''
"""
import threading
from datetime import datetime
import time
def test():
    print('我是一个线程函数 %s' %datetime.now())
    # time.sleep(2)
def th():
    thList = []
    for t in range(50):
        t = threading.Thread(target=test())
        thList.append(t)
    for t in thList:
        t.start()
if __name__=='__main__':
    th()
"""
'''
如果线程非常多这种差异会很明显，我们现在实现500个并发函数执行
'''

"""
import threading
from datetime import datetime

def test():
    print('我是一个线程函数{}'.format(datetime.now()))

def addtest():
    for i in range(20):
        test()
def th():
    thList = []
    for i in range(25):
        th = threading.Thread(target=addtest())
        thList.append(th)
    for th in thList:
        th.start()
if __name__=='__main__':
    th()
"""
# 守护线程：为了 主线程结束 使子线程也跟着结束
"""
import threading
from datetime import datetime
import time
def test():
    time.sleep(10)
    print('我是一个线程函数{}'.format(datetime.now()))

def th():
    thlist = []
    for i in range(20):
        th = threading.Thread(target=test())
        th.setDaemon(True)  # 设置每一个子线程都为守护进程
        thlist.append(th)
        
    for th in thlist:
        th.start()
if __name__ == '__main__':
    th()
    print('主线程执行结束')
"""
# 线程等待/阻塞线程

import threading
from datetime import datetime
import time

def test():
    time.sleep(1)
    print('我是一个线程函数', datetime.now())

def th():
    thlist = []
    for i in range(10):
        th = threading.Thread(target=test(), name=str(i))
        th.setDaemon(True)
        thlist.append(th)

    for th in thlist:
        th.start()
    for th in thlist:
        th.join(2)
if __name__=='__main__':
    th()
    print('主线程结束')