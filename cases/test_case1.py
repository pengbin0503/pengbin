import unittest
import requests
from jiekou.util.common import get_data,get_connect
connect=get_connect()
class TestAdd(unittest.TestCase):
    def setUp(self):
        connect.con_mysql()
        self.url1='http://127.0.0.1:8000/api/add_event/'
        self.url2='http://127.0.0.1:8000/api/add_guest/'
    def tearDown(self):
        connect.close()
    def testcase01(self):
        g = get_data()
        self.data = {}
        self.data['eid'] = g.get_num(2001, 9999)
        self.data['name'] = '小米' + str(g.get_num(10, 999)) + '发布会'
        self.data['status'] = g.get_num(0, 1)
        self.data['limit'] = g.get_num(1, 1000)
        self.data['address'] = g.get_add()
        self.data['start_time'] = g.get_datetime()
        r = requests.post(self.url1, self.data)
        res = r.json()
        print(res)
        #self.con, cur = connect.con_mysql()
        sql = 'select * from sign_event where id="%d" and name="%s";'
        select_result = connect.execute_sql(sql  %(self.data['eid'], self.data['name']))
        try:
            self.assertEqual(res['status'],10000)
            self.assertEqual(res['message'],'add event success')
            self.assertEqual(select_result,1)
        except:
            raise Exception
        # if res['status'] == 10000 and res['message'] == 'add event success' and select_result == 1:
        #     print('pass')
        # else:
        #     print('fail')
    def testcase02(self):
        g = get_data()
        self.data = {}
        self.data['eid'] = 1001
        self.data['realname'] = g.get_name()
        self.data['email'] = str(g.get_num(10000, 99999))+'@163.com'
        self.data['phone'] = str(13)+str(g.get_num(000000000, 999999999))
        r = requests.post(self.url2, self.data)
        res = r.json()
        print(res)
        #self.con, cur = connect.con_mysql()
        sql = 'select * from sign_guest where realname="%s";'
        select_result = connect.execute_sql(sql  %(self.data['realname']))
        try:
            self.assertEqual(res['status'],10000)
            self.assertEqual(res['message'],'add guest success')
            self.assertEqual(select_result,1)
            #res['status'] == 10000 and res['message'] == 'add guest success' and select_result == 1:
            #print('pass')
        except:
            raise Exception
            #print('fail')
    def testcase03(self):
        g = get_data()
        self.data = {}
        self.data['eid'] = 1001
        self.data['realname'] = g.get_name()
        self.data['email'] = str(g.get_num(10000, 99999)) + '@163.com'
        self.data['phone'] = str(15) + str(g.get_num(000000000, 999999999))
        r = requests.post(self.url2, self.data)
        res = r.json()
        print(res)
        # self.con, cur = connect.con_mysql()
        sql = 'select * from sign_guest where realname="%s";'
        select_result = connect.execute_sql(sql % (self.data['realname']))
        try:
            self.assertEqual(res['status'],10000)
            self.assertEqual(res['message'],'add guest success')
            self.assertEqual(select_result,1)
        except:
            raise Exception
        #if res['status'] == 10000 and res['message'] == 'add guest success' and select_result == 1:
         #   print('pass')
        #else:
         #   print('fail')
    def testcase04(self):
        g = get_data()
        self.data = {}
        self.data['eid'] = 1001
        self.data['realname'] = g.get_name()
        self.data['email'] = str(g.get_num(10000, 99999)) + '@163.com'
        self.data['phone'] = str(17) + str(g.get_num(000000000, 999999999))
        r = requests.post(self.url2, self.data)
        res = r.json()
        print(res)
        # self.con, cur = connect.con_mysql()
        sql = 'select * from sign_guest where realname="%s";'
        select_result = connect.execute_sql(sql % (self.data['realname']))
        try:
            self.assertEqual(res['status'],10000)
            self.assertEqual(res['message'],'add guest success')
            self.assertEqual(select_result,1)
        except:
            raise Exception
        # if res['status'] == 10000 and res['message'] == 'add guest success' and select_result == 1:
        #     print('pass')
        # else:
        #     print('fail')
    def testcase05(self):
        g = get_data()
        self.data = {}
        self.data['eid'] = 1001
        self.data['realname'] = g.get_name()
        self.data['email'] = str(g.get_num(10000, 99999)) + '@163.com'
        self.data['phone'] = str(18) + str(g.get_num(000000000, 999999999))
        r = requests.post(self.url2, self.data)
        res = r.json()
        print(res)
        # self.con, cur = connect.con_mysql()
        sql = 'select * from sign_guest where realname="%s";'
        select_result = connect.execute_sql(sql % (self.data['realname']))
        try:
            self.assertEqual(res['status'],10000)
            self.assertEqual(res['message'],'add guest success')
            self.assertEqual(select_result,1)
        except:
            raise Exception
        # if res['status'] == 10000 and res['message'] == 'add guest success' and select_result == 1:
        #     print('pass')
        # else:
        #     print('fail')
    def testcase06(self):
        g = get_data()
        self.data = {}
        self.data['eid'] = 1001
        self.data['realname'] = g.get_name()
        self.data['email'] = str(g.get_num(10000, 99999)) + '@163.com'
        self.data['phone'] = str(19) + str(g.get_num(000000000, 999999999))
        r = requests.post(self.url2, self.data)
        res = r.json()
        print(res)
        # self.con, cur = connect.con_mysql()
        sql = 'select * from sign_guest where realname="%s";'
        select_result = connect.execute_sql(sql % (self.data['realname']))
        try:
            self.assertEqual(res['status'],10000)
            self.assertEqual(res['message'],'add guest success')
            self.assertEqual(select_result,1)
        except:
            raise Exception
        # if res['status'] == 10000 and res['message'] == 'add guest success' and select_result == 1:
        #     print('pass')
        # else:
        #     print('fail')
    def testcase07(self):
        g = get_data()
        self.data = {}
        self.data['eid'] = 1001
        self.data['realname'] = g.get_name()
        self.data['email'] = str(g.get_num(10000, 99999)) + '@163.com'
        self.data['phone'] = str(12) + str(g.get_num(000000000, 999999999))
        r = requests.post(self.url2, self.data)
        res = r.json()
        print(res)
        # self.con, cur = connect.con_mysql()
        sql = 'select * from sign_guest where realname="%s";'
        select_result = connect.execute_sql(sql % (self.data['realname']))
        try:
            self.assertEqual(res['status'],10027)
            self.assertEqual(res['message'],'phone error')
            self.assertEqual(select_result,0)
        except:
            raise Exception
        # if res['status'] == 10027 and res['message'] == 'phone error' and select_result==0:
        #     print('pass')
        # else:
        #     print('fail')
    def testcase08(self):
        g = get_data()
        self.data = {}
        self.data['eid'] = 1001
        self.data['realname'] = g.get_name()
        self.data['email'] = str(g.get_num(10000, 99999)) + '@163.com'
        self.data['phone'] = str(21) + str(g.get_num(000000000, 999999999))
        r = requests.post(self.url2, self.data)
        res = r.json()
        print(res)
        # self.con, cur = connect.con_mysql()
        sql = 'select * from sign_guest where realname="%s";'
        select_result = connect.execute_sql(sql % (self.data['realname']))
        try:
            self.assertEqual(res['status'],10027)
            self.assertEqual(res['message'],'phone error')
            self.assertEqual(select_result,0)
        except:
            raise Exception
        # if res['status'] == 10027 and res['message'] == 'phone error' and select_result == 0:
        #     print('pass')
        # else:
        #     print('fail')

if __name__=='__main__':
    unittest.main()
