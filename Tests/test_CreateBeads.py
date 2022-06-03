import time
import os
from Config.config import TestData, ElementCreateRect
from Tests.test_base import BaseTest
from Pages.LoginPage import LoginPage
from Pages.MainPage import MainPage
from selenium.webdriver.common.by import By


class Test_Beads(BaseTest):
    """
    Testcases for Creating beads automatically
    """

    file = os.path.join(os.getcwd(), TestData.INPUT_FOLDER, 'box_mm.stl')


    def test_create_beads(self):

        beads1_x = 961
        beads1_y = 630
        beads2_x = 1065
        beads2_y = 564

        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.login_page.do_select_app()

        self.main_page = MainPage(self.driver)
        self.main_page.create_beads(self.file, beads1_x, beads1_y, beads2_x, beads2_y, processing_time=15)
        actual = self.main_page.get_result_text((By.XPATH, TestData.RESULT_TXT))        

        assert actual != 'No file result'
