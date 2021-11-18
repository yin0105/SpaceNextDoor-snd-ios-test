# ---***--- coding = utf-8 ---***---
# @Time : 2021/7/26 15:47
# @Author: Paco

from TestProjects.baseProject import BaseProject


class OnBoarding(BaseProject):

    def close_onboarding(self):
        closeBtn = self.driver.find_element_by_xpath('//*[@label="btn close"]')
        if len(closeBtn) > 0:
            self.loading()
            closeBtn.click()
        else:
            self.loading()

    def swipe_onboarding(self):
        for i in range(4):
            self.el.opreate_swipe_left()
        else:
            self.driver.find_element_by_xpath('//*[@label="btn close"]').click()