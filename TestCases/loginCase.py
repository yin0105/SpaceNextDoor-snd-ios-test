# ---***--- coding = utf-8 ---***---
# @Time : 2021/7/26 15:00
# @Author: Paco

from TestProjects.loginProject import Login


def login_with_phone():
    login_case = Login()
    login_case.in_login_page()
    login_case.into_to_phone_login_page_to_input_phone()
    login_case.judge_term_select()
    login_case.input_otp()
    login_case.click_verify_to_login()

login_with_phone()