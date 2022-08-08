import time
import unittest
from turtledemo.minimal_hanoi import play

from selenium import webdriver
from selenium.webdriver.common.by import By


class ImageTestOther(unittest.TestCase):

    # 初始化环境
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://106.52.212.221:8080/java_image_server/")
        self.driver.maximize_window()

    # 清除环境
    def tearDown(self):
        self.driver.quit()

    # @unittest.skip("skipping")
    # 查询图片详情
    def test_picture(self):
        driver = self.driver
        driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/figure/div/div[1]/img").click()
        time.sleep(5)
        driver.find_element(by=By.XPATH, value="/ html / body / div[2] / div[2] / a").click()
        time.sleep(5)

    if __name__ == '__main__':
        unittest.main(verbosity=2)