__authors__ = ['mupputuri', 'Sreedevi']

from libUtils.seleniumUtils.weblocate_helper import WebLocateHelper
from pim_page import PIMPage
from libUtils.seleniumUtils.driver_manager import DriverManager
import time


class PIMConfigurationPage:

    def __init__(self, driver):
        pim_page = PIMPage(driver)
        #self.Custom_field = '//*[text()="Custom Fields"]'
        #pim_page.navigate_to_configuration(self.Custom_field)
        self.Reporting_Methods = '//*[text()="Reporting Methods"]'
        pim_page.navigate_to_configuration(self.Reporting_Methods)
        #self.Termination_Reasons = '//*[text()="Termination Reasons"]'
        #pim_page.navigate_to_configuration(self.Termination_Reasons)
        #self.Optional_Fields = '//*[text()="Optional Fields"]'
        #pim_page.navigate_to_configuration(self.Optional_Fields)
        self.helper = WebLocateHelper(driver)

    def enable_optional_fields(self, **filed_values):
        for v, k in filed_values.items():
            # print(k)
            text = filed_values.values()
            print(text)
            elements = self.helper.identify_element('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div/div/div/p',"XPATH", "elements")
            # print(elements)
            for i in range(len(elements)):
                # print(i)
                text2 = elements[i].text
                text3 = text2.split(",")
                print(text3)
                if (list(text)) == (text3):
                    element = self.helper.identify_element("//span[@class='oxd-switch-input oxd-switch-input--active --label-right']", "XPATH","elements")[i]
                    element.click()
                    time.sleep(5)
                    save = self.helper.identify_element("//button[@type='submit']", "XPATH", "click_save")
                    save.click()
                    time.sleep(5)

    def disable_optional_fields(self, **filed_values):
        for v, k in filed_values.items():
            #print(k)
            text = filed_values.values()
            #print(text)
            elements = self.helper.identify_element('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div/div/div/p',"XPATH", "elements")
            # print(elements)
            for i in range(len(elements)):
                #print(i)
                text2 = elements[i].text
                text3 = text2.split(",")
                print(text3)
                if (list(text)) == (text3):
                    element = self.helper.identify_element("//span[@class='oxd-switch-input oxd-switch-input--active --label-right']", "XPATH", "elements")[i]
                    element.click()
                    time.sleep(5)
                    save = self.helper.identify_element("//button[@type='submit']", "XPATH", "click_save")
                    save.click()
                    time.sleep(5)

    def enable_all_optional_fields(self):
        enable_optional_fields = self.helper.identify_element("//span[@class='oxd-switch-input oxd-switch-input--active --label-right']", "XPATH", "PIM")
        enable_optional_fields.click()
        time.sleep(4)
        enable_optional_fields = self.helper.identify_element("(//span[@class='oxd-switch-input oxd-switch-input--active --label-right'])[1]", "XPATH", "PIM")
        enable_optional_fields.click()
        time.sleep(4)
        enable_optional_fields = self.helper.identify_element("(//span[@class='oxd-switch-input oxd-switch-input--active --label-right'])[2]", "XPATH", "PIM")
        enable_optional_fields.click()
        time.sleep(4)
        enable_optional_fields = self.helper.identify_element("(//span[@class='oxd-switch-input oxd-switch-input--active --label-right'])[3]", "XPATH", "PIM")
        enable_optional_fields.click()
        time.sleep(4)
        save = self.helper.identify_element("//button[@type='submit']", "XPATH", "click_save")
        save.click()
        time.sleep(5)
    def disable_all_optional_fields(self):
        disable_optional_fields = self.helper.identify_element("//span[@class='oxd-switch-input oxd-switch-input--active --label-right']", "XPATH", "PIM")
        disable_optional_fields.click()
        time.sleep(4)
        disable_optional_fields = self.helper.identify_element("(//span[@class='oxd-switch-input oxd-switch-input--active --label-right'])[1]", "XPATH", "PIM")
        disable_optional_fields.click()
        time.sleep(4)
        disable_optional_fields = self.helper.identify_element("(//span[@class='oxd-switch-input oxd-switch-input--active --label-right'])[2]", "XPATH", "PIM")
        disable_optional_fields.click()
        time.sleep(4)
        disable_optional_fields = self.helper.identify_element("(//span[@class='oxd-switch-input oxd-switch-input--active --label-right'])[3]", "XPATH", "PIM")
        disable_optional_fields.click()
        time.sleep(4)
        save = self.helper.identify_element("//button[@type='submit']", "XPATH", "click_save")
        save.click()
        time.sleep(5)
    def add_custom_fields(self, **details):
        add = self.helper.identify_element("//button[@class='oxd-button oxd-button--medium oxd-button--secondary']", "XPATH", "click_add")
        add.click()
        time.sleep(5)

        for v, k in details.items():
            # print(k)
            text = details.values()
            print(text)
            elements = self.helper.identify_element('//*[text()="Custom Fields"]',"XPATH", "elements")
            time.sleep(5)
            print(elements)
            for i in range(len(elements)):
                # print(i)
                text2 = elements[i].text
                text3 = text2.split(",")
                print(text3)
                if (list(text)) == (text3):
                    element = self.helper.identify_element("//input[@class='oxd-input oxd-input--active']", "XPATH","elements")[i]
                    self.helper.enter_text(element, details)
                    element.click()
                    time.sleep(5)
                    #save = self.helper.identify_element("//button[@type='submit']", "XPATH", "click_save")
                    #save.click()
                    #time.sleep(5)

    def get_custom_filed_records(self):
        custom_field = self.helper.identify_element('//*[text()="Custom Fields"]', "XPATH", "Custom Field")
        custom_field.click()
        time.sleep(5)

    def add_reporting_method(self):
        add = self.helper.identify_element("//button[@class='oxd-button oxd-button--medium oxd-button--secondary']", "XPATH", "click_add")
        add.click()
        time.sleep(5)
        name = self.helper.identify_element("(//input[@class='oxd-input oxd-input--active'])[2]", "XPATH", "Name")
        self.helper.enter_text(name, "Sree")
        self.helper.click_on(name, '')
        time.sleep(5)
        save = self.helper.identify_element("//button[@type='submit']", "XPATH", "click_save")
        save.click()
        time.sleep(5)
    def get_reporting_method_records(self):
        reporting_method = self.helper.identify_element('//*[text()="Reporting Methods"]', "XPATH", "Reporting Method")
        reporting_method.click()
        time.sleep(5)
    def add_termination_reason(self):
        add = self.helper.identify_element("//button[@class='oxd-button oxd-button--medium oxd-button--secondary']",
                                           "XPATH", "click_add")
        add.click()
        time.sleep(5)
        name = self.helper.identify_element("(//input[@class='oxd-input oxd-input--active'])[2]", "XPATH", "Name")
        self.helper.enter_text(name, "Sree")
        self.helper.click_on(name, '')
        time.sleep(5)
        save = self.helper.identify_element("//button[@type='submit']", "XPATH", "click_save")
        save.click()
        time.sleep(5)

    def get_termination_reason_records(self):
        termination_reason = self.helper.identify_element('//*[text()="Termination Reasons"]', "XPATH", "Termination Reasons")
        termination_reason.click()
        time.sleep(5)

    def import_data(self):
        pass

if __name__ == "__main__":

    dm = DriverManager()
    #obj = PIMPage(dm.driver)
    #obj_optional_fields = PIMConfigurationPage(dm.driver)
    #obj_optional_fields.disable_optional_fields(**{"v1": "Show SSN field in Personal Details"})
    #obj_optional_fields.disable_optional_fields(**{"v2": "Show SIN field in Personal Details"})
    #time.sleep(5)
    #obj_optional_fields = PIMConfigurationPage(dm.driver)
    #obj_optional_fields.enable_optional_fields(**{"v1": "Show SSN field in Personal Details"})
    #obj_optional_fields.enable_optional_fields(**{"v2": "Show SIN field in Personal Details"})
    #time.sleep(5)
    #obj_enable_optional_fields = PIMConfigurationPage(dm.driver)
    #obj_enable_optional_fields.enable_all_optional_fields()
    #obj_disable_optional_fields = PIMConfigurationPage(dm.driver)
    #obj_disable_optional_fields.disable_optional_fields()

    #custom_field = PIMConfigurationPage(dm.driver)
    #custom_field.add_custom_fields(**{'Field NAME':'Aadhar'})
    #obj_custom_field = PIMConfigurationPage(dm.driver)
    #obj_custom_field.get_custom_filed_records()
    obj_reporting_method = PIMConfigurationPage(dm.driver)
    obj_reporting_method.get_reporting_method_records()
    #reporting_method = PIMConfigurationPage(dm.driver)
    #reporting_method.add_reporting_method()
    #obj_termination_reasons = PIMConfigurationPage(dm.driver)
    #obj_termination_reasons.get_termination_reason_records()
    #termination_reasons = PIMConfigurationPage(dm.driver)
    #termination_reasons.add_termination_reason()



