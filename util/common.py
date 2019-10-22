from faker import Faker
import pymysql,os
BASEPATH=os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
CASEPATH=os.path.join(BASEPATH,'cases')
DATAPATH=os.path.join(BASEPATH,'data')
REPORTPATH=os.path.join(BASEPATH,'report')
class get_data():
    fake = Faker(locale='zh_CN')
    def get_num(self, m, n):
        return self.fake.random_int(min=m, max=n)
    def get_string(self):
        return self.fake.sentence()[:-1]
    def get_add(self):
        return self.fake.province() + '-' + self.fake.city()
    def get_datetime(self):
        return self.fake.future_datetime()
    def get_name(self):
        return self.fake.name()
class get_connect():
    def con_mysql(self):
        try:
            self.con = pymysql.connect(host='localhost', user='root', password='root',
                                  database='learn', port=3306, charset='utf8')
        except:
            print('连接数据库失败')
        else:
            self.cur = self.con.cursor()
        return self.con, self.cur
    def execute_sql(self,sql):
        return self.cur.execute(sql)
    def close(self):
        self.cur.close()
        self.con.close()