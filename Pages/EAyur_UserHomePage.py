from time import sleep
from selenium.webdriver.common.by import By

from Utils.EAyur_driverUtils import Test_Functions


class TestUserHomePage(Test_Functions):
    Lnk_Logout = (By.XPATH, "//a[@id='LinkButton2']")
    Txt_SearchBox = (By.XPATH, "//input[@id='txt_search_box']")
    Btn_Go = (By.XPATH, "//input[@id='lnk_search']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def test_LogoutFromApplication(self):
        # Logout from Website-------------------------------------------------------------------------------------------------
        print('Logout from the application.')
        sleep(3)
        self.click(self.Lnk_Logout)
        print('Logout from the application is completed!.')

    def test_SearchForAProduct(self,sProduct):
        # search a required product from the website----------------------------------
        print('Search for required product.')
        self.enter_text(self.Txt_SearchBox, sProduct)
        self.click(self.Btn_Go)
        print('Product page is displayed.')