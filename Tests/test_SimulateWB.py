import time
import os
from Config.config import TestData
from Tests.test_base import BaseTest
from Pages.LoginPage import LoginPage
from Pages.MainPage import MainPage
from selenium.webdriver.common.by import By


class Test_SimulateWB(BaseTest):
    """
    Testcases for simulate 3D-WB device
    """

    def test_simulate_wb_normal(self):
        
        file = os.path.join(os.getcwd(), TestData.INPUT_FOLDER, 'test.rwb')
        
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.login_page.do_select_app()
        
        self.main_page = MainPage(self.driver)
        self.main_page.simulate_3d_wb(file, processing_time=5)
        actual = self.main_page.get_result_text((By.XPATH, TestData.RESULT_TXT))

        assert actual != 'No file result'
