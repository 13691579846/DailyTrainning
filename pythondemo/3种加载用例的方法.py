import unittest

from selenium import webdriver

import HTMLTestRunner

class Baidu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
    def test_baidu(self):

        self.driver.get('http://www.baidu.com')
        title = self.driver.title
        self.assertEqual('百度一下，你就知道',title)
    def tearDown(self):
        self.driver.quit()
# 加载用例方式1
def suite1():
    tests = unittest.TestSuite()
    tests.addTest(Baidu('test_baidu'))
    return tests
# 加载用例方式2
def suite2():
    tests = unittest.makeSuite('Baidu')
    return tests
# 加载用例方式3
def suite3():
    discover = unittest.defaultTestLoader.discover('./','test_*.py')
    return discover
if __name__ == '__main__':
    # 运行方式1
    # unittest.main()
    # 运行方式2
    # runner = unittest.TestRunner()
    # runner.run(suite1())
    # # 运行方式3
    # runner = unittest.TestRunner()
    # runner.run(suite2())
    # # y运行方式4
    # runner = unittest.TestRunner()
    # runner.run(suite3())
    # 加载测试报告
    tests = unittest.TestSuite()
    tests.addTest(Baidu('test_baidu'))
    fr = open('./report1.html', 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fr, title='测试报告', description='详情')
    runner.run(tests)
    fr.close()