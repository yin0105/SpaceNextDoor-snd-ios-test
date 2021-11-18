# ---***--- coding = utf-8 ---***---
# @Time : 2021/7/26 15:00
# @Author: Paco

from TestProjects.baseProject import BaseProject
import time


class Login(BaseProject):
    login_pages = []

    def in_login_page(self):
        while len(self.login_pages) < 2:
            self.loading()
            self.login_pages = self.driver.find_elements_by_class_name("XCUIElementTypeButton")

    # phone
    def into_to_phone_login_page_to_input_phone(self):
        self.login_pages[1].click()
        self.loading()
        self.driver.find_element_by_ios_predicate("value == 'Phone number'").send_keys(self.testPhone)

    # Email
    def into_to_email_login_page_to_input_email(self):
        self.login_pages[0].click()
        self.loading()
        self.driver.find_element_by_ios_predicate("value == 'Email'").send_keys(self.testPhone)

    def judge_term_select(self):
        self.loading()
        # Judge term is select or not
        term_btn = self.driver.find_element_by_xpath('//*[@label="policy unselect"]')
        if term_btn.is_selected():
            self.driver.find_element_by_ios_predicate("name == 'LOGIN'").click()
        else:
            print("the term is unselect")
        return term_btn.is_selected()

    def send_otp_again(self):
        self.loading()
        send_again_btn = self.driver.find_element_by_xpath('label == "Didn’t you receive the message? please send it again."')
        send_again_btn.click()

    def input_otp(self):
        time.sleep(1)
        pin_code_view = self.driver.find_element_by_xpath('//XCUIElementTypeApplication[@name="Space Next Door"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeCollectionView/XCUIElementTypeCell/XCUIElementTypeOther[2]/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeCollectionView')
        self.loading()
        pin_cell = pin_code_view.find_elements_by_class_name('XCUIElementTypeTextField')
        for a in pin_cell:
            a.send_keys("3")

    # to login
    def click_verify_to_login(self):
        self.loading()
        self.driver.find_element_by_ios_predicate("name == 'VERIFY'").click()
