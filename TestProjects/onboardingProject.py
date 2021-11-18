# ---***--- coding = utf-8 ---***---
# @Time : 2021/7/26 15:47
# @Author: Paco

from baseProject import BaseProject


class OnBoarding(BaseProject):
    closeBtn = super.driver.find_element_by_xpath('//*[@label="btn close"]')

    def close_onboarding(self):
        self.closeBtn.click()

    def swipe_onboarding(self):
        for i in range(4):
            self.el.opreate_swipe_left()
        else:
            self.closeBtn.click()