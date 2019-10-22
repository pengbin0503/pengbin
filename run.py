import unittest  # 导入单元测试框架
from jiekou.util.HTMLTestReportCN import HTMLTestRunner
from jiekou.util.common import CASEPATH,REPORTPATH,get_data
num=get_data().get_num(10,999)
# discover()方法，用于加载指定目录下所有以test开头的用例文件中的测试用例
tests = unittest.defaultTestLoader.discover(CASEPATH)
f = open(REPORTPATH+'/'+str(num) + '.html', 'wb')  # 以二进制写的方式打开文件test_result.html
runner = HTMLTestRunner(stream=f, title='接口自动化测试报告', tester='张三、李四、王五')
runner.run(tests)   # 执行测试
f.close()