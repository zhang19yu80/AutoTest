import unittest, time
from mysql_action import mysqlclass
from get_somethings import *



class RegisterLoginLogout(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        #清理注册账号
        myconnect = mysqlclass('58.20.17.84', 3306, 'sdadmin', 'sdadmin', 'ebc_user')
        time.sleep(1)
        sql = "select * from ebc_user_info where mobile=13312345678"
        params = []
        try:
            userid = myconnect.select_one(sql)[1]
            params = [userid]
        except TypeError as e:
            print("空数据：", e)

        sql = "delete from ebc_user_info where user_account=%s"
        myconnect.delete(sql, params)

        sql = "delete from ebc_user_auth where user_account=%s"
        myconnect.delete(sql, params)

        myconnect = mysqlclass('58.20.17.84', 3306, 'sdadmin', 'sdadmin', 'ebc')
        time.sleep(1)
        sql = "delete from sd_account where user_account=%s"
        myconnect.delete(sql, params)

        sql = "delete from ebc_user where account=%s"
        myconnect.delete(sql, params)

        myconnect = mysqlclass('58.20.17.84', 3306, 'sdadmin', 'sdadmin', 'rent_car')
        time.sleep(1)
        sql = "delete from account where user_id=%s"
        myconnect.delete(sql, params)

        sql = "delete from user_info where user_account=%s"
        myconnect.delete(sql, params)

        sql = "delete from credit_score_record where user_account=%s"
        myconnect.delete(sql, params)





    def test_login(self):
        results = get_somethings().get_userinfo()
        json_res = requests[1]['code']
        response = results[0]
        self.assertEqual(response.status_code,200,"Fail-此API不通！")
        self.assertEqual(json_res['data']['id'],"ebc1468317275943","Fail-没有获得用户信息")

    def test_logout(self):
        jsessionid = get_somethings().get_jsessionid()
        url = "http://api.ebopay.cn/api_cloud/api/usersys/logout"
        header = {
            "Content-Type": "application/json",
            "jsessionid": jsessionid

        }
        response = requests.get(url,headers=header)
        json_res = response.json()
        self.assertEqual(response.status_code,200,"Fail-此API不通！")
        self.assertEqual(json_res['code'],1,"Fail-没有成功登出！")


    def test_register(self):
        #发送验证码
        url = "http://api.ebopay.cn/api_cloud/api/usersys/sendVerifyCode"
        header = {
            "Content-Type":"application/json"
        }
        data1 =  {"mobile":"13312345678","type":1}
        response = requests.post(url,data=json.dumps(data1),headers=header)
        time.sleep(5)

        #去web上查看验证码
        mobilephone = "13312345678"
        verifycode = getSMS_fromwebpage(mobilephone)

        #开始注册
        url = "http://api.ebopay.cn/api_cloud/api/usersys/register"
        header = {
            "Content-Type":"application/json"
        }
        data = {"mobile":mobilephone,"password":"123456","verifyCode":verifycode,"appCode":"ebcapp"}
        response = requests.post(url,data=json.dumps(data),headers=header)
        json_res = response.json()
        self.assertEqual(response.status_code,200,"Fail-此API不通！")
        self.assertEqual(json_res['code'],1,"Fail-没有成功注册")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(RegisterLoginLogout)
    unittest.TextTestRunner(verbosity=2).run(suite)