#coding=utf-8
import os
import time
import unittest
from appium import webdriver





'''
sum = 0
for i in range(101):
    sum = sum + i
print(sum)


for j in range(5):
   for i in range(10):
       if i < 5:
         print("输出：",i)
         continue  #跳出本次循环，满足上面的判断条件，则执行continue上面的语句，不满足条件，跳出循环，执行continue下面的语句
       print("打印：",i)
       if j > 3:
          print("计数：",j)
          break  #跳出这一层的循环


PATH=lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = 'HUAWEI MT&-CL00'
desired_caps['noSign'] = 'True'
desired_caps['app'] = PATH('C:\\Users\\zhangy\\Documents\\Tencent Files\\28766012\\FileRecv\\ebc_1117.apk')
#desired_caps['appPackage'] = 'com.sdwx.ebochong'
#desired_caps['appActivity'] = '.activity.MainActivity'
desired_caps['unicodeKeyboard']=True
desired_caps['resetKeyboard']=True

#如果设置的是app在电脑上的路径，则不需要配appPackage和appActivity，同理反之

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

driver.implicitly_wait(8)
driver.find_element_by_id("com.sdwx.ebochong:id/index_item_rb_4").click()
driver.find_element_by_id("com.sdwx.ebochong:id/tv_click_login").click()
driver.find_element_by_id("com.sdwx.ebochong:id/et_user_name").send_keys("13612345678")
driver.find_element_by_id("com.sdwx.ebochong:id/et_password").send_keys("123456")
driver.find_element_by_id("com.sdwx.ebochong:id/btn_login").click()

driver.quit()
'''
