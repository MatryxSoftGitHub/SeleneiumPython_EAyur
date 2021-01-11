from time import sleep
import pytest
from selenium import webdriver

from EAyurProject_PythonSelenium.Baseclass.conftest import TestBase
from EAyurProject_PythonSelenium.Pages.EAyur_HomePage import TestHomePage
from EAyurProject_PythonSelenium.Pages.EAyur_LoginPage import TestLoginPage
from EAyurProject_PythonSelenium.Pages.EAyur_ProductPage import TestProductsPage
from EAyurProject_PythonSelenium.Pages.EAyur_ShoppingCartPage import TestShoppingCartPage
from EAyurProject_PythonSelenium.Pages.EAyur_UserHomePage import TestUserHomePage


@pytest.mark.usefixtures('setup')
class TestDemo1(TestBase):

    def test_DemoMethod(self):
        homePage = TestHomePage(self.driver)
        loginPage = TestLoginPage(self.driver)
        userHomePage = TestUserHomePage(self.driver)
        productPage=TestProductsPage(self.driver)
        shoppingCartPage=TestShoppingCartPage(self.driver)

        #Step-1
        print('Navigate to login page')
        homePage.test_NavigateToLoginPage()
        print('Login page is displayed')

        # Step-2
        print('login to application')
        loginPage.test_LoginToApplication("vidyaclk12@gmail.com", "Matryx@2020")
        print('Login is successfull!!!')

        #first  prduct
        userHomePage.test_SearchForAProduct('Balm')
        productPage.test_SelectRequiredProduct('Himalaya Natural Intensi')
        productPage.test_AddtoCart()
        productPage.test_ContinueShopping()

        #Second product
        userHomePage.test_SearchForAProduct('Hair Care')
        productPage.test_SelectRequiredProduct('Dhathri Hair Care Herbal')
        productPage.test_AddtoCart()

        productPage.test_proceedToPayment()
        shoppingCartPage.test_addDetailsToShoppingCartPage("Vidyashri","LG HALLI, BANLORE-94","Banglore","","560094","7892604547")

        sleep(10)
        #Step-Last
        print('Logout from the application')
        userHomePage.test_LogoutFromApplication()
        print('Logout from the application is completed!')

        print('Test completed!!!')