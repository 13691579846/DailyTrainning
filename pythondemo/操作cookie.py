from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get('https://www.cnblogs.com/')
# login = driver.find_element_by_xpath("//span[@id='span_userinfo']/a[0]")
login = driver.find_element_by_link_text('登录')
login.click()
time.sleep(2)
# username = driver.find_element_by_id('input1')
# password = driver.find_element_by_id('input2')
# username.send_keys('13691579846')
# password.send_keys('xiaochao11520!@#')
# time.sleep(10)
# print(driver.get_cookies())
cookies = [{'name': '_gat', 'value': '1', 'path': '/', 'domain': '.cnblogs.com', 'secure': False, 'httpOnly': False, 'expiry': 1551875599}, {'name': '.CNBlogsCookie', 'value': 'DC6031258A7577CE83B48B9F0276C77E669806F588065A076A610A091915A1BCBD78173567043FDFE2DE48F34E404CBC0902ABFFFB6D0D6DF296649E10AD87EF05373CC69CF6BA02C6AFDAD7B9962DEC2BD672C2844AB68EC0EEB9D3316A59B107C73025', 'path': '/', 'domain': '.cnblogs.com', 'secure': False, 'httpOnly': True}, {'name': '.Cnblogs.AspNetCore.Cookies', 'value': 'CfDJ8JcopKY7yQlPr3eegllP76PFWctaI2hg0aWnmAEXgvNiBImmz1Wul2y3sycg6E745rsFAD_jyHF5tkhUOmp1Gru0xKOh6y7P5FOcyDG0_2u8nSzgLtfWEQ4V5gHryHctO4aT0-TtPqxmKaap4U4wescgKYsTim9WHi35Au5_10Bu30dedVMeAV_w3L16zND4dFe6TjspL8K2Q16xFXEPugH-d4bx-VZMwna4rH1bzwDGdG27iz4ZP0kcts2MrkLZHS3qIS46P8pfxs2IW5dygDT6w2kf7tuAEtonXge39_BA', 'path': '/', 'domain': '.cnblogs.com', 'secure': False, 'httpOnly': True}, {'name': '_ga', 'value': 'GA1.2.788115623.1551875540', 'path': '/', 'domain': '.cnblogs.com', 'secure': False, 'httpOnly': False, 'expiry': 1614947549}, {'name': '_gid', 'value': 'GA1.2.1588511830.1551875540', 'path': '/', 'domain': '.cnblogs.com', 'secure': False, 'httpOnly': False, 'expiry': 1551961949}, {'name': '__gads', 'value': 'ID=5b931e45966a257e:T=1551875549:S=ALNI_MZqaBmycRHN-v6WI9l3NMi1Qj5oFA', 'path': '/', 'domain': '.cnblogs.com', 'secure': False, 'httpOnly': False, 'expiry': 1614947549}]
for cookie in cookies:
    driver.add_cookie(cookie)
time.sleep(3)
driver.get('https://www.cnblogs.com')
import requests
#
# testUrl = 'http://www.163.com'
# respsone = requests.get(testUrl) # 发送get请求
# print(respsone.status_code) # 获取状态码
# print(respsone.headers) # 获取返回结果的头部信息
# print(respsone.cookies) #
# print(respsone.text) # 获取返回结果的内容
#
# cookie163 = {'JSESSIONID':'232713510BCCC33C58DE11CF3E89E2B1'}
# testUrl = r'https://mail.163.com/js6/main.jsp?sid=rBoIvXmSOxKjttYgJISSoKHOKJScRTuZ&df=mail163_letter#module=welcome.WelcomeModule%7C%7B%7D'
# respsone = requests.get(testUrl, cookies = cookie163)
# print(respsone.status_code)
# print(respsone.headers)
# print(respsone.text)
