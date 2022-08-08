import os.path

from selenium import webdriver
import unittest
import time

from selenium.common import NoAlertPresentException
from selenium.webdriver.common.by import By


class ImageTestMain(unittest.TestCase):

    # 初始化环境
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://106.52.212.221:8080/java_image_server/")
        self.driver.maximize_window()

    # 清除环境
    def tearDown(self):
        self.driver.quit()

    # @unittest.skip("skipping")
    # 上传功能
    def test_upload(self):
        driver = self.driver
        # driver.find_element_by_class_name("am-form-field am-input-sm").send_keys(os.path.abspath("E:/test.jpg"))
        driver.find_element(by=By.XPATH, value="/html/body/div[1]/nav/div/form/div[1]/input").send_keys(os.path.abspath("E:/test.jpg"))
        # driver.find_element_by_class_name("am-form-field am-input-sm").click()
        driver.find_element(by=By.XPATH, value="/html/body/div[1]/nav/div/form/div[2]/input").click()
        time.sleep(5)
        # 如果重复，出现弹窗
        try:
            alert = driver.switch_to.alert
            alert.accept()
            time.sleep(5)
        # 不重复
        except:
            time.sleep(1)

    # @unittest.skip("skipping")
    # 删除功能
    def test_delete(self):
        driver=self.driver
        driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/figure/div/div[2]/button").click()
        time.sleep(5)
        alert=driver.switch_to.alert
        alert.accept()
        time.sleep(5)

    if __name__ == '__main__':
        unittest.main(verbosity=2)
