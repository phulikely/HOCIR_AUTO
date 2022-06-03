import time
import os
from Config.config import TestData
from Tests.test_base import BaseTest
from Pages.LoginPage import LoginPage
from Pages.MainPage import MainPage
from selenium.webdriver.common.by import By


class Test_ScaleXYZ(BaseTest):
    """
    Testcases for Scale individually in each XYZ direction
    """
    
    def test_scale_xyz_normal(self):

        file = os.path.join(os.getcwd(), TestData.INPUT_FOLDER, 'bend.stl')

        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.login_page.do_select_app()

        self.main_page = MainPage(self.driver)
        self.main_page.scale_xyz(file, x_pct=200, y_pct=200, z_pct=200, processing_time=15)
        actual = self.main_page.get_result_text((By.XPATH, TestData.RESULT_TXT))

        assert actual != 'No file result'
