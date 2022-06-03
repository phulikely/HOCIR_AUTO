import time
import os
from Config.config import TestData
from Tests.test_base import BaseTest
from Pages.LoginPage import LoginPage
from Pages.MainPage import MainPage
from selenium.webdriver.common.by import By


class Test_Add_Texture(BaseTest):
    """
    Testcases for Adding Texture
    """

    def test_add_texture_area(self):
        
        file = os.path.join(os.getcwd(), TestData.INPUT_FOLDER, 'box_no_color.stl')
        img = os.path.join(os.getcwd(), TestData.INPUT_FOLDER, 'hiep.jpg')        
        point1_x = 961
        point1_y = 547
        
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.login_page.do_select_app()
        
        self.main_page = MainPage(self.driver)
        self.main_page.add_texture(file, img, point1_x, point1_y, processing_time=10, select_area=True)
        actual = self.main_page.get_result_text((By.XPATH, TestData.RESULT_TXT))        

        assert actual != 'No file result'
        