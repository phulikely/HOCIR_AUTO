import time
import os
from Config.config import TestData
from Tests.test_base import BaseTest
from Pages.LoginPage import LoginPage
from Pages.MainPage import MainPage
from selenium.webdriver.common.by import By


class Test_Move_To_Plane(BaseTest):
    """
    Testcases for Move_To_Plane
    """

    def test_move_to_xy(self):

        file = os.path.join(os.getcwd(), TestData.INPUT_FOLDER, 'box_no_color.stl')

        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.login_page.do_select_app()

        self.main_page = MainPage(self.driver)
        self.main_page.move_to_plane(file, processing_time=15)
        actual = self.main_page.get_result_text((By.XPATH, TestData.RESULT_TXT))

        assert actual != 'No file result'


    def test_move_to_yz(self):

        file = os.path.join(os.getcwd(), TestData.INPUT_FOLDER, 'box_no_color.stl')

        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.login_page.do_select_app()

        self.main_page = MainPage(self.driver)
        self.main_page.move_to_plane(file, plane='yz', processing_time=5)
        actual = self.main_page.get_result_text((By.XPATH, TestData.RESULT_TXT))

        assert actual != 'No file result'


    def test_move_to_zx(self):

        file = os.path.join(os.getcwd(), TestData.INPUT_FOLDER, 'box_no_color.stl')

        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.login_page.do_select_app()

        self.main_page = MainPage(self.driver)
        self.main_page.move_to_plane(file, plane='zx', processing_time=15)
        actual = self.main_page.get_result_text((By.XPATH, TestData.RESULT_TXT))

        assert actual != 'No file result'