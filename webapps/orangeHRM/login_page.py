import time
from libUtils.seleniumUtils.weblocate_helper import WebLocateHelper


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.helper = WebLocateHelper(self.driver)

    def login(self):
        print("Login into the application...")
        ele_username = self.helper.identify_element("username", "NAME", "Username")
        self.helper.enter_text(ele_username, "Admin")
        time.sleep(2)
        element_password = self.helper.identify_element("password", "NAME", "password")
        self.helper.enter_text(element_password, "admin123")
        time.sleep(2)
        element_login_button = self.helper.identify_element("//button[@type='submit']", "XPATH", "login button")
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
