from home_page import HomePage
from libUtils.seleniumUtils.weblocate_helper import WebLocateHelper
import time

class LeavePage:

    def __init__(self, driver):
        home_page = HomePage(driver)
        home_page.navigate_to_leave()
        self.helper = WebLocateHelper(driver)

    def navigate_to_apply(self):
        print("Navigating to apply ...")
        apply_page = self.helper.identify_element("//a[@class='oxd-topbar-body-nav-tab-item']", "XPATH", "Apply")
        apply_page.click()
        time.sleep(2)
        print("Successfully navigated to apply page")

    def navigate_to_my_leave(self):
        print("Navigating to myleave ...")
        myleave_page = self.helper.identify_element("(//a[@class='oxd-topbar-body-nav-tab-item'])[2]", "XPATH", "My Leave")
        myleave_page.click()
        time.sleep(2)
        print("Successfully navigated to myleave page")


    def navigate_entitlements(self, option):
        print("Navigating to entitlements ...")
        entitlements_page = self.helper.identify_element("//span[@class='oxd-topbar-body-nav-tab-item']", "XPATH", " Entitlements")
        entitlements_page.click()
        time.sleep(5)
        sub_module = self.helper.identify_element(option, "XPATH", "entitlements")
        sub_module.click()
        time.sleep(3)
        print("Successfully navigated to entitlements page")

    def navigate_reports(self, option):
        print("Navigating to reports ...")
        reports_page = self.helper.identify_element('//*[text()="Reports "]',"XPATH","Reports")
        reports_page.click()
        time.sleep(2)
        sub_module = self.helper.identify_element(option, "XPATH", "reports")
        sub_module.click()
        time.sleep(3)
        print("Successfully navigated to reports page")



    def navigate_configure(self, option):
        print("Navigating to configure ...")
        add_entitlements_page = self.helper.identify_element("(//span[@class='oxd-topbar-body-nav-tab-item'])[3]", "XPATH",
                                                             "Configure")
        add_entitlements_page.click()
        time.sleep(2)
        sub_module = self.helper.identify_element(option, "XPATH", "configure")
        sub_module.click()
        time.sleep(3)
        print("Successfully navigated to configure page")
    def navigate_leave_list(self):
        print("Navigating to leave list ...")
        add_entitlements_page = self.helper.identify_element('//*[text()="Leave List"]', "XPATH","Leave list")
        add_entitlements_page.click()
        time.sleep(2)
        print("Successfully navigated to leave list page")

    def navigate_assign_leave(self):
        print("Navigating to assign leave  ...")
        add_entitlements_page = self.helper.identify_element('//*[text()="Assign Leave"]', "XPATH", "Assign Leave ")
        add_entitlements_page.click()
        time.sleep(2)
        print("Successfully navigated to assign leave page")


if __name__ == "__main__":
    # Test code or Driver code
    from libUtils.seleniumUtils.driver_manager import DriverManager
    # Driver Initialization
    dm = DriverManager()
    # Navigate to Home --> PIM
    obj = LeavePage(dm.driver)
    #obj.navigate_to_apply()
    #obj.navigate_to_my_leave()
    #add_entitlements = "//a[@class='oxd-topbar-body-nav-tab-link']"
    #employee_entitlements = "(//a[@class='oxd-topbar-body-nav-tab-link'])[2]"
    #my_entitlements = "(//a[@class='oxd-topbar-body-nav-tab-link'])[3]"
    #obj.navigate_entitlements(add_entitlements)
    #obj.navigate_entitlements(employee_entitlements)
    #obj.navigate_entitlements(my_entitlements)

    #leave_entitlements_and_usage_report="//a[@class='oxd-topbar-body-nav-tab-link']"
    #my_leave_entitlements_and_usage_report = "(//a[@class='oxd-topbar-body-nav-tab-link'])[2]"
    #obj.navigate_reports(leave_entitlements_and_usage_report)
    #obj.navigate_reports(my_leave_entitlements_and_usage_report)

    #leave_period = "//a[@class='oxd-topbar-body-nav-tab-link']"
    #leave_types= "(//a[@class='oxd-topbar-body-nav-tab-link'])[2]"
    #work_week= "(//a[@class='oxd-topbar-body-nav-tab-link'])[3]"
    #holidays= "(//a[@class='oxd-topbar-body-nav-tab-link'])[4]"
    #obj.navigate_configure(leave_period)
    #obj.navigate_configure(leave_types)
    #obj.navigate_configure(work_week)
    #obj.navigate_configure(holidays)
    #obj.navigate_leave_list()
    obj.navigate_assign_leave()


