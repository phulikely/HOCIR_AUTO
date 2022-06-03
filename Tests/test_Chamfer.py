import time
import os
from Config.config import TestData
from Tests.test_base import BaseTest
from Pages.LoginPage import LoginPage
from Pages.MainPage import MainPage
from selenium.webdriver.common.by import By


class Test_Chamfer(BaseTest):
    """
    Testcases for Chamfer
    """

    def test_chamfer_edge(self):
        
        vertex1_x = 961
        vertex1_y = 637
        vertex2_x = 1137
        vertex2_y = 524
        file = os.path.join(os.getcwd(), TestData.INPUT_FOLDER, 'box_no_color.stl')
    
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.login_page.do_select_app()

        self.main_page = MainPage(self.driver)
        self.main_page.chamfer(file, vertex1_x, vertex1_y, vertex2_x, vertex2_y, width=3000, segment=5, processing_time=15)
        actual = self.main_page.get_result_text((By.XPATH, TestData.RESULT_TXT))     

        assert actual != 'No file result'


    def test_chamfer_vertex(self):

        vertex1_x = 961
        vertex1_y = 637
        vertex2_x = 1137
        vertex2_y = 524
        file = os.path.join(os.getcwd(), TestData.INPUT_FOLDER, 'box_no_color.stl')

        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.login_page.do_select_app()

        self.main_page = MainPage(self.driver)
        self.main_page.chamfer(file, vertex1_x, vertex1_y, vertex2_x, vertex2_y, width=3000, segment=5, edge=False, processing_time=15)
        actual = self.main_page.get_result_text((By.XPATH, TestData.RESULT_TXT)) 

        assert actual != 'No file result'
        