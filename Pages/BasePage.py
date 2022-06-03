from tkinter import Image
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from Config.config import TestData
from io import BytesIO
from PIL import Image, ImageDraw
import time

class BasePage:
    """
    This class is the parent of all pages
    It contains all the generic methods and utilities for all the pages
    """
    
    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator, time_wait=0.5):
        time.sleep(time_wait)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()
        time.sleep(time_wait)

    def do_clear_txb(self, by_locator, time_wait=0.5):
        time.sleep(time_wait)
        txb = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator))
        txb.click()
        txb.send_keys(Keys.CONTROL + "a")
        txb.send_keys(Keys.DELETE)
        time.sleep(time_wait)

    def do_send_keys(self, by_locator, text, time_wait=0.5):
        time.sleep(time_wait)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)
        time.sleep(time_wait)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def is_clickable(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator))
        return bool(element)

    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title
    
    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)
    
    def take_screenshot(self):
        return self.driver.get_screenshot_as_png()
    
    def draw_rect(self, element, time_wait=0.5):
        time.sleep(time_wait)
        loc = element.location
        size = element.size
        png = self.take_screenshot()
        img = Image.open(BytesIO(png))
        left = loc['x']
        top = loc['y']
        right = loc['x'] + size['width']
        bottom = loc['y'] + size['height']
        red_frame = ImageDraw.Draw(img)
        red_frame = red_frame.rectangle((left - TestData.OFFSET_ELEMENT,
                                         top - TestData.OFFSET_ELEMENT,
                                         right + TestData.OFFSET_ELEMENT,
                                         bottom + TestData.OFFSET_ELEMENT),
                                        outline ="red", width=4)
        time.sleep(time_wait)
        return img
