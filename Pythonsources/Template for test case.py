#coding=utf-8
from appium import webdriver
import time,unittest,os
import EBC_Emulator_Data

class person_info(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        EBC_Emulator_Data.CSH_data()
        EBC_Emulator_Data.driver
        EBC_Emulator_Data.driver.implicitly_wait(15)
#        EBC_Emulator_Data.Login_userA()

    @classmethod
    def tearDownClass(cls):
        EBC_Emulator_Data.CSH_clear_data()

    def test_PersonInfo_carinfo(self):
        EBC_Emulator_Data.driver.find_element_by_id("com.sdwx.ebochong:id/index_item_rb_4").click()
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


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(person_info)
    unittest.TextTestRunner(verbosity=2).run(suite)
