import time
import os
from Config.config import TestData
from Tests.test_base import BaseTest
from Pages.LoginPage import LoginPage
from Pages.MainPage import MainPage
from selenium.webdriver.common.by import By


class Test_Get_Length_Around(BaseTest):
    """
    Testcases for get length of multi points around in 3D model
    """

    def test_get_length_around_normal(self):
        
        file = os.path.join(os.getcwd(), TestData.INPUT_FOLDER, 'box_mm.stl')
        
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.login_page.do_select_app()
        
        self.main_page = MainPage(self.driver)
        self.main_page.get_length_around(file, xy_length=10, processing_time=15)
        actual = self.main_page.get_result_text((By.XPATH, TestData.RESULT_TXT))

        assert actual != 'No file result'
