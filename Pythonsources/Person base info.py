#coding=utf-8
from appium import webdriver
import time,unittest,os
import EBC_Emulator_Data

class person_info(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        EBC_Emulator_Data.CSH_data()
        EBC_Emulator_Data.driver
        EBC_Emulator_Data.driver.implicitly_wait(10)
#        EBC_Emulator_Data.Login_userA()

    @classmethod
    def tearDownClass(cls):
        EBC_Emulator_Data.CSH_clear_data()

    def test_PersonBaseInfo(self):
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/index_item_rb_4").click()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/layout_edit").click()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/et_user_name").clear()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/et_user_name").send_keys(u"火枪")
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/tv_gender").click()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/btn_item2").click()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/tv_phone").clear()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/et_user_name").send_keys("13687654321")
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/et_id_info").clear()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/et_id_info").send_keys("431381198109106573")
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/iv_return").click()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/layout_edit").click()
        self.assertEqual(EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/et_user_name").text,u"火枪","Fail - 修改用户名失败。")
        self.assertEqual(EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/tv_gender").text,u"女","Fail - 修改姓别失败。")
        self.assertEqual(EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/tv_phone").text,u"13687654321","Fail - 修改手机失败。")
        self.assertEqual(EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/et_id_info").text,u"431381198109106573","Fail - 修改身份证失败。")
        #修改回初始状态
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/et_user_name").clear()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/et_user_name").send_keys(u"巨魔")
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/tv_gender").click()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/btn_item2").click()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/tv_phone").clear()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/et_user_name").send_keys("13612345678")
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/et_id_info").clear()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/et_id_info").send_keys("431381198809122734")
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/iv_return").click()

    def test_ChangesPW(self):
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/index_item_rb_4").click()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/layout_edit").click()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/btn_change_password").click()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/et_origin_password").send_keys("123456")
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/et_new_password").send_keys("654321")
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/et_re_new_password").send_keys("654321")
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/btn_submit").click()
        #退出登录
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/btn_logout").click()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/tv_click_login").click()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/et_user_name").send_keys("13612345678")
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/et_password").send_keys("654321")
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/btn_login").click()
        self.assertEqual(EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/tv_mobile").text,u"13612345678","Fail-登录失败，个人中心里无此用户")
        #改回到初始密码
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/layout_edit").click()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/btn_change_password").click()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/et_origin_password").send_keys("654321")
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/et_new_password").send_keys("123456")
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/et_re_new_password").send_keys("123456")
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/btn_submit").click()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/iv_return").click()

    def test_PreferencesNavigation(self):
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/index_item_rb_4").click()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/layout_edit").click()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/rl_navigation_software").click()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/ll_navi_soft_set").click()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/tv_item1").click()
        self.assertEqual(EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/tv_navi_software").text,u"内置地图","Fail - 内置地图没有被启用。")
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/ll_navi_soft_set").click()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/tv_item2").click()
        self.assertEqual(EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/tv_navi_software").text,u"百度地图","Fail - 内置地图没有被启用。")
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/ll_navi_soft_set").click()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/tv_item3").click()
        self.assertEqual(EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/tv_navi_software").text,u"高德地图","Fail - 内置地图没有被启用。")
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/iv_return").click()

    def test_PreferencesLocation(self):
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/index_item_rb_4").click()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/layout_edit").click()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/rl_navigation_software").click()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/ll_home_site").click()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/et_select_condition").send_keys(u"腾讯众创空间")
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/iv_find").click()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/tv_site_name").click()
        self.assertEqual(EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/tv_home_site").text,u"腾讯众创空间","Fail - 设置家的位置未见效。")
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/ll_company_site").click()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/et_select_condition").send_keys(u"七里香榭")
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/iv_find").click()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/tv_site_name").click()
        self.assertEqual(EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/tv_home_site").text,u"七里香榭","Fail - 设置公司的位置未见效。")
        #改回到初始数据
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/ll_home_site").click()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/et_select_condition").send_keys(u"永通商邸")
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/iv_find").click()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/tv_site_name").click()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/ll_company_site").click()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/et_select_condition").send_keys(u"中海国际社区2")
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/iv_find").click()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/tv_site_name").click()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/iv_return").click()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/iv_return").click()
        


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(person_info)
    unittest.TextTestRunner(verbosity=2).run(suite)



