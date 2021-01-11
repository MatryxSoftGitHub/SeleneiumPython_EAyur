import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os


class TestBase:

    # def __init__(self, driver):
    #     self.driver = driver

    @pytest.fixture()
    def setup(self):
        print('Launching Browser')
        self.d_Options = webdriver.ChromeOptions()
        self.d_Options.add_argument("--disable-notifications")
        self.driver = webdriver.Chrome(chrome_options=self.d_Options,executable_path="D:\\Selenium\\DemoProject_PythonSelenium\\chromedriver.exe")

        self.driver.implicitly_wait(5)

        self.driver.get("https://www.eayur.com/")
        self.driver.maximize_window()
        print('Browser launched')
        print(self.driver.title)  # Title of the page
        yield
        self.driver.close()
        print('Browser is closed')