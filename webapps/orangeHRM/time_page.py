from home_page import HomePage
from libUtils.seleniumUtils.weblocate_helper import WebLocateHelper
from libUtils.seleniumUtils.locators import TimePageLocators as lp
import time


class TimePage:

    def __init__(self, driver):
        home_page = HomePage(driver)
        home_page.navigate_to_time()
        self.helper = WebLocateHelper(driver)

    def navigate_to_time_sheets(self, option,identifier):
       time_sheet = self.helper.identify_element(lp.TIMESHEET_BT_XPATH_LOC[0],
                                                  lp.TIMESHEET_BT_XPATH_LOC[1], "Timesheet")
       time_sheet.click()
       time.sleep(3)
       sub_mobule = self.helper.identify_element(option,identifier, "Timesheet")
       sub_mobule.click()
       time.sleep(3)

    def navigate_to_attendance(self, option,identifier):
        attendence=self.helper.identify_element(lp.ATTENDENCE_BT_XPATH_LOC[0],
                                                lp.ATTENDENCE_BT_XPATH_LOC[1],"Attendence")
        attendence.click()
        time.sleep(3)
        sub_mobule = self.helper.identify_element(option,identifier, "Attendence")
        sub_mobule.click()
        time.sleep(3)

    def navigate_to_reports(self, option,identifier):
        reports=self.helper.identify_element(lp.REPORTS_BT_XPATH_LOC[0],
                                             lp.REPORTS_BT_XPATH_LOC[1],"Reports")
        reports.click()
        time.sleep(3)
        sub_mobule = self.helper.identify_element(option,identifier, "Reports")
        sub_mobule.click()
        time.sleep(3)

    def navigate_to_project_info(self, option,identifier):
        project_info = self.helper.identify_element(lp.PROJECT_INFO_BT_XPATH_LOC[0],
                                                    lp.PROJECT_INFO_BT_XPATH_LOC[1], "Project info")
        project_info.click()
        time.sleep(3)
        sub_mobule = self.helper.identify_element(option,identifier, "Project info")
        sub_mobule.click()
        time.sleep(3)

if __name__ == "__main__":
    # Test code or Driver code
    from libUtils.seleniumUtils.driver_manager import DriverManager

    # Driver Initialization
    dm = DriverManager()
    # Navigate to Home --> PIM
    obj = TimePage(dm.driver)
    time.sleep(3)
    #TIMESHEET-----------
    #my_timesheet=lp.MY_TIMESHEET_BT_XPATH_LOC[0]
    #obj.navigate_to_time_sheets(my_timesheet,lp.MY_TIMESHEET_BT_XPATH_LOC[1])
    #employe_timesheet=lp.EMPLOYEE_TIMESHEET_BT_XPATH_LOC[0]
    #obj.navigate_to_time_sheets(employe_timesheet,lp.EMPLOYEE_TIMESHEET_BT_XPATH_LOC[1])

    # ATTENDENCE-----------
    #my_record=lp.MY_RECORDS_BT_XPATH_LOC[0]
    #obj.navigate_to_attendance(my_record, lp.MY_RECORDS_BT_XPATH_LOC[1])
    #punch_inout=lp.PUNCH_INOUT_BT_XPATH_LOC[0]
    #obj.navigate_to_attendance(punch_inout, lp.PUNCH_INOUT_BT_XPATH_LOC[1])
    #employee_records=lp.EMPLOYEE_RECORDS_BT_XPATH_LOC[0]
    #obj.navigate_to_attendance(employee_records, lp.EMPLOYEE_RECORDS_BT_XPATH_LOC[1])
    #configaration=lp.CONFIGARATION_BT_XPATH_LOC[0]
    #obj.navigate_to_attendance(configaration,lp.CONFIGARATION_BT_XPATH_LOC[1])
    #REPORT------------------
    #projects_reports=lp.PROJECT_REPORTS_BT_XPATH_LOC[0]
    #obj.navigate_to_reports(projects_reports, lp.PROJECT_REPORTS_BT_XPATH_LOC[1])
    #employee_reports=lp.EMPLOYEE_REPORTS_BT_XPATH_LOC[0]
    #obj.navigate_to_reports(employee_reports, lp.EMPLOYEE_REPORTS_BT_XPATH_LOC[1])
    #attendance_summary=lp.ATTENDENCE_SUMMARY_BT_XPATH_LOC[0]
    #obj.navigate_to_reports(attendance_summary,lp.ATTENDENCE_SUMMARY_BT_XPATH_LOC[1])

    #PROJECT_INFO-------------------
    #customers=lp.CUSTOMERS_BT_XPATH_LOC[0]
    #obj.navigate_to_project_info(customers,lp.CUSTOMERS_BT_XPATH_LOC[1])
    projects=lp.PROJECTS_BT_XPATH_LOC[0]
    obj.navigate_to_project_info(projects,lp.PROJECTS_BT_XPATH_LOC[1])