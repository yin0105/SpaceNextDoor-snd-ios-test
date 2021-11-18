# ---***--- coding = utf-8 ---***---
# @Time : 2021/7/26 14:55
# @Author: Paco

from appium import webdriver
from Common import operateElements


class BaseProject():
    # configurations
    testPhone = "97777777"
    params = {
        "platformName": "iOS",
        "platformVersion": "14.5",
        "deviceName": "iPhone 12",
        "app": "com.spacenextdoor"
    }

    # 访问路径
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", params)
    el = operateElements

    def loading(self):
        self.driver.implicitly_wait(10)
