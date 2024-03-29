import pytest
from selenium import webdriver
from Pages.LoginPage import LoginPage
from seleniumwire import webdriver


"""
Excution before and after each testcase
"""

# @pytest.fixture(params=['chrome'], scope='class')
@pytest.fixture()
def setup(request):
    web_driver = webdriver.Chrome()
    # web_driver.implicitly_wait(10)
    web_driver.maximize_window()
    web_driver.delete_all_cookies()
    # if request.param == 'firefox':
    #     web_driver = webdriver.FireFox(executable_path=TestData.FIREFOX_EXECUTABLE_PATH)
    request.cls.driver = web_driver
    login_page = LoginPage(web_driver)
    yield
    try:
        login_page.do_logout()
        web_driver.close()
        web_driver.quit()
    except:
        print('Logout unsuccessfully!')