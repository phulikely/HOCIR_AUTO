import pytest
from Config.config import TestData
from Tests.test_base import BaseTest
from Pages.LoginPage import LoginPage


class Test_Login(BaseTest):
    """
    Testcases for Login Page
    """

    def test_forgot_pwd_link_clickable(self):
        self.loginPage = LoginPage(self.driver)
        result = self.loginPage.is_forgot_pwd_link_exist()
        assert result
        
    def test_login_page_title(self):
        self.loginPage = LoginPage(self.driver)
        title = self.loginPage.get_title(TestData.LOGIN_PAGE_TITLE)
        assert title == TestData.LOGIN_PAGE_TITLE
    
    def test_login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)