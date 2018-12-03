#coding=utf-8
from appium import webdriver
import unittest
import time
import os

#PATH=lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))

class LoginAndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'Android Emulator'
        #desired_caps['app'] = PATH('C:\\Users\\LENOVO\\Desktop\\StarZone_V2.0.0.apk')　
        desired_caps['appPackage'] = 'com.sdwx.ebochong'
        desired_caps['appActivity'] = '.activity.MainActivity'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
        self.driver.implicitly_wait(20)

    def tearDown(self):
        self.driver.quit()
        self.driver.close_app()

    def test_incorrect_username(self):
        self.driver.find_element_by_id("com.sdwx.ebochong:id/index_item_rb_4").click()
        self.driver.find_element_by_id("com.sdwx.ebochong:id/tv_click_login").click()
        self.driver.find_element_by_id("com.sdwx.ebochong:id/et_user_name").send_keys("13612345679")
        self.driver.find_element_by_id("com.sdwx.ebochong:id/et_password").send_keys("123456")
        self.driver.find_element_by_id("com.sdwx.ebochong:id/btn_login").click()
        self.assertTrue(self.driver.find_element_by_id("com.sdwx.ebochong:id/btn_login").is_enabled(), "Fail - 输入不正确用户名后应该仍在登陆页面。")

    def test_incorrect_password(self):
        self.driver.find_element_by_id("com.sdwx.ebochong:id/index_item_rb_4").click()
        self.driver.find_element_by_id("com.sdwx.ebochong:id/tv_click_login").click()
        self.driver.find_element_by_id("com.sdwx.ebochong:id/et_user_name").send_keys("13612345678")
        self.driver.find_element_by_id("com.sdwx.ebochong:id/et_password").send_keys("123457")
        self.driver.find_element_by_id("com.sdwx.ebochong:id/btn_login").click()
        self.assertTrue(self.driver.find_element_by_id("com.sdwx.ebochong:id/btn_login").is_enabled(),"Fail - 输入不正确密码后应该仍在登陆页面。")



    def test_login(self):
        self.driver.find_element_by_id("com.sdwx.ebochong:id/index_item_rb_4").click()
        self.driver.find_element_by_id("com.sdwx.ebochong:id/iv_return").click()
        self.driver.find_element_by_id("com.sdwx.ebochong:id/tv_click_login").click()
        self.driver.find_element_by_id("com.sdwx.ebochong:id/et_user_name").send_keys("13612345678")
        self.driver.find_element_by_id("com.sdwx.ebochong:id/et_password").send_keys("123456")
        self.driver.find_element_by_id("com.sdwx.ebochong:id/btn_login").click()
        self.assertEqual(self.driver.find_element_by_id("com.sdwx.ebochong:id/tv_mobile").text,u"13612345678","Fail - 登陆账号与已登陆账号不匹配。")




if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(LoginAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
