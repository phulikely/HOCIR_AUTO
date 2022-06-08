import pytest
from Config.config import TestData
from Pages.HomePage import HomePage
from Tests.test_base import BaseTest
from Pages.LoginPage import LoginPage


class Test_HomePage(BaseTest):
    """
    Testcases for Home Page
    """

    def test_homepage_title(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        title = homePage.get_home_page_title(TestData.HOME_PAGE_TITLE)
        self.loginPage.do_logout()
        assert title  == TestData.HOME_PAGE_TITLE

    def test_homepage_header(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        header = homePage.get_header_text()
        self.loginPage.do_logout()
        assert header  == TestData.HOME_PAGE_HEADER

    def test_homepage_account(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        acc_name = homePage.get_account_name()
        self.loginPage.do_logout()
        assert acc_name  == TestData.USER_NAME

    def test_logout_clickable(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)  
        assert homePage.is_logout_link_exist()
        self.loginPage.do_logout()