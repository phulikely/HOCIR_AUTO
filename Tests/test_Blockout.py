import time
import os
from Config.config import TestData
from Tests.test_base import BaseTest
from Pages.LoginPage import LoginPage
from Pages.MainPage import MainPage
from selenium.webdriver.common.by import By


class Test_Blockout(BaseTest):
    """
    Testcases for Blockout
    """

    def test_blockout_normal(self):
        
        point1_x = 960
        point1_y = 697        
        file = os.path.join(os.getcwd(), TestData.INPUT_FOLDER, 'box_mm.stl')
        
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.login_page.do_select_app()
        
        self.main_page = MainPage(self.driver)
        self.main_page.block_out(file, point1_x, point1_y, processing_time=15)
        actual = self.main_page.get_result_text((By.XPATH, TestData.RESULT_TXT))

        assert actual != 'No file result'
