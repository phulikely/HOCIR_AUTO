import time
import os
from Config.config import TestData
from Tests.test_base import BaseTest
from Pages.LoginPage import LoginPage
from Pages.MainPage import MainPage
from selenium.webdriver.common.by import By


class Test_Boolean_Union(BaseTest):
    """
    Testcases for Boolean Union(A + B)
    """
    
    def test_boolean_union(self):
        
        file1 = os.path.join(os.getcwd(), TestData.INPUT_FOLDER, 'box_no_color.stl')
        file2 = os.path.join(os.getcwd(), TestData.INPUT_FOLDER, 'box_no_color2.stl')
        
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.login_page.do_select_app()
        
        self.main_page = MainPage(self.driver)
        self.main_page.boolean_union(file1, file2, processing_time=10)
        actual = self.main_page.get_result_text((By.XPATH, TestData.RESULT_TXT))
        
        assert actual != 'No file result'