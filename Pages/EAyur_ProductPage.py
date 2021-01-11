from time import sleep
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By

from Utils.EAyur_driverUtils import Test_Functions


class TestProductsPage(Test_Functions):
    Btn_AddtoCart = (By.XPATH, "//a[@id='cbCheckOut']")
    Lnk_lsProducts = "//*[@class='jewellery']"
    Btn_ProceedToPayment = (By.XPATH, "//*[@id='tr_add_to_cart']/div[3]")
    Btn_ContinueShopping = (By.XPATH, "//*[@id='tr_add_to_cart']/div[2]/a/img")


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def test_SelectRequiredProduct(self,sReqProduct):
        try:
            # ---------------------------------
            lsProducts=self.driver.find_elements_by_xpath(self.Lnk_lsProducts)
            for product in lsProducts:
                print(product.text)
                if product.text.__contains__(sReqProduct):
                    product.click()
        except StaleElementReferenceException:
            print('except block')

    def test_AddtoCart(self):
        sleep(3)
        self.click(self.Btn_AddtoCart)

    def test_proceedToPayment(self):
        sleep(3)
        self.click(self.Btn_ProceedToPayment)

    def test_ContinueShopping(self):
        sleep(3)
        self.click(self.Btn_ContinueShopping)

