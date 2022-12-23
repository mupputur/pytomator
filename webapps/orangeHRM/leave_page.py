from home_page import HomePage
from libUtils.seleniumUtils.weblocate_helper import WebLocateHelper
from libUtils.seleniumUtils.locators import LeavePageLocators as lp
import time

class LeavePage:

    def __init__(self, driver):
        home_page = HomePage(driver)
        home_page.navigate_to_leave()
        self.helper = WebLocateHelper(driver)

    def navigate_to_apply(self):
        print("Navigating to apply ...")
        apply_page = self.helper.identify_element(lp.APPLY_PAGE_BT_XPATH_LOC[0],lp.APPLY_PAGE_BT_XPATH_LOC[1], "Apply")
        apply_page.click()
        time.sleep(2)
        print("Successfully navigated to apply page")

    def navigate_to_my_leave(self):
        print("Navigating to myleave ...")
        myleave_page = self.helper.identify_element(lp.MYLEAVE_PAGE_BT_XPATH_LOC[0],lp.MYLEAVE_PAGE_BT_XPATH_LOC[1], "My Leave")
        myleave_page.click()
        time.sleep(2)
        print("Successfully navigated to myleave page")


    def navigate_entitlements(self, option,identifier):
        print("Navigating to entitlements ...")
        entitlements_page = self.helper.identify_element(lp.ENTITLEMENTS_PAGE_BT_XPATH_LOC[0],lp.ENTITLEMENTS_PAGE_BT_XPATH_LOC[1], " Entitlements")
        entitlements_page.click()
        time.sleep(5)
        sub_module = self.helper.identify_element(option,identifier, "entitlements")
        sub_module.click()
        time.sleep(3)
        print("Successfully navigated to entitlements page")

    def navigate_reports(self, option,identifier):
        print("Navigating to reports ...")
        reports_page = self.helper.identify_element(lp.REPORTS_PAGE_BT_XPATH_LOC[0],lp.REPORTS_PAGE_BT_XPATH_LOC[1],"Reports")
        reports_page.click()
        time.sleep(2)
        sub_module = self.helper.identify_element(option,identifier, "reports")
        sub_module.click()
        time.sleep(3)
        print("Successfully navigated to reports page")



    def navigate_configure(self, option,identifier):
        print("Navigating to configure ...")
        add_entitlements_page = self.helper.identify_element(lp.ADD_ENTITLEMENTS_CONFIGURE_PAGE_BT_XPATH_LOC[0],
                                                             lp.ADD_ENTITLEMENTS_CONFIGURE_PAGE_BT_XPATH_LOC[1], "Configure")
        add_entitlements_page.click()
        time.sleep(2)
        sub_module = self.helper.identify_element(option,identifier, "configure")
        sub_module.click()
        time.sleep(3)
        print("Successfully navigated to configure page")
    def navigate_leave_list(self):
        print("Navigating to leave list ...")
        add_entitlements_page = self.helper.identify_element(lp.ADD_ENTITLEMENTS_LEAVE_LIST_PAGE_BT_XPATH_LOC[0],
                                                             lp.ADD_ENTITLEMENTS_LEAVE_LIST_PAGE_BT_XPATH_LOC[1],"Leave list")
        add_entitlements_page.click()
        time.sleep(2)
        print("Successfully navigated to leave list page")

    def navigate_assign_leave(self):
        print("Navigating to assign leave  ...")
        add_entitlements_page = self.helper.identify_element(lp.ADD_ENTITLEMENTS_ASSIGN_LEAVE_PAGE_BT_XPATH_LOC[0],
                                                             lp.ADD_ENTITLEMENTS_ASSIGN_LEAVE_PAGE_BT_XPATH_LOC[1], "Assign Leave ")
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

        #CONFIGURE-----
    #leave_period = lp.LEAVE_PERIOD_BT_XPATH_LOC[0]
    #leave_types= lp.LEAVE_TYPES_BT_XPATH_LOC[0]
    #work_week= lp.WORK_WEEK_BT_XPATH_LOC[0]
    #holidays= lp.HOLIDAYS_BT_XPATH_LOC[0]
    #obj.navigate_configure(leave_period,lp.LEAVE_PERIOD_BT_XPATH_LOC[1])
    #obj.navigate_configure(leave_types,lp.LEAVE_TYPES_BT_XPATH_LOC[1])
    #obj.navigate_configure(work_week,lp.WORK_WEEK_BT_XPATH_LOC[1])
    #obj.navigate_configure(holidays,lp.HOLIDAYS_BT_XPATH_LOC[1])

    #obj.navigate_leave_list()
    #obj.navigate_assign_leave()


