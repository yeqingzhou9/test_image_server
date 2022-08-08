import os.path
import sys
import time
import unittest
from HTMLTestRunner import HTMLTestRunner

import testImageMain


def createsuite():
    # suit=unittest.TestSuite()
    # suit.addTest(unittest.makeSuite(testImage.ImageTest))
    # return suit

    discover = unittest.defaultTestLoader.discover('../test_image_server', pattern='test*.py', top_level_dir = None)
    print(discover)
    return discover

if __name__ == '__main__':
    # suite=createsuite()
    # runner=unittest.TextTestRunner(verbosity=2)
    # runner.run(suite)

    curpath=sys.path[0]
    # 取当前时间，解决重复命名的问题
    now=time.strftime("%Y-%m-%d-%H %M %S",time.localtime(time.time()))
    # 创建一个存放HTML报告的文件夹
    if not os.path.exists(curpath+'/resultreport'):
        os.makedirs(curpath+'/resultreport')

    filename=curpath+'/resultreport/'+now+'resultreport.html'
    with open(filename,'wb') as fp:
        # 出html报告
        runner=HTMLTestRunner(stream=fp, title=u'测试报告', description=u'用例执行情况', verbosity=2)
        suite=createsuite()
        runner.run(suite)