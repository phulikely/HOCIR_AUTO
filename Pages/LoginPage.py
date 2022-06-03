from Config.config import TestData
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from Pages.HomePage import HomePage
from Pages.MainPage import MainPage
import time


class LoginPage(BasePage):
    """
    This class is page actions for login page
    Including locators, constructor of page class, page actions, get page title
    """
    
    USER = (By.ID, 'username')
    PASSWORD = (By.ID, 'password')
    LOGIN_BTN = (By.XPATH, '//*[@id="page-login"]/div/div[1]/div[2]/div/form/div[3]/button')
    FORGOT_PWD_LINK = (By.LINK_TEXT, 'Forgot password')
    LOG_OUT_LINK = (By.XPATH, '/html/body/div[1]/div[1]/header/nav/ul/li[3]')
    LOG_OUT_CONFIRM = (By.XPATH, "//button[contains(text(),'Yes')]")
    APPLICATION_LIST_PAGE = (By.XPATH, '/html/body/div[1]/div[1]/div/div/div[2]/div[2]/div[1]/a/button')
    
    
    def __init__(self, driver):
        """
        Constructor of the login page class
        """
        
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)
    
    def get_login_page_title(self, title):
        """
        Get the page title
        """
        
        return self.get_title(title)
    
    def is_forgot_pwd_link_exist(self):
        """
        Check forgot password link
        """
        
        return self.is_clickable(self.FORGOT_PWD_LINK)
    
    def do_login(self, username, password):
        """
        Login to app
        """
        
        self.do_send_keys(self.USER, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BTN)
        return HomePage(self.driver)
    
    def do_logout(self):
        """
        Logout
        """
        
        self.do_click(self.LOG_OUT_LINK)   
        self.do_click(self.LOG_OUT_CONFIRM)

    def do_select_app(self):
        """
        Click Application List
        """
        
        self.do_click(self.APPLICATION_LIST_PAGE)
        return MainPage(self.driver)
        