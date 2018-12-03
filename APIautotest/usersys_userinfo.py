import unittest,requests,json
from get_somethings import get_somethings


class userinfo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass


    def test_userinfo(self):
        jsessionid=get_somethings().get_jsessionid()
        url = "http://api.ebopay.cn/api_cloud/api/usersys/user/userInfo"
        header = {
            "Content-Type":"application/json",
            "jsessionid":jsessionid
        }
        response = requests.get(url,headers=header)
        json_res = response.json()
        self.assertEqual(response.status_code,200,"Fail-此API不通！")
        self.assertEqual(json_res['code'],1,"Fail-没有收到用户信息")

    def test_modify_user(self):
        jsessionid = get_somethings().get_jsessionid()
        url = "http://api.ebopay.cn/api_cloud/api/usersys/user/modifyUser"
        header = {
            "Content-Type": "application/json",
            "jsessionid": jsessionid
        }
        data = {"name":"张三","gender":"1","mobile":"13999999999","identityCard":"","alipay":"","appCode":"ebcapp"}
        response = requests.put(url, data=json.dumps(data), headers=header)
        json_res = response.json()
        self.assertEqual(response.status_code, 200, "Fail-此API不通！")
        self.assertEqual(json_res['code'], 1, "Fail-没有收到用户信息")



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase()
    unittest.TextTestRunner(verbosity=2).run(suite)