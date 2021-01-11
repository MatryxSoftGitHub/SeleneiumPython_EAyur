from time import sleep
from selenium.webdriver.common.by import By

from Utils.EAyur_driverUtils import Test_Functions


class TestLoginPage(Test_Functions):
    Txt_Username = (By.XPATH, "//input[@id='ContentPlaceHolder1_txt_email']")
    Txt_Password = (By.XPATH, "//input[@id='ContentPlaceHolder1_txt_password']")
    Btn_Login = (By.XPATH, "//input[@id='ContentPlaceHolder1_btn_submit_login']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def test_LoginToApplication(self, sUsername, sPassword):
        # Login To Website-------------------------------------------------------------------------------------------------
        print('Login to the application')
        self.enter_text(self.Txt_Username, sUsername)
        self.enter_text(self.Txt_Password, sPassword)
        sleep(3)
        self.click(self.Btn_Login)
        print('Logged in is successfully completed!')