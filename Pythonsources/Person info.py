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
        EBC_Emulator_Data.Login_userA()

    @classmethod
    def tearDownClass(cls):
        EBC_Emulator_Data.CSH_clear_data()

    def test_PersonInfo_notification(self):
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/iv_push_message").click()
        self.assertTrue(EBC_Emulator_Data.driver.find_elements_by_id("com.sdwx.ebochong:id/tv_text"),"Fail - 通知列表为空，可能接口有问题。")
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/iv_return").click()

    def test_PersonInfo_balance(self):
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/layout_my_balance").click()
        self.assertNotEquals(EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/tv_balance").text,u"0.00桑叶"),"Fail - 桑叶为0，可能接口有问题。"

        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/rl_view_recharge_record").click()
        self.assertTrue(EBC_Emulator_Data.driver.find_elements_by_id("com.sdwx.ebochong:id/tv_deal_amount"),"Fail - 充值记录列表为空，可能接口有问题。")

        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/iv_return").click()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/rl_balance_recharge").click()
        self.assertTrue(EBC_Emulator_Data.driver.find_elements_by_id("com.sdwx.ebochong:id/tv_title_name"),"Fail- 没有进入余额充值页。")
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/iv_return").click()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/iv_return").click()

    def test_PersonInfo_order(self):
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/layout_my_order").click()
        self.assertTrue(EBC_Emulator_Data.driver.find_elements_by_id("com.sdwx.ebochong:id/tv_site_name"),"Fail - 订单列表为空，可能是接口有问题。")
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/iv_return").click()

    def test_PersonInfo_income(self):
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/layout_my_income").click()
        self.assertNotEqual(EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/tv_total_income").text,u"￥0.0元","Fail - 未提现收益为0元，可能借口有问题。")
        self.assertNotEqual(EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/tv_total_income1").text,u"￥0.0元","Fail - 总收益为0元，可能借口有问题。")
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/ll_income_record").click()
        self.assertTrue(EBC_Emulator_Data.driver.find_elements_by_id("com.sdwx.ebochong:id/tv_deal_amount"),"Fail - 收益记录列表为空，可能是接口有问题")
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/iv_return").click()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/ll_withdraw_record").click()
        self.assertTrue(EBC_Emulator_Data.driver.find_elements_by_id("com.sdwx.ebochong:id/tv_deal_amount"),"Fail - 提现记录列表为空，可能是接口有问题")
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/iv_return").click()
        self.assertEqual(EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/btn_withdraw").text,u"我要提现","Fail - 有未提现的收益，‘我要提现’按钮没有显示出来。")
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/iv_return").click()

    def test_PersonInfo_carinfo(self):
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/layout_my_car_info").click()
        self.assertEqual(EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/tv_no").text,u"您暂未添加任何车辆信息","Fail - 可能未进入车辆信息页。")
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/btn_add").click()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/et_license_plate").click()
        EBC_Emulator_Data.driver.press_keycode(29)
        EBC_Emulator_Data.driver.press_keycode(8)
        EBC_Emulator_Data.driver.press_keycode(10)
        EBC_Emulator_Data.driver.press_keycode(12)
        EBC_Emulator_Data.driver.press_keycode(14)
        EBC_Emulator_Data.driver.press_keycode(16)
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/rb_fuel_vechicle").click()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/btn_commit").click()
        self.assertEqual(EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/tv_license_plate").text,u"湘A13579","Fail - 我的车牌没有显示出来。")
        self.assertTrue(EBC_Emulator_Data.driver.find_elements_by_id("com.sdwx.ebochong:id/tv_default"),"Fail - 没有自动设置成默认车辆。")
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/tv_edit").click()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/tv_modify").click()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/rb_electric_vehicle").click()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/et_license_plate").click()
        EBC_Emulator_Data.driver.press_keycode(67)
        EBC_Emulator_Data.driver.press_keycode(7)
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/btn_commit").click()
        self.assertEqual(EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/tv_license_plate").text,u"湘A13570","Fail - 修改后的车牌没有显示出来。")
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/tv_del").click()
        EBC_Emulator_Data.driver.find_element_by_id("android:id/button1").click()
        EBC_Emulator_Data.driver.find_element_by_id("android:id/button1").click()
        self.assertEqual(EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/tv_no").text,u"您暂未添加任何车辆信息","Fail - 未成功删除车辆。")
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/iv_return").click()

    def test_PersonInfo_mychargingpile(self):
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/layout_electric_pipe_info").click()
        self.assertTrue(EBC_Emulator_Data.driver.find_elements_by_id("com.sdwx.ebochong:id/ib_cost_set"),"Fail - 没有分享的电桩显示出来。")
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/iv_is_open").click()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/ib_cost_set").click()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/save_set").click()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/iv_return").click()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/index_item_rb_1").click()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/rl_search").click()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/ll_home_site").click()
        self.assertEqual(EBC_Emulator_Data.driver.find_element_by_xpath("//android.widget.TextView[@text=\"YT006\"]").text,u"YT006","Fail - 没到找到该车位，共享失败。")
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/iv_return").click()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/ll_return").click()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/index_item_rb_4").click()
        #关闭共享充电桩
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/layout_electric_pipe_info").click()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/iv_is_open").click()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/iv_return").click()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/index_item_rb_1").click()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/rl_search").click()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/ll_home_site").click()
        self.assertFalse(EBC_Emulator_Data.driver.find_elements_by_xpath("//android.widget.TextView[@text=\"YT006\"]"),"Fail - 还能找到该电桩，关闭失败。")
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/iv_return").click()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/ll_return").click()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/index_item_rb_4").click()

    def test_PersonInfo_myparking(self):
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/layout_parking_info").click()
        self.assertTrue(EBC_Emulator_Data.driver.find_elements_by_id("com.sdwx.ebochong:id/tv_open_lock"),"Fail - 没有分享的车位显示出来。")
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/ll_cost_set").click()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/save_set").click()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/tv_share_park").click()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/iv_return").click()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/index_item_rb_1").click()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/rl_search").click()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/ll_home_site").click()
        time.sleep(5)
        EBC_Emulator_Data.driver.swipe(400,1800,400,1000,300)#往上滑动页面。
        time.sleep(3)
        self.assertEqual(EBC_Emulator_Data.driver.find_element_by_xpath("//android.widget.TextView[@text=\"YT005\"]").text,u"YT005","Fail - 没到找到该车位，共享失败。")
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/iv_return").click()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/ll_return").click()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/index_item_rb_4").click()
        #关闭共享车位
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/layout_parking_info").click()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/tv_share_park").click()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/iv_return").click()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/index_item_rb_1").click()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/rl_search").click()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/ll_home_site").click()
        time.sleep(5)
        EBC_Emulator_Data.driver.swipe(400,1800,400,1000,300)#往上滑动页面。
        time.sleep(3)
        self.assertFalse(EBC_Emulator_Data.driver.find_elements_by_xpath("//android.widget.TextView[@text=\"YT005\"]"),"Fail - 还能找到该车位，关闭失败。")
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/iv_return").click()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/ll_return").click()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/index_item_rb_4").click()

    def test_PersonInfo_applychargingpile(self):
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/layout_apply_cons_pipe").click()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/et_name").send_keys("1")
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/et_mobile").send_keys("1")
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/btn_commit").click()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/iv_return").click()

    def test_PersonInfo_applyparking(self):
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/layout_share_parking").click()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/et_address").send_keys("1")
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/et_name").send_keys("1")
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/et_mobile").send_keys("1")
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/btn_apply").click()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/iv_return").click()

    def test_PersonInfo_feedback(self):
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/layout_feedback").click()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/tv_content").send_keys(u"这是自动化测试。")
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/btn_commit").click()
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/iv_return").click()

    def test_PersonInfo_about(self):
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/layout_about_ebochong").click()
        self.assertTrue(EBC_Emulator_Data.driver.find_elements_by_id("com.sdwx.ebochong:id/tv_title_name"),"Fail - 没有打开关于易泊充的面板。")
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/iv_return").click()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(person_info)
    unittest.TextTestRunner(verbosity=2).run(suite)
