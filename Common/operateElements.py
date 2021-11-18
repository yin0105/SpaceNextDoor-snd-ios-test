# ---***--- coding = utf-8 ---***---
# @Time : 2021/7/26 14:05
# @Author: Paco

# -*- coding: utf-8 -*-
from selenium.webdriver.support.ui import WebDriverWait
import selenium.common.exceptions
import time
from Common.variables import GetVariable as Common
from Common import errorLogs


# 此脚本主要用于查找元素是否存在，操作页面元素
class OperateElement():
    def __init__(self, driver=""):
        self.driver = driver

    def findElement(self, mOperate):
        '''
        查找元素.mOperate是字典
        operate_type：对应的操作
        element_info：元素详情
        find_type: find类型
        '''
        try:
            WebDriverWait(self.driver, Common.WAIT_TIME).until(lambda x: elements_by(mOperate, self.driver))
            return True
        except selenium.Common.exceptions.TimeoutException:
            return False
        except selenium.Common.exceptions.NoSuchElementException:
            print("找不到数据")
            return False

    def operate_element(self, mOperate):
        if self.findElement(mOperate):
            elements = {
                Common.CLICK: lambda: operate_click(mOperate, self.driver),
                # GetVariable.TAP: lambda: operate_tap(mOperate["find_type"], self.driver,  mOperate["element_info"], arg),
                Common.SEND_KEYS: lambda: send_keys(mOperate, self.driver),
                Common.SWIPELEFT: lambda: swipe_left(mOperate, self.driver),
                Common.SEND_CODE: lambda: send_code()
            }
            return elements[mOperate["operate_type"]]()
        return False

# 如果要输入验证码，暂停10秒钟，手动去输入
def sendCodeWithInputByManual():
    time.sleep(10)

# 点击事件
def operate_click(mOperate, cts):
    if mOperate["find_type"] == Common.find_element_by_id or mOperate["find_type"] == Common.find_element_by_name or \
            mOperate["find_type"] == Common.find_element_by_xpath:
        elements_by(mOperate, cts).click()
    if mOperate["find_type"] == Common.find_elements_by_id or mOperate["find_type"] == Common.find_elements_by_name:
        elements_by(mOperate, cts)[mOperate["index"]].click()
    # 记录运行过程中的一些系统日志，比如闪退会造成自动化测试停止
    if Common.SELENIUM_APPIUM == Common.APPIUM:
        # errorLog.get_error(log=mOperate["log"], devices=mOperate["devices"])
        pass

# 向上滑动
def swipe_up(driver, t=500, n=1):
    s = driver.get_window_size()
    x1 = s['width'] * 0.5  # x坐标
    y1 = s['height'] * 0.75  # 起点y坐标
    y2 = s['height'] * 0.25  # 终点y坐标
    for i in range(n):
        driver.swipe(x1, y1, x1, y2, t)

# 向下滑动
def swipe_down(driver, t=500, n=1):
    s = driver.get_window_size()
    x1 = s['width'] * 0.5  # x坐标
    y1 = s['height'] * 0.25  # 起点y坐标
    y2 = s['height'] * 0.75  # 终点y坐标
    for i in range(n):
        driver.swipe(x1, y1, x1, y2, t)

# 向左滑动
def swipe_left(driver, t=500, n=1):
    s = driver.get_window_size()
    x1 = s['width'] * 0.75
    y1 = s['height'] * 0.5
    x2 = s['width'] * 0.25
    for i in range(n):
        driver.swipe(x1, y1, x2, y1, t)

# 向右
def swipe_right(driver, t=500, n=1):
    l = driver.get_window_size()
    x1 = l['width'] * 0.25
    y1 = l['height'] * 0.5
    x2 = l['width'] * 0.75
    for i in range(n):
        driver.swipe(x1, y1, x2, y1, t)

# start_x,start_y,end_x,end_y

# 轻打x轴向右移动x单位，y轴向下移动y单位
# def operate_tap(elemen_by,driver,element_info, xy=[]):
#     elements_by(elemen_by, driver, element_info).tap(x=xy[0], y=xy[1])

def send_keys(mOperate, cts):
    elements_by(mOperate, cts).send_keys(mOperate["text"])


# 封装常用的标签
def elements_by(mOperate, cts):
    elements = {
        Common.find_element_by_id: lambda: cts.find_element_by_id(mOperate["element_info"]),
        Common.find_elements_by_id: lambda: cts.find_elements_by_id(mOperate["element_info"]),
        Common.find_element_by_xpath: lambda: cts.find_element_by_xpath(mOperate["element_info"]),
        Common.find_element_by_name: lambda: cts.find_element_by_name(mOperate['name']),
        Common.find_elements_by_name: lambda: cts.find_elements_by_name(mOperate['name'])[mOperate['index']],
        Common.find_element_by_class_name: lambda: cts.find_element_by_class_name(mOperate['element_info']),
        Common.find_elements_by_class_name: lambda: cts.find_elements_by_class_name(mOperate['element_info'])[
            mOperate['index']]
    }
    return elements[mOperate["find_type"]]()
