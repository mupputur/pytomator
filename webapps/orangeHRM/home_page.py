from login_page import LoginPage
from libUtils.seleniumUtils.weblocate_helper import WebLocateHelper
import time


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
        print("Navigating to time page...")
        time_page = self.helper.identify_element("(//a[@class='oxd-main-menu-item'])[4]", "XPATH", "Time")
        time_page.click()
        time.sleep(2)
        print("Successfully navigated to time page")

    def navigate_to_recruitment(self):
        """
        Function navigates to recruitment page

        :Authors: Pravallika
        """
        print("Navigating to recruitement page...")
        recruitment_page = self.helper.identify_element("(//a[@class='oxd-main-menu-item'])[5]", "XPATH", "Recruitment")
        recruitment_page.click()
        time.sleep(2)
        print("Successfully navigated to recruitment page")

    def navigate_to_performance(self):
        """
        Function navigates to performance page

        :Authors: Radha Krishna
        """
        print("Navigating to performance page ...")
        performance_page = self.helper.identify_element("(//a[@class='oxd-main-menu-item'])[7]", "XPATH", "Performance")
        performance_page.click()
        time.sleep(5)
        print("Successfully navigated to performance page")
    def navigate_to_leave(self):
        """
        Function navigates to leave page

        :Authors: Radha Krishna
        """
        print("Navigating to leave page ...")
        leave_page = self.helper.identify_element("//a[@href= '/web/index.php/leave/viewLeaveModule']", "XPATH",
                                                  "Leave")
        leave_page.click()
        time.sleep(5)
        print("Successfully navigated to leave page")

    def navigate_to_myinfo(self):
        """
        Function navigates to myinfo page

        :Authors: Sreedevi
        """
        print("Navigating to myinfo...")
        myinfo_page = self.helper.identify_element ("(//a[@class='oxd-main-menu-item'])[6]", "XPATH", "My Info")
        myinfo_page.click()
        time.sleep(5)
        print("Successfully navigated to myinfo")

    def navigate_to_dashboard(self):
        """
        Function navigates to dashboard page

        :Authors: Sreedevi
        """
        print("Navigating to dashboard...")
        dashboard_page = self.helper.identify_element("//a[@class='oxd-main-menu-item active']", "XPATH", "Dashboard")
        dashboard_page.click()
        time.sleep(5)
        print("Successfully navigated to dashboard")

    def navigate_to_directories(self):
        """
        Function navigates to directories page

        :Authors: Sreevani
        """
        print("navigates to directories page...")
        directories_page = self.helper.identify_element("(//a[@class='oxd-main-menu-item'])[8]", "XPATH", "Directory")
        directories_page.click()
        time.sleep(5)
        print("Successfully navigated directories page")

    def navigate_to_maintenance(self):
        """
        Function navigates to maintenance page

        :Authors: Sreevani
        """
        print("navigates to maintenance page...")
        maintenance_page = self.helper.identify_element("(//a[@class='oxd-main-menu-item'])[9]", "XPATH", "Maintance")
        maintenance_page.click()
        time.sleep(5)
        print("Successfully navigated maintenance page ")

    def navigate_to_buzz(self):
        """
        Function navigates to buzz page

        :Authors: Radha Krishna
        """
        print("Navigating to buzz page ...")
        buzz_page = self.helper.identify_element("//a[@href= '/web/index.php/buzz/viewBuzz']", "XPATH", "Buzz")
        buzz_page.click()
        time.sleep(5)
        print("Successfully navigated to buzz page")

if __name__ == "__main__":
    # Test code or Driver code
    from libUtils.seleniumUtils.driver_manager import DriverManager
    # Driver Initialization
    dm = DriverManager()

    # Navigate to Home --> PIM
    obj = HomePage(dm.driver)
    # obj.navigate_to_pim()
    #obj.navigate_to_admin()
    #obj.navigate_to_myinfo()
    #obj.navigate_to_dashboard()
    #obj.navigate_to_time()
    #obj.navigate_to_recruitment()
    #obj.navigate_to_leave()
    #obj.navigate_to_performance()
    #obj.navigate_to_buzz()
    #obj.navigate_to_directories()
    obj.navigate_to_maintenance()
