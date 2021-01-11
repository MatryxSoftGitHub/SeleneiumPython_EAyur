from time import sleep
import pytest
from selenium import webdriver

from Baseclass.conftest import TestBase
from Pages.EAyur_HomePage import TestHomePage
from Pages.EAyur_LoginPage import TestLoginPage
from Pages.EAyur_ProductPage import TestProductsPage
from Pages.EAyur_ShoppingCartPage import TestShoppingCartPage
from Pages.EAyur_UserHomePage import TestUserHomePage


@pytest.mark.usefixtures('setup')
class TestDemo1(TestBase):

    def test_DemoMethod(self):
        homePage = TestHomePage(self.driver)
        loginPage = TestLoginPage(self.driver)
        userHomePage = TestUserHomePage(self.driver)
        productPage=TestProductsPage(self.driver)
        shoppingCartPage=TestShoppingCartPage(self.driver)

        #Step-1
        sleep(5)
        
        print('Navigate to login page')
        homePage.test_NavigateToLoginPage()
        print('Login page is displayed')

        # Step-2
        print('login to application')
        loginPage.test_LoginToApplication("vidyaclk12@gmail.com", "Matryx@2020")
        print('Login is successfull!!!')

        userHomePage.test_SearchForAProduct('Balm')

        productPage.test_SelectRequiredProduct('Himalaya Lip Balm')
        productPage.test_AddtoCart()
        productPage.test_proceedToPayment()

        shoppingCartPage.test_addDetailsToShoppingCartPage("Vidyashri","LG HALLI, BANLORE-94","Banglore","","560094","7892604547")

        sleep(10)
        #Step-Last
        print('Logout from the application')
        userHomePage.test_LogoutFromApplication()
        print('Logout from the application is completed!')

        print('Test completed!!!')