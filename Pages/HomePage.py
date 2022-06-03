from Config.config import TestData
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    """
    This class is page actions for home page
    Including locators, constructor of page class, page actions, get page title
    """
    
    ACCOUNT_NAME = (By.XPATH, '/html/body/div[1]/div[1]/header/nav/ul/li[1]/div/span')
    HEADER = (By.XPATH, '/html/body/div[1]/div[1]/div/div/div[2]/div[1]/div[1]/h4')
    LOGOUT_LINK = (By.XPATH, '/html/body/div[1]/div[1]/header/nav/ul/li[3]')
    
    def __init__(self, driver):
        """
        Constructor of the home page class
        """
        
        super().__init__(driver)
        # self.driver.get(TestData.BASE_URL)
    
    def get_home_page_title(self, title):
        """
        Get the page title
        """
        
        return self.get_title(title)
    
    def is_logout_link_exist(self):
        """
        Check forgot password link
        """
        
        return self.is_clickable(self.LOGOUT_LINK)
    
    def get_header_text(self):
        """
        Get the header of home page
        """
        
        if self.is_visible(self.HEADER):
            return self.get_element_text(self.HEADER)
        
    def get_account_name(self):
        """
        Get the name of loging account
        """
        
        if self.is_visible(self.ACCOUNT_NAME):
            return self.get_element_text(self.ACCOUNT_NAME)
