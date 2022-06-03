import time
import os
from Config.config import TestData
from Tests.test_base import BaseTest
from Pages.LoginPage import LoginPage
from Pages.MainPage import MainPage
from selenium.webdriver.common.by import By


class Test_Smooth_Area(BaseTest):
    """
    Testcases for smooth an area of object
    """

    def test_smooth_area_normal(self):

        change_size_area_x = 1316
        change_size_area_y = 1000
        point1_x = 975
        point1_y = 645        
        file = os.path.join(os.getcwd(), TestData.INPUT_FOLDER, 'sphere.stl')
        
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.login_page.do_select_app()
        
        self.main_page = MainPage(self.driver)
        self.main_page.smooth_area(file, change_size_area_x, change_size_area_y, point1_x, point1_y, processing_time=10)
        actual = self.main_page.get_result_text((By.XPATH, TestData.RESULT_TXT))

        assert actual != 'No file result'
