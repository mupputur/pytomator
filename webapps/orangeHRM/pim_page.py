__author__="pravallikakolakaluri"

import time
from libUtils.seleniumUtils.weblocate_helper import WebLocateHelper
from home_page import HomePage
from libUtils.seleniumUtils.locators import PIMPAGELocators as lp

class PIMPage:

    def __init__(self, driver):
        home_page = HomePage(driver)
        home_page.navigate_to_pim()
        self.helper = WebLocateHelper(driver)

    def navigate_to_configuration(self, option,identifier):
        print("Navigating to configuration page ...")
        configuration = self.helper.identify_element(lp.CONFIGURATION_BT_XPATH_LOC[0],lp.CONFIGURATION_BT_XPATH_LOC[1], "configuration")
        configuration.click()
        time.sleep(3)
        sub_mobule = self.helper.identify_element(option,identifier, "configuration")
        sub_mobule.click()
        time.sleep(3)
        # Write your logic here
        print(f"Successfully configuration page.")

    def navigate_to_employee_list(self):
        print("Navigating to employee list page ...")
        employee_list = self.helper.identify_element(lp.EMP_LIST_BT_XPATH_LOC[0],lp.EMP_LIST_BT_XPATH_LOC[1], "employee list")
        employee_list.click()
        time.sleep(4)
        # Write your logic here
        print(f"Successfully navigated employee list page.")

    def navigate_to_add_employee(self):
        print("Navigating to add employee page ...")
        add_employee = self.helper.identify_element(lp.ADD_EMP_BT_XPATH_LOC[0],lp.ADD_EMP_BT_XPATH_LOC[1],"add employee")
        add_employee.click()
        time.sleep(4)
        # Write your logic here
        print(f"Successfully navigated to add employee.")

    def navigate_to_reports(self):
        print("Navigating to report page ...")
        report = self.helper.identify_element(lp.REPORT_BT_XPATH_LOC[0],lp.REPORT_BT_XPATH_LOC[1], "report")
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
    #Optional_fieled=lp.OPT_FIELD_BT_XPATH_LOC[0]
    #Custom_fieled=lp.CUSTOM_FIELD_BT_XPATH_LOC[0]
    #Data_import=lp.DATA_IMPORT_BT_XPATH_LOC[0]
    #Reporting_methods=lp.REPORTING_METHODS_BT_XPATH_LOC[0]
    #Teminational_resons=lp.TERMINATIONAL_REASONS_BT_XPATH_LOC[0]

    #obj.navigate_to_configuration(Optional_fieled,lp.OPT_FIELD_BT_XPATH_LOC[1])
    #obj.navigate_to_configuration(Custom_fieled, lp.OPT_FIELD_BT_XPATH_LOC[1])
    #obj.navigate_to_configuration(Data_import, lp.OPT_FIELD_BT_XPATH_LOC[1])
    #obj.navigate_to_configuration(Reporting_methods, lp.OPT_FIELD_BT_XPATH_LOC[1])
    #obj.navigate_to_configuration(Teminational_resons, lp.OPT_FIELD_BT_XPATH_LOC[1])
    #ime.sleep(4)



