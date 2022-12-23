__authors__ = ['mupputuri', 'RadhaKrishna']
import time
from libUtils.seleniumUtils.weblocate_helper import WebLocateHelper
from webapps.orangeHRM.pim_page import PIMPage
from libUtils.seleniumUtils.driver_manager import DriverManager
from libUtils.seleniumUtils.locators import AddEmployeePageLocators as lp

class AddEmployeePage:

    def __init__(self, driver):
        pim_page = PIMPage(driver)
        pim_page.navigate_to_add_employee()
        self.helper = WebLocateHelper(driver)

    def add_employee_with_out_login_details(self, first_name,middle_name,last_name):
        firstname = self.helper.identify_element(lp.FIRSTNAME_TB_XPATH_LOC[0],lp.FIRSTNAME_TB_XPATH_LOC[1], "firstname")
        self.helper.enter_text(firstname,first_name)
        time.sleep(5)
        middlename = self.helper.identify_element(lp.MIDDLENAME_TB_XPATH_LOC[0],lp.MIDDLENAME_TB_XPATH_LOC[1], "middlename")
        self.helper.enter_text(middlename,middle_name)
        time.sleep(5)
        lastname = self.helper.identify_element(lp.LASTNAME_TB_XPATH_LOC[0],lp.LASTNAME_TB_XPATH_LOC[1], "lastname")
        self.helper.enter_text(lastname, last_name)
        time.sleep(5)
        save = self.helper.identify_element(lp.SAVE_BT_XPATH_LOC[0],lp.SAVE_BT_XPATH_LOC[1], "click_save")
        save.click()
        time.sleep(5)
        element= self.helper.wait(lp.WAIT_BT_XPATH_LOC)
        return element


    def add_employee_with_login_details(self,first_name,middle_name,last_name,user_name,_password,_confirm_password):
        firstname = self.helper.identify_element(lp.FIRSTNAME_TB_XPATH_LOC[0],lp.FIRSTNAME_TB_XPATH_LOC[1], "firstname")
        self.helper.enter_text(firstname,first_name)
        time.sleep(3)
        middlename = self.helper.identify_element(lp.MIDDLENAME_TB_XPATH_LOC[0],lp.MIDDLENAME_TB_XPATH_LOC[1], "middlename")
        self.helper.enter_text(middlename, middle_name)
        time.sleep(3)
        lastname = self.helper.identify_element(lp.LASTNAME_TB_XPATH_LOC[0],lp.LASTNAME_TB_XPATH_LOC[1], "lastname")
        self.helper.enter_text(lastname, last_name)
        time.sleep(3)
        enable_button = self.helper.identify_element(lp.ENABLE_BT_XPATH_LOC[0],lp.ENABLE_BT_XPATH_LOC[1], "click_enable_button")
        enable_button.click()
        time.sleep(3)
        username = self.helper.identify_element(lp.USERNAME_TB_XPATH_LOC[0],lp.USERNAME_TB_XPATH_LOC[1], "username")
        self.helper.enter_text(username, user_name)
        time.sleep(3)
        password = self.helper.identify_element(lp.PASSWORD_TB_XPATH_LOC[0],lp.PASSWORD_TB_XPATH_LOC[1], "password")
        self.helper.enter_text(password, _password)
        time.sleep(3)
        confirm_password = self.helper.identify_element(lp.CONFIRM_PASSWORD_TB_XPATH_LOC[0],lp.CONFIRM_PASSWORD_TB_XPATH_LOC[1], "confirm_password")
        self.helper.enter_text(confirm_password,_confirm_password)
        time.sleep(3)
        save = self.helper.identify_element(lp.SAVE_BT_XPATH_LOC[0],lp.SAVE_BT_XPATH_LOC[1], "click_save")
        save.click()
        time.sleep(5)
        element = self.helper.wait(lp.WAIT_BT_XPATH_LOC)
        return element


    def get_records(self):
        add_employee = self.helper.identify_element(lp.ADD_EMPLOYEE_TB_XPATH_LOC[0],lp.ADD_EMPLOYEE_TB_XPATH_LOC[1],"add employee")
        add_employee.click()
        time.sleep(4)

if __name__ == "__main__":
    dm = DriverManager()
    obj_add_emp = AddEmployeePage(dm.driver)
    obj_add_emp.get_records()
    #obj_add_emp.add_employee_with_out_login_details("sree","laxmi","devi")
    #obj_add_emp.add_employee_with_login_details("vallika","valli","kolakaluri","vallika","Valli@123","Valli@123")