import time
import os
from Config.config import TestData
from Tests.test_base import BaseTest
from Pages.LoginPage import LoginPage
from Pages.MainPage import MainPage
from selenium.webdriver.common.by import By


class Test_Get_Length_Specified(BaseTest):
    """
    Testcases for get length of multi points specified in 3D model
    """

    def test_get_length_specified_normal(self):
        
        point1_x = 835
        point1_y = 551
        point2_x = 1063
        point2_y = 565
        file = os.path.join(os.getcwd(), TestData.INPUT_FOLDER, 'box_mm.stl')

        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.login_page.do_select_app()
        
        self.main_page = MainPage(self.driver)
        self.main_page.get_length_of_point(file, point1_x, point1_y, point2_x, point2_y, processing_time=5)
        actual = self.main_page.get_result_text((By.XPATH, TestData.RESULT_TXT))

        assert actual != 'No file result'
