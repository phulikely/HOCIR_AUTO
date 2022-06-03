import time
import os
from Config.config import TestData
from Tests.test_base import BaseTest
from Pages.LoginPage import LoginPage
from Pages.MainPage import MainPage
from selenium.webdriver.common.by import By


class Test_FillHole(BaseTest):
    """
    Testcases for Fill Hole
    """

    def test_fill_hole_normal(self):
        start1_x = 1014
        start1_y = 589
        tgt1_x = 931
        tgt1_y = 649
        start2_x = 1045
        start2_y = 727
        tgt2_x = 1124
        tgt2_y = 650
        file = os.path.join(os.getcwd(), TestData.INPUT_FOLDER, 'cube_with_hole.stl')

        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.login_page.do_select_app()

        self.main_page = MainPage(self.driver)
        self.main_page.fill_hole(file, start1_x, start1_y, tgt1_x, tgt1_y, start2_x, start2_y, tgt2_x, tgt2_y, processing_time=10)
        actual = self.main_page.get_result_text((By.XPATH, TestData.RESULT_TXT))

        assert actual != 'No file result'
