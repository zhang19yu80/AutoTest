import unittest, requests, json


class SendSMS(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass


    def test_sendsms(self):
        url = "http://api.ebopay.cn/api_cloud/api/usersys/sendVerifyCode"
        header = {
            "Content-Type":"application/json"
        }
        data =  {"mobile":"13999992999","type":1}
        response = requests.post(url,data=json.dumps(data),headers=header)
        json_res = response.json()
        # print(response.json())
        # print(response.status_code)
        self.assertEqual(response.status_code,200,"Fail-此API不通！")
        self.assertEqual(json_res['msg'],"发送验证码成功","Fail-发送验证码!")



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SendSMS)
    unittest.TextTestRunner(verbosity=2).run(suite)