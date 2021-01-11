from time import sleep
from selenium.webdriver.common.by import By

from Utils.EAyur_driverUtils import Test_Functions


class TestHomePage(Test_Functions):
    Lnk_LogIn = (By.XPATH, "//body/form[@id='payment_form']/div[4]/div[1]/nav[1]/div[8]/div[1]/ul[1]/li[1]/a[1]")

    #// *[ @ id = 'div_login'] / li[1] / a
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def test_NavigateToLoginPage(self):
        # Login To EAyur website-------------------------------------------------------------------------------------------------
        print('Navigate to login page.')
        #self.wait_visibility(self.Lnk_LogIn)
        self.click(self.Lnk_LogIn)
        print('Login page displayed successfully!.')