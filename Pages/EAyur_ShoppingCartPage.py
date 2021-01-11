from time import sleep
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Utils.EAyur_driverUtils import Test_Functions


class TestShoppingCartPage(Test_Functions):
    Txt_FullName = (By.XPATH, "//input[@id='ContentPlaceHolder1_txt_billingname']")
    Txt_Address = (By.XPATH, "//textarea[@id='ContentPlaceHolder1_txt_b_address']")
    Txt_City = (By.XPATH, "//input[@id='ContentPlaceHolder1_txt_b_City']")
    Pop_State = (By.XPATH, "//select[@id='ContentPlaceHolder1_drp_b_State']")
    #Pop_State = (By.ID, "ContentPlaceHolder1_drp_b_State")
    Txt_Pincode = (By.XPATH, "//input[@id='ContentPlaceHolder1_txt_b_PinCode']")
    Txt_MobileNo = (By.XPATH, "//input[@id='ContentPlaceHolder1_txt_mobileno']")
    Chk_SameAddress = (By.XPATH, "//input[@id='ContentPlaceHolder1_chkbx_regshipping']")
    Btn_SaveContinue = (By.XPATH, "//input[@id='ContentPlaceHolder1_btn_address']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def test_addDetailsToShoppingCartPage(self,sFullName,sAddress,sCity,sState,sPincode,sMobileNo):
        print('Add deatils to shopping cart page.')
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # scroll
        sleep(3)
        #FullName
        self.keys_controlA(self.Txt_FullName)
        self.enter_text(self.Txt_FullName,sFullName)
        #Address
        self.keys_controlA(self.Txt_Address)
        self.enter_text(self.Txt_Address, sAddress)
        #City
        self.keys_controlA(self.Txt_City)
        self.enter_text(self.Txt_City,sCity)
        #State
        # self.click(self.Pop_State)
        # PopUpSelect = Select(self.driver.find_element(self.Pop_State))
        # PopUpSelect.select_by_value(sState)
        #pincode
        self.keys_controlA(self.Txt_Pincode)
        self.enter_text(self.Txt_Pincode, sPincode)
        #Mobile no
        self.keys_controlA(self.Txt_MobileNo)
        self.enter_text(self.Txt_MobileNo, sMobileNo)
        #Same billing address check box
        self.click(self.Chk_SameAddress)
        #Save and continue button
        sleep(5)
        self.click(self.Btn_SaveContinue)
