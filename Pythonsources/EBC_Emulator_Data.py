#coding=utf-8
from appium import webdriver
import time

#使用SDK模拟器进行自动化测试

def CSH_data():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '6.0'
    desired_caps['deviceName'] = 'Android Emulator'
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
    driver.find_element_by_id("com.sdwx.ebochong:id/btn_login").click()

#获得屏幕大小宽和高
def getSize(driver):
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x, y)

#屏幕向上滑动
def swipeUp(driver,t=300):
    l = getSize(driver)
    x1 = int(l[0] * 0.5)    #x坐标
    y1 = int(l[1] * 0.75)   #起始y坐标
    y2 = int(l[1] * 0.25)   #终点y坐标
    driver.swipe(x1, y1, x1, y2,t)

#屏幕向下滑动
def swipeDown(driver,t=300):
    l = getSize(driver)
    x1 = int(l[0] * 0.5)  #x坐标
    y1 = int(l[1] * 0.25)   #起始y坐标
    y2 = int(l[1] * 0.75)   #终点y坐标
    driver.swipe(x1, y1, x1, y2,t)
#屏幕向左滑动
def swipLeft(driver,t=300):
    l=getSize(driver)
    x1=int(l[0]*0.75)
    y1=int(l[1]*0.5)
    x2=int(l[0]*0.05)
    driver.swipe(x1,y1,x2,y1,t)
#屏幕向右滑动
def swipRight(driver,t=300):
    l=getSize(driver)
    x1=int(l[0]*0.05)
    y1=int(l[1]*0.5)
    x2=int(l[0]*0.75)
    driver.swipe(x1,y1,x2,y1,t)
