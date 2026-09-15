from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver import FirefoxOptions
from selenium.webdriver import EdgeOptions
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select


import json
import pytest

class page_3:

    def __init__(self,driver):
        self.driver = driver


    def window_switch(self):
        windows_list = self.driver.window_handles
        print(len(windows_list))
        # self.driver.switch_to.window(windows_list[1])
