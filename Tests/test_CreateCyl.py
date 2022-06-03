import time
import pytest
from Config.config import TestData, ElementCreateRect
from Tests.test_base import BaseTest
from Pages.LoginPage import LoginPage
from Pages.MainPage import MainPage
from selenium.webdriver.common.by import By


class Test_Cyl(BaseTest):
    """
    Testcases for Creating Cynlinder
    """
    
    def test_create_cyl_normal(self):
        
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.login_page.do_select_app()
        
        self.main_page = MainPage(self.driver)
        self.main_page.create_cyl(radius=45, height=55, processing_time=10)
        actual = self.main_page.get_result_text((By.XPATH, TestData.RESULT_TXT))        

        assert actual != 'No file result'
