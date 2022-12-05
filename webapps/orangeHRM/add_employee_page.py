__authors__ = ['mupputuri', 'RadhaKrishna']
import time
from libUtils.seleniumUtils.weblocate_helper import WebLocateHelper
from pim_page import PIMPage
from libUtils.seleniumUtils.driver_manager import DriverManager




class AddEmployeePage:

    def __init__(self, driver):
        pim_page = PIMPage(driver)
        pim_page.navigate_to_add_employee()
        self.helper = WebLocateHelper(driver)


    def add_employee_with_out_login_details(self, **details):
        firstname = self.helper.identify_element('//input[@class="oxd-input oxd-input--active orangehrm-firstname"]', "XPATH", "firstname")
        self.helper.enter_text(firstname, "Radha")
        self.helper.click_on(firstname, '')
        time.sleep(5)
        middlename = self.helper.identify_element('//input[@class="oxd-input oxd-input--active orangehrm-middlename"]',"XPATH", "middlename")
        self.helper.enter_text(middlename, "Krishna")
        self.helper.click_on(middlename, '')
        time.sleep(5)
        lastname = self.helper.identify_element('//input[@class="oxd-input oxd-input--active orangehrm-lastname"]',"XPATH", "lastname")
        self.helper.enter_text(lastname, "Raju")
        self.helper.click_on(lastname, '')
        time.sleep(5)
        save = self.helper.identify_element("//button[@type='submit']", "XPATH", "click_save")
        save.click()
        time.sleep(5)

    def add_employee_with_login_details(self, status=True, **details):
        firstname = self.helper.identify_element('//input[@class="oxd-input oxd-input--active orangehrm-firstname"]',"XPATH", "firstname")
        self.helper.enter_text(firstname, "Radha")
        self.helper.click_on(firstname, '')
        time.sleep(3)
        middlename = self.helper.identify_element('//input[@class="oxd-input oxd-input--active orangehrm-middlename"]',"XPATH", "middlename")
        self.helper.enter_text(middlename, "Raju")
        self.helper.click_on(middlename, '')
        time.sleep(3)
        lastname = self.helper.identify_element('//input[@class="oxd-input oxd-input--active orangehrm-lastname"]',"XPATH", "lastname")
        self.helper.enter_text(lastname, "Krishna")
        self.helper.click_on(lastname, '')
        time.sleep(3)
        enable_button = self.helper.identify_element("//span[@class='oxd-switch-input oxd-switch-input--active --label-right']", "XPATH", "click_enable_button")
        enable_button.click()
        time.sleep(3)
        username = self.helper.identify_element('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input',"XPATH", "username")
        self.helper.enter_text(username, "Radha")
        self.helper.click_on(username, '')
        time.sleep(3)
        password = self.helper.identify_element('//input[@type="password"]',"XPATH", "password")
        self.helper.enter_text(password, "Krishna@9052")
        self.helper.click_on(password, '')
        time.sleep(3)
        confirm_password = self.helper.identify_element('(//input[@type="password"])[2]',"XPATH", "confirm_password")
        self.helper.enter_text(confirm_password, "Krishna@9052")
        self.helper.click_on(confirm_password, '')
        time.sleep(3)
        save = self.helper.identify_element("//button[@type='submit']", "XPATH", "click_save")
        save.click()
        time.sleep(5)


    def get_records(self):
        add_employee = self.helper.identify_element("(//a[@class='oxd-topbar-body-nav-tab-item'])[2]", "XPATH","add employee")
        add_employee.click()
        time.sleep(4)

if __name__ == "__main__":
    dm = DriverManager()
    obj_add_employee = AddEmployeePage(dm.driver)
    obj_add_employee.get_records()
    #obj_add_employee.add_employee_with_out_login_details()
    obj_add_employee.add_employee_with_login_details()