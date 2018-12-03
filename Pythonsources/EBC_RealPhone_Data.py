#coding=utf-8
from appium import webdriver
import time

#使用真机进行自动化测试

def CSH_data():
#    PATH=lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '6.0'
    desired_caps['deviceName'] = 'HUAWEI MT&-CL00'
    desired_caps['noSign'] = 'True'
#    desired_caps['app'] = PATH('C:\\Users\\zhangy\\Documents\\Tencent Files\\28766012\\FileRecv\\ebc_1117.apk')
    desired_caps['appPackage'] = 'com.sdwx.ebochong'
    desired_caps['appActivity'] = '.activity.MainActivity'
    desired_caps['unicodeKeyboard']=True
    desired_caps['resetKeyboard']=True
    return desired_caps

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',CSH_data())



def CSH_clear_data():
    driver.close_app()
    driver.quit()

def Login_userA():
    driver.find_element_by_id("com.sdwx.ebochong:id/index_item_rb_4").click()
    driver.find_element_by_id("com.sdwx.ebochong:id/tv_click_login").click()
    driver.find_element_by_id("com.sdwx.ebochong:id/et_user_name").send_keys("13612345678")
    driver.find_element_by_id("com.sdwx.ebochong:id/et_password").send_keys("123456")
    driver.press_keycode(111)
    driver.find_element_by_id("com.sdwx.ebochong:id/btn_login").click()
