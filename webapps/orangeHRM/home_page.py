from login_page import LoginPage
from libUtils.seleniumUtils.weblocate_helper import WebLocateHelper


class HomePage:

    def __init__(self, driver):
        login_page = LoginPage(driver)
        login_page.login()
        # login_page.login() Enable incase if you are getting CRF token issue
        self.helper = WebLocateHelper(driver)

    def navigate_to_pim(self):
        """
        Function navigates to pim page

        :Authors: mupputuri
        """
        print("Navigating to pim page ...")
        pim_page = self.helper.identify_element("//a[@href= '/web/index.php/pim/viewPimModule']", "XPATH", "PIM")
        pim_page.click()
        print("Successfully navigated to pim page")

    def navigate_to_admin(self):
        """
        Function navigates to admin page

        :Authors: mupputuri
        """
        print("Navigating to admin page...")
        admin_page = self.helper.identify_element("//a[@href='/web/index.php/admin/viewAdminModule']", "XPATH", "Admin")
        admin_page.click()
        print("Successfully navigated to admin page")

    def navigate_to_time(self):
        """
        Function navigates to time page

        :Authors: Pravallika
        """
        pass

    def navigate_to_recruitment(self):
        """
        Function navigates to recruitment page

        :Authors: Pravallika
        """
        pass

    def navigate_to_performance(self):
        """
        Function navigates to performance page

        :Authors: Radha Krishna
        """
        pass

    def navigate_to_leave(self):
        """
        Function navigates to leave page

        :Authors: Radha Krishna
        """
        pass

    def navigate_to_myinfo(self):
        """
        Function navigates to myinfo page

        :Authors: Sreedevi
        """
        pass

    def navigate_to_dashboard(self):
        """
        Function navigates to dashboard page

        :Authors: Sreedevi
        """
        pass

    def navigate_to_directories(self):
        """
        Function navigates to directories page

        :Authors: Sreevani
        """
        pass

    def navigate_to_maintenance(self):
        """
        Function navigates to maintenance page

        :Authors: Sreevani
        """
        pass

    def navigate_to_buzz(self):
        """
        Function navigates to buzz page

        :Authors: Radha Krishna
        """
        pass

if __name__ == "__main__":
    # Test code or Driver code
    from libUtils.seleniumUtils.driver_manager import DriverManager
    # Driver Initialization
    dm = DriverManager()

    # Navigate to Home --> PIM
    obj = HomePage(dm.driver)
    # obj.navigate_to_pim()
    obj.navigate_to_admin()