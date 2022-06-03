import time
import os
from Config.config import TestData
from Tests.test_base import BaseTest
from Pages.LoginPage import LoginPage
from Pages.MainPage import MainPage
from selenium.webdriver.common.by import By


class Test_Offset(BaseTest):
    """
    Testcases for offset 3D model
    """

    def test_offset_normal(self):
        
        point_x = 958
        point_y = 744        
        file = os.path.join(os.getcwd(), TestData.INPUT_FOLDER, 'box_mm.stl')
        
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.login_page.do_select_app()
        
        self.main_page = MainPage(self.driver)
        self.main_page.off_set(file, point_x, point_y, amount=10, processing_time=10)
        actual = self.main_page.get_result_text((By.XPATH, TestData.RESULT_TXT))

        assert actual != 'No file result'
