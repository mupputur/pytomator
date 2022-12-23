__authors__ = ['mupputuri', 'pravallika']

import time
from libUtils.seleniumUtils.weblocate_helper import WebLocateHelper
from pim_page import PIMPage
from libUtils.seleniumUtils.driver_manager import DriverManager
from libUtils.seleniumUtils.locators import EmployeeListPageLocators as lp
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver

class EmployeeListPage:
    def __init__(self,driver):
        pim_page = PIMPage(driver)
        pim_page.navigate_to_employee_list()
        self.helper = WebLocateHelper(driver)

    def search(self, emp_name,empid,Supervisor):
        employee_name = self.helper.identify_element(lp.EMPLOYEE_NAME_TB_XPATH_LOC[0],lp.EMPLOYEE_NAME_TB_XPATH_LOC[1],"employee_name")
        self.helper.enter_text(employee_name, emp_name)
        time.sleep(3)
        emp_id = self.helper.identify_element(lp.EMP_ID_TB_XPATH_LOC[0],lp.EMP_ID_TB_XPATH_LOC[1], "emp_id")
        self.helper.enter_text(emp_id, empid)
        time.sleep(3)
        status = self.helper.identify_element(lp.STATUS_BT_XPATH_LOC[0],lp.STATUS_BT_XPATH_LOC[1], "status")
        status.click()
        time.sleep(2)
        emp_status = self.helper.identify_element(lp.EMP_STATUS_BT_XPATH_LOC[0],lp.EMP_STATUS_BT_XPATH_LOC[1], "emp_status")
        emp_status.click()
        time.sleep(3)
        include = self.helper.identify_element(lp.INCLUDE_BT_XPATH_LOC[0],lp.INCLUDE_BT_XPATH_LOC[1], "include")
        include.click()
        time.sleep(3)
        Supervisor_Name = self.helper.identify_element(lp.SUPERVISOR_NAME_TB_XPATH_LOC[0],lp.SUPERVISOR_NAME_TB_XPATH_LOC[1],"Supervisor_name")
        self.helper.enter_text(Supervisor_Name, Supervisor)
        self.helper.click_on(Supervisor_Name, '')
        time.sleep(3)
        # Supervisor_Name.click()
        job_title = self.helper.identify_element(lp.JOB_TITLE_BT_XPATH_LOC[0],lp.JOB_TITLE_BT_XPATH_LOC[1], "job_title")
        job_title.click()
        time.sleep(2)
        job_title_is = self.helper.identify_element(lp.JOB_TITLE_IS_BT_XPATH_LOC[0],lp.JOB_TITLE_IS_BT_XPATH_LOC[1], "job_title_is")
        job_title_is.click()
        time.sleep(3)
        sub_unit = self.helper.identify_element(lp.SUB_UNIT_BT_XPATH_LOC[0],lp.SUB_UNIT_BT_XPATH_LOC[1], "sub_unit")
        sub_unit.click()
        time.sleep(2)
        sub_unit_is = self.helper.identify_element(lp.SUB_UNIT_IS_BT_XPATH_LOC[0],lp.SUB_UNIT_IS_BT_XPATH_LOC[1], "sub_unit_is")
        sub_unit_is.click()
        time.sleep(3)
        reset = self.helper.identify_element(lp.RESET_BT_XPATH_LOC[0],lp.RESET_BT_XPATH_LOC[1], "reset")
        reset.click()
        time.sleep(5)

    def reset(self):
        employee_name = self.helper.identify_element(lp.EMPLOYEE_NAME_TB_XPATH_LOC[0],lp.EMPLOYEE_NAME_TB_XPATH_LOC[1],"employee_name")
        self.helper.enter_text(employee_name, "Linda Jane Anderson")
        time.sleep(3)
        emp_id=self.helper.identify_element(lp.EMP_ID_TB_XPATH_LOC[0],lp.EMP_ID_TB_XPATH_LOC[1],"emp_id")
        self.helper.enter_text(emp_id, "102")
        time.sleep(3)
        status = self.helper.identify_element(lp.STATUS_BT_XPATH_LOC[0],lp.STATUS_BT_XPATH_LOC[1], "status")
        status.click()
        time.sleep(2)
        emp_status=self.helper.identify_element(lp.EMP_STATUS_BT_XPATH_LOC[0],lp.EMP_STATUS_BT_XPATH_LOC[1], "emp_status")
        emp_status.click()
        time.sleep(3)
        include=self.helper.identify_element(lp.INCLUDE_BT_XPATH_LOC[0],lp.INCLUDE_BT_XPATH_LOC[1], "include")
        include.click()
        time.sleep(3)
        Supervisor_Name=self.helper.identify_element(lp.SUPERVISOR_NAME_TB_XPATH_LOC[0],lp.SUPERVISOR_NAME_TB_XPATH_LOC[1], "Supervisor_Name")
        self.helper.enter_text(Supervisor_Name, "Kevin  Mathews")
        self.helper.click_on(Supervisor_Name, '')
        time.sleep(3)
        #Supervisor_Name.click()
        job_title=self.helper.identify_element(lp.JOB_TITLE_BT_XPATH_LOC[0],lp.JOB_TITLE_BT_XPATH_LOC[1], "job_title")
        job_title.click()
        time.sleep(2)
        job_title_is=self.helper.identify_element(lp.JOB_TITLE_IS_BT_XPATH_LOC[0],lp.JOB_TITLE_IS_BT_XPATH_LOC[1], "job_title_is")
        job_title_is.click()
        time.sleep(3)
        sub_unit=self.helper.identify_element(lp.SUB_UNIT_BT_XPATH_LOC[0],lp.SUB_UNIT_BT_XPATH_LOC[1], "sub_unit")
        sub_unit.click()
        time.sleep(2)
        sub_unit_is = self.helper.identify_element(lp.SUB_UNIT_IS_BT_XPATH_LOC[0],lp.SUB_UNIT_IS_BT_XPATH_LOC[1], "sub_unit_is")
        sub_unit_is.click()
        time.sleep(3)
        reset = self.helper.identify_element(lp.RESET_BT_XPATH_LOC[0],lp.RESET_BT_XPATH_LOC[1], "reset")
        reset.click()
        time.sleep(5)

    def get_all_records(self):
        employee_list = self.helper.identify_element(lp.EMP_LIST_BT_XPATH_LOC[0],lp.EMP_LIST_BT_XPATH_LOC[1], "employee list")
        employee_list.click()
        time.sleep(4)

if __name__ == "__main__":
    dm = DriverManager()
    emp_list = EmployeeListPage(dm.driver)
    #emp_list.get_all_records()
    emp_list.reset()
    #keywords ={"Employee Name":"Linda Jane Anderson"}
    #emp_list.search(**{"Employee Name" : "Linda Jane Anderson"})
    #emp_list.search('Anthony','4567','Linda Jane Anderson')





