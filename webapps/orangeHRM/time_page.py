from home_page import HomePage
from libUtils.seleniumUtils.weblocate_helper import WebLocateHelper
import time


class TimePage:

    def __init__(self, driver):
        home_page = HomePage(driver)
        home_page.navigate_to_time()
        self.helper = WebLocateHelper(driver)

    def navigate_to_time_sheets(self, option):
       time_sheet = self.helper.identify_element("//*[@class='oxd-icon bi-chevron-down']", "XPATH", "Timesheet")
       time_sheet.click()
       time.sleep(3)
       sub_mobule = self.helper.identify_element(option, "XPATH", "Timesheet")
       sub_mobule.click()
       time.sleep(3)

    def navigate_to_attendance(self, option):
        attendence=self.helper.identify_element('//*[text()="Attendance "]',"XPATH",'Attendence')
        attendence.click()
        time.sleep(3)
        sub_mobule = self.helper.identify_element(option, "XPATH", "Attendence")
        sub_mobule.click()
        time.sleep(3)

    def navigate_to_reports(self, option):
        reports=self.helper.identify_element('//*[text()="Reports "]',"XPATH",'Reports')
        reports.click()
        time.sleep(3)
        sub_mobule = self.helper.identify_element(option, "XPATH", "Reports")
        sub_mobule.click()
        time.sleep(3)

    def navigate_to_project_info(self, option):
        project_info = self.helper.identify_element('//*[text()="Project Info "]', "XPATH", 'Project info')
        project_info.click()
        time.sleep(3)
        sub_mobule = self.helper.identify_element(option, "XPATH", "Project info")
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
    #my_timesheet="//a[@class='oxd-topbar-body-nav-tab-link']"
    #employe_timesheet="//*[text()='Employee Timesheets']"
    #obj.navigate_to_time_sheets(employe_timesheet)
    #my_report='//*[text()="My Records"]'
    #punch_inout='//*[text()="Punch In/Out"]'
    #employee_records='//*[text()="Employee Records"]'
    #configaration='//*[text()="Configuration"]'
    #obj.navigate_to_attendance(configaration)
    #projects_reports='//*[text()="Project Reports"]'
    #employee_reports='//*[text()="Employee Reports"]'
    #attendance_summary='//*[text()="Attendance Summary"]'
    #obj.navigate_to_reports(attendance_summary)
    #customers='//*[text()="Customers"]'
    projects='//*[text()="Projects"]'
    obj.navigate_to_project_info(projects)