import time
import os
from Config.config import TestData, ElementCreateRect
from Tests.test_base import BaseTest
from Pages.LoginPage import LoginPage
from Pages.MainPage import MainPage
from selenium.webdriver.common.by import By


class Test_Add_Color(BaseTest):
    """
    Testcases for Adding Color
    """

    def test_add_color_all_obj(self):

        color_pos_x = 1750
        color_pos_y = 572
        color_ok_btn_x = 1747
        color_ok_btn_y = 590
        color_area_x = 1104
        color_area_y = 515
        file = os.path.join(os.getcwd(), TestData.INPUT_FOLDER, 'box_no_color.stl')

        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.login_page.do_select_app()

        self.main_page = MainPage(self.driver)
        self.main_page.add_color(file, color_pos_x, color_pos_y,
                                 color_ok_btn_x, color_ok_btn_y,
                                 color_area_x, color_area_y,
                                 processing_time=10, select_area=False)
        actual = self.main_page.get_result_text((By.XPATH, TestData.RESULT_TXT))        

        assert actual != 'No file result'


    def test_add_color_select_area(self):

        color_pos_x = 1750
        color_pos_y = 572
        color_ok_btn_x = 1747
        color_ok_btn_y = 590
        color_area_x = 1104
        color_area_y = 515
        file = os.path.join(os.getcwd(), TestData.INPUT_FOLDER, 'box_no_color.stl')

        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.login_page.do_select_app()

        self.main_page = MainPage(self.driver)
        self.main_page.add_color(file, color_pos_x, color_pos_y,
                                 color_ok_btn_x, color_ok_btn_y,
                                 color_area_x, color_area_y,
                                 processing_time=10, select_area=True)
        actual = self.main_page.get_result_text((By.XPATH, TestData.RESULT_TXT))

        assert actual != 'No file result'
        