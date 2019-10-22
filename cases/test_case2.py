import unittest
import requests
from jiekou.util.common import get_connect
connect=get_connect()
class TestLogin(unittest.TestCase):
    def setUp(self):
        connect.con_mysql()
        self.data = {}
        self.data['eid'] = 1001
        self.url = 'http://127.0.0.1:8000/api/sec_get_event_list/'
        self.a=requests.get(self.url,self.data,auth=('pengbin','pengbin900503'))
    def tearDown(self):
        connect.close()
    def testcase03(self):
        sql='select * from sign_event where id=1001;'
        select_result = connect.execute_sql(sql)
        res = self.a.json()
        print(res)
        try:
            self.assertEqual(res['status'],200)
            self.assertEqual(res['message'],'success')
            self.assertEqual(select_result,1)
            #res['status'] == 200 and res['message'] == 'success'and select_result==1
            #print('pass')
        except:
            raise Exception
            #print('fail')
if __name__=='__main__':
    unittest.main()