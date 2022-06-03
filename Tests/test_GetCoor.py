import time
import os
from Config.config import TestData
from Tests.test_base import BaseTest
from Pages.LoginPage import LoginPage
from Pages.MainPage import MainPage
from selenium.webdriver.common.by import By


class Test_Get_Coor(BaseTest):
    """
    Testcases for get coordinate information of multi points
    """

    def test_get_coor_normal(self):

        point1_x = 835
        point1_y = 551
        point2_x = 1063
        point2_y = 565
        point3_x = 958
        point3_y = 744   
        file = os.path.join(os.getcwd(), TestData.INPUT_FOLDER, 'box_mm.stl')

        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.login_page.do_select_app()

        self.main_page = MainPage(self.driver)
        self.main_page.get_coor(file, point1_x, point1_y, point2_x, point2_y, point3_x, point3_y, processing_time=10)
        actual = self.main_page.get_result_text((By.XPATH, TestData.RESULT_TXT))

        assert actual != 'No file result'
