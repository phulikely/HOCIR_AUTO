import json
from Config.config import TestData
from Tests.test_base import BaseTest
from Pages.LoginPage import LoginPage
from Pages.MainPage import MainPage
from selenium.webdriver.common.by import By
from seleniumwire.utils import decode


class Test_Rect(BaseTest):
    """
    Testcases for Creating Rectangular
    """
    
    def test_create_rect_normal(self):
        
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.login_page.do_select_app()
        
        self.main_page = MainPage(self.driver)
        self.main_page.create_rect(length=555, width=666, height=777, processing_time=15)
        actual = self.main_page.get_result_text((By.XPATH, TestData.RESULT_TXT))        

        for request in self.driver.requests:
            if request.response and 'request_id' in request.url:
                # print(request.url.split('?')[-1])
                # break
                response = request.response
                body = decode(response.body, response.headers.get('Content-Encoding', 'identity'))
                        # if request.url == "https://api.3dd-toolbox.com/ricoh-api/uploadfile":
                print(json.loads(body))
                break

        assert actual != 'No file result'


    # def test_create_rect_with_alphabe(self):
        
    #     self.login_page = LoginPage(self.driver)
    #     self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
    #     self.login_page.do_select_app()
        
    #     self.main_page = MainPage(self.driver)
    #     self.main_page.create_rect(length='5ab5c5', width='222\222', height=77.07, processing_time=15)
    #     actual = self.main_page.get_result_text((By.XPATH, TestData.RESULT_TXT))
    #     # self.login_page.do_logout()
    #     assert actual != 'No file result'


    # def test_create_rect_with_special_char(self):
        
    #     self.login_page = LoginPage(self.driver)
    #     self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
    #     self.login_page.do_select_app()
        
    #     self.main_page = MainPage(self.driver)
    #     self.main_page.create_rect(length='!@#$%^&*()_+.', width='!@#$%^&*()_+.', height='!@#$%^&*()_+.', processing_time=15)
    #     actual = self.main_page.get_result_text((By.XPATH, TestData.RESULT_TXT))

    #     assert actual == 'No file result'
