import time
from libUtils.seleniumUtils.weblocate_helper import WebLocateHelper
from libUtils.seleniumUtils.locators import LoginPageLocators as lp

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.helper = WebLocateHelper(self.driver)

    def login(self):
        print("Login into the application...")
        time.sleep(5)
        ele_username = self.helper.identify_element(lp.USERNAME_TB_NAME_LOC[0], lp.USERNAME_TB_NAME_LOC[1], "Username")
        self.helper.enter_text(ele_username, "Admin")
        time.sleep(2)
        element_password = self.helper.identify_element(lp.PASSWORD_TB_NAME_LOC[0], lp.PASSWORD_TB_NAME_LOC[1], "password")
        self.helper.enter_text(element_password, "admin123")
        time.sleep(2)
        element_login_button = self.helper.identify_element(lp.LOGIN_BT_XPATH_LOC[0], lp.LOGIN_BT_XPATH_LOC[1], "login button")
        self.helper.click_on(element_login_button, "LoginButton")
        print("Successfully login to application.")

    def logout(self):
        print("Logging out app")

if __name__ == "__main__":
    # Get driver instance
    from libUtils.seleniumUtils.driver_manager import DriverManager
    driver_manager = DriverManager()
    login_page = LoginPage(driver_manager.driver)
    login_page.login()
    login_page.login()
