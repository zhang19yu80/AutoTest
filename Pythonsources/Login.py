#coding=utf-8
from appium import webdriver
import time,unittest,os


class login_muile(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['appPackage'] = 'com.sdwx.ebochong'
        desired_caps['appActivity'] = '.activity.MainActivity'

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

        self.driver.implicitly_wait(20)
        

    def tearDown(self):
        self.driver.close_app()
        self.driver.quit()


    def test_password_incorrectly(self):
        self.driver.find_element_by_id("com.sdwx.ebochong:id/index_item_rb_4").click()
        try:
            self.driver.find_element_by_id("com.sdwx.ebochong:id/tv_mobile") != None

        except:
            self.driver.find_element_by_id("com.sdwx.ebochong:id/tv_click_login").click()


        else:
            self.driver.find_element_by_id("com.sdwx.ebochong:id/tv_mobile").click()
            self.driver.find_element_by_id("com.sdwx.ebochong:id/btn_logout").click()
            self.driver.find_element_by_id("com.sdwx.ebochong:id/tv_click_login").click()
        self.driver.find_element_by_id("com.sdwx.ebochong:id/et_user_name").send_keys("13612345678")
        self.driver.find_element_by_id("com.sdwx.ebochong:id/et_password").send_keys("123")
        self.driver.find_element_by_id("com.sdwx.ebochong:id/btn_login").click()
        self.assertTrue(self.driver.find_elements_by_id("com.sdwx.ebochong:id/btn_login"),"Fail-输入了错误的密码后应该停留在登录界面。")
        self.driver.find_element_by_id("com.sdwx.ebochong:id/iv_return").click()

    def test_username_incorrectly(self):
        self.driver.find_element_by_id("com.sdwx.ebochong:id/index_item_rb_4").click()
        try:
            self.driver.find_element_by_id("com.sdwx.ebochong:id/tv_mobile") != None

        except:
            self.driver.find_element_by_id("com.sdwx.ebochong:id/tv_click_login").click()

        else:
            self.driver.find_element_by_id("com.sdwx.ebochong:id/tv_mobile").click()
            self.driver.find_element_by_id("com.sdwx.ebochong:id/btn_logout").click()
            self.driver.find_element_by_id("com.sdwx.ebochong:id/tv_click_login").click()
        self.driver.find_element_by_id("com.sdwx.ebochong:id/et_user_name").send_keys("13612345679")
        self.driver.find_element_by_id("com.sdwx.ebochong:id/et_password").send_keys("123456")
        self.driver.find_element_by_id("com.sdwx.ebochong:id/btn_login").click()
        self.assertTrue(self.driver.find_elements_by_id("com.sdwx.ebochong:id/btn_login"),"Fail-输入了错误的用户名后应该停留在登录界面。")
        self.driver.find_element_by_id("com.sdwx.ebochong:id/iv_return").click()


    def test_login(self):
        self.driver.find_element_by_id("com.sdwx.ebochong:id/index_item_rb_4").click()
        try:
            self.driver.find_element_by_id("com.sdwx.ebochong:id/tv_mobile") != None

        except:
            self.driver.find_element_by_id("com.sdwx.ebochong:id/tv_click_login").click()

        else:
            self.driver.find_element_by_id("com.sdwx.ebochong:id/tv_mobile").click()
            self.driver.find_element_by_id("com.sdwx.ebochong:id/btn_logout").click()
            self.driver.find_element_by_id("com.sdwx.ebochong:id/tv_click_login").click()
        self.driver.find_element_by_id("com.sdwx.ebochong:id/et_user_name").send_keys("13612345678")
        self.driver.find_element_by_id("com.sdwx.ebochong:id/et_password").send_keys("123456")
        self.driver.find_element_by_id("com.sdwx.ebochong:id/btn_login").click()
   
        self.assertEqual(self.driver.find_element_by_id("com.sdwx.ebochong:id/tv_mobile").text,u"13612345678","Fail-登录失败，个人中心里无此用户")
        self.driver.find_element_by_id("com.sdwx.ebochong:id/iv_return").click()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(login_muile)
    unittest.TextTestRunner(verbosity=2).run(suite)
