__author__="pravallikakolakaluri"

import time
from libUtils.seleniumUtils.weblocate_helper import WebLocateHelper
from home_page import HomePage


class PIMPage:

    def __init__(self, driver):
        home_page = HomePage(driver)
        home_page.navigate_to_pim()
        self.helper = WebLocateHelper(driver)

    def navigate_to_configuration(self, option):
        print("Navigating to configuration page ...")
        configuration = self.helper.identify_element("//span[@class='oxd-topbar-body-nav-tab-item']", "XPATH", "configuration")
        configuration.click()
        time.sleep(3)
        sub_mobule = self.helper.identify_element(option, "XPATH", "configuration")
        sub_mobule.click()
        time.sleep(3)
        # Write your logic here
        print(f"Successfully configuration page.")

    def navigate_to_employee_list(self):
        print("Navigating to employee list page ...")
        employee_list = self.helper.identify_element("//a[@class='oxd-topbar-body-nav-tab-item']", "XPATH", "employee list")
        employee_list.click()
        time.sleep(4)
        # Write your logic here
        print(f"Successfully navigated employee list page.")

    def navigate_to_add_employee(self):
        print("Navigating to add employee page ...")
        add_employee = self.helper.identify_element("(//a[@class='oxd-topbar-body-nav-tab-item'])[2]", "XPATH","add employee")
        add_employee.click()
        time.sleep(4)
        # Write your logic here
        print(f"Successfully navigated to add employee.")

    def navigate_to_reports(self):
        print("Navigating to report page ...")
        report = self.helper.identify_element("(//a[@class='oxd-topbar-body-nav-tab-item'])[3]", "XPATH", "report")
        report.click()
        time.sleep(4)
        # Write your logic here
        print(f"Successfully navigated to reports page.")


if __name__ == "__main__":
    # Test code or Driver code
    from libUtils.seleniumUtils.driver_manager import DriverManager
    # Driver Initialization
    dm = DriverManager()
    # Navigate to Home --> PIM
    obj = PIMPage(dm.driver)
    time.sleep(2)
    #obj.navigate_to_employee_list()
    #obj.navigate_to_add_employee()
    #obj.navigate_to_reports()
    Optional_fieled="//a[@class='oxd-topbar-body-nav-tab-link']"
    Custom_fieled="(//a[@class='oxd-topbar-body-nav-tab-link'])[2]"
    Data_import="(//a[@class='oxd-topbar-body-nav-tab-link'])[3]"
    Reporting_methods="(//a[@class='oxd-topbar-body-nav-tab-link'])[4]"
    Teminational_resons="(//a[@class='oxd-topbar-body-nav-tab-link'])[5]"

    obj.navigate_to_configuration(Data_import)
    #time.sleep(4)



