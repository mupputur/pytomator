__authors__ = ['mupputuri', 'Sreedevi']

from libUtils.seleniumUtils.weblocate_helper import WebLocateHelper
from pim_page import PIMPage
from libUtils.seleniumUtils.driver_manager import DriverManager
from libUtils.seleniumUtils.locators import PIMConfigurationPageLocators as lp
#from selenium.webdriver.common.action_chains import ActionChains
#from selenium.webdriver.common.keys import Keys
import time


class PIMConfigurationPage:

    def __init__(self, driver):
        pim_page = PIMPage(driver)
        #self.Custom_field = lp.CUSTOM_FIELD_XPATH_LOC[0]
        #pim_page.navigate_to_configuration(self.Custom_field,lp.CUSTOM_FIELD_XPATH_LOC[1])
        #self.Reporting_Methods = lp.REPORTING_METHODS_XPATH_LOC[0]
        #pim_page.navigate_to_configuration(self.Reporting_Methods,lp.REPORTING_METHODS_XPATH_LOC[1])
        self.Termination_Reasons = lp.TERMINATION_REASONS_XPATH_LOC[0]
        pim_page.navigate_to_configuration(self.Termination_Reasons,lp.TERMINATION_REASONS_XPATH_LOC[1])
        #self.Optional_Fields = lp.OPTIONAL_FIELDS_BT_XPATH_LOC[0]
        #pim_page.navigate_to_configuration(self.Optional_Fields,lp.OPTIONAL_FIELDS_BT_XPATH_LOC[1])
        self.helper = WebLocateHelper(driver)

    def enable_optional_fields(self, Show_SSN_field_in_Personal_Details , Show_SIN_field_in_Personal_Details):
        ssn_field=self.helper.identify_element(lp.SSN_FIELD_ENABLE_OPTIONAL_FIELDS_XPATH_LOC[0],
                                               lp.SSN_FIELD_ENABLE_OPTIONAL_FIELDS_XPATH_LOC[1],"Show_SSN_field_in_Personal_Details")
        ssn_field.click()
        time.sleep(5)
        sin_field=self.helper.identify_element(lp.SIN_FIELD_ENABLE_OPTIONAL_FIELDS_XPATH_LOC[0],
                                               lp.SIN_FIELD_ENABLE_OPTIONAL_FIELDS_XPATH_LOC[1],"Show_SIN_field_in_Personal_Details")

        sin_field.click()
        time.sleep(5)
        save = self.helper.identify_element(lp.ENABLE_OPTIONAL_FIELD_SAVE_BT_XPATH_LOC[0],
                                            lp.ENABLE_OPTIONAL_FIELD_SAVE_BT_XPATH_LOC[1], "click_save")
        save.click()
        time.sleep(5)
    def disable_optional_fields(self,Show_SSN_field_in_Personal_Details , Show_SIN_field_in_Personal_Details):
        ssn_field = self.helper.identify_element(lp.SSN_FIELD_DISABLE_OPTIONAL_FIELDS_XPATH_LOC[0],
                                                 lp.SSN_FIELD_DISABLE_OPTIONAL_FIELDS_XPATH_LOC[1],
                                                 "Show_SSN_field_in_Personal_Details")
        ssn_field.click()
        time.sleep(5)
        sin_field = self.helper.identify_element(lp.SIN_FIELD_DISABLE_OPTIONAL_FIELDS_XPATH_LOC[0],
                                                 lp.SIN_FIELD_DISABLE_OPTIONAL_FIELDS_XPATH_LOC[1],
                                                 "Show_SIN_field_in_Personal_Details")

        sin_field.click()
        time.sleep(5)
        save = self.helper.identify_element(lp.DISABLE_OPTIONAL_FIELD_SAVE_BT_XPATH_LOC[0],
                                            lp.DISABLE_OPTIONAL_FIELD_SAVE_BT_XPATH_LOC[1], "click_save")
        save.click()
        time.sleep(5)

    def enable_all_optional_fields(self):
        enable_optional_fields = self.helper.identify_element(lp.ENABLE_ALL_OPTIONAL_FIELDS_BT_XPATH_LOC[0],
                                                              lp.ENABLE_ALL_OPTIONAL_FIELDS_BT_XPATH_LOC[1], "PIM")
        enable_optional_fields.click()
        time.sleep(4)
        enable_optional_fields = self.helper.identify_element(lp.ENABLE_ALL_OPTIONAL_FIELDS_1_BT_XPATH_LOC[0],
                                                              lp.ENABLE_ALL_OPTIONAL_FIELDS_1_BT_XPATH_LOC[1], "PIM")
        enable_optional_fields.click()
        time.sleep(4)
        enable_optional_fields = self.helper.identify_element(lp.ENABLE_ALL_OPTIONAL_FIELDS_2_BT_XPATH_LOC[0],
                                                              lp.ENABLE_ALL_OPTIONAL_FIELDS_2_BT_XPATH_LOC[1], "PIM")
        enable_optional_fields.click()
        time.sleep(4)
        enable_optional_fields = self.helper.identify_element(lp.ENABLE_ALL_OPTIONAL_FIELDS_3_BT_XPATH_LOC[0],
                                                              lp.ENABLE_ALL_OPTIONAL_FIELDS_3_BT_XPATH_LOC[1], "PIM")
        enable_optional_fields.click()
        time.sleep(4)
        save = self.helper.identify_element(lp.ENABLE_ALL_OPTIONAL_FIELDS_SAVE_BT_XPATH_LOC[0],
                                            lp.ENABLE_ALL_OPTIONAL_FIELDS_SAVE_BT_XPATH_LOC[1], "click_save")
        save.click()
        time.sleep(5)
    def disable_all_optional_fields(self):
        disable_optional_fields = self.helper.identify_element(lp.DISABLE_ALL_OPTIONAL_FIELDS_BT_XPATH_LOC[0],
                                                               lp.DISABLE_ALL_OPTIONAL_FIELDS_BT_XPATH_LOC[1], "PIM")

        disable_optional_fields.click()
        time.sleep(4)
        disable_optional_fields = self.helper.identify_element(lp.DISABLE_ALL_OPTIONAL_FIELDS_1_BT_XPATH_LOC[0],
                                                               lp.DISABLE_ALL_OPTIONAL_FIELDS_1_BT_XPATH_LOC[1], "PIM")

        disable_optional_fields.click()
        time.sleep(4)
        disable_optional_fields = self.helper.identify_element(lp.DISABLE_ALL_OPTIONAL_FIELDS_2_BT_XPATH_LOC[0],
                                                                lp.DISABLE_ALL_OPTIONAL_FIELDS_2_BT_XPATH_LOC[1], "PIM")


        disable_optional_fields.click()
        time.sleep(4)
        disable_optional_fields = self.helper.identify_element(lp.DISABLE_ALL_OPTIONAL_FIELDS_3_BT_XPATH_LOC[0],
                                                               lp.DISABLE_ALL_OPTIONAL_FIELDS_3_BT_XPATH_LOC[1], "PIM")


        disable_optional_fields.click()
        time.sleep(4)
        save = self.helper.identify_element(lp.DISABLE_ALL_OPTIONAL_FIELDS_SAVE_BT_XPATH_LOC[0],
                                            lp.DISABLE_ALL_OPTIONAL_FIELDS_SAVE_BT_XPATH_LOC[1], "click_save")
        save.click()
        time.sleep(5)
    def add_custom_fields(self, filed_name):
        add = self.helper.identify_element(lp.ADD_BT_XPATH_LOC[0],lp.ADD_BT_XPATH_LOC[1], "click_add")
        add.click()
        time.sleep(5)
        filedname= self.helper.identify_element(lp.FIELD_NAME_TB_XPATH_LOC[0],
                                                lp.FIELD_NAME_TB_XPATH_LOC[1],"filed_name")
        self.helper.enter_text(filedname, filed_name)
        time.sleep(2)
        screen= self.helper.identify_element(lp.SCREEN_BT_XPATH_LOC[0],lp.SCREEN_BT_XPATH_LOC[1],"screen")
        screen.click()
        details = self.helper.identify_element(lp.DETAILS_BT_XPATH_LOC[0],lp.DETAILS_BT_XPATH_LOC[1],"details")
        details.click()
        type= self.helper.identify_element(lp.TYPE_BT_XPATH_LOC[0],lp.TYPE_BT_XPATH_LOC[1],"type")
        type.click()
        time.sleep(2)
        type_detals = self.helper.identify_element(lp.TYPE_DETAILS_BT_XPATH_LOC[0],
                                                   lp.TYPE_DETAILS_BT_XPATH_LOC[1],"type_detals")
        type_detals.click()
        # time.sleep(10)
        save = self.helper.identify_element(lp.CUSTOM_FIELD_SAVE_BT_XPATH_LOC[0],
                                            lp.CUSTOM_FIELD_SAVE_BT_XPATH_LOC[1],"save")
        save.click()
        time.sleep(10)

    def get_custom_filed_records(self):
        custom_field = self.helper.identify_element(lp.CUSTOM_FIELD_RECORDS_XPATH_LOC[0],
                                                    lp.CUSTOM_FIELD_RECORDS_XPATH_LOC[1], "Custom Field")
        custom_field.click()
        time.sleep(5)

    def add_reporting_method(self):
        add = self.helper.identify_element(lp.REPORTING_METHODS_ADD_BT_XPATH_LOC[0],
                                           lp.REPORTING_METHODS_ADD_BT_XPATH_LOC[1], "click_add")
        add.click()
        time.sleep(5)
        name = self.helper.identify_element(lp.NAME_TB_XPATH_LOC[0],lp.NAME_TB_XPATH_LOC[1], "Name")
        self.helper.enter_text(name, "Sree")
        self.helper.click_on(name, '')
        time.sleep(5)
        save = self.helper.identify_element(lp.REPORTING_METHODS_SAVE_BT_XPATH_LOC[0],
                                            lp.REPORTING_METHODS_SAVE_BT_XPATH_LOC[1], "click_save")
        save.click()
        time.sleep(5)
    def get_reporting_method_records(self):
        reporting_method = self.helper.identify_element(lp.REPORTING_METHODS_RECORDS_BT_XPATH_LOC[0],
                                                        lp.REPORTING_METHODS_RECORDS_BT_XPATH_LOC[1], "Reporting Method")
        reporting_method.click()
        time.sleep(5)
    def add_termination_reason(self):
        add = self.helper.identify_element(lp.TERMINATION_REASONS_ADD_BT_XPATH_LOC[0],
                                           lp.TERMINATION_REASONS_ADD_BT_XPATH_LOC[1], "click_add")
        add.click()
        time.sleep(5)
        name = self.helper.identify_element(lp.TERMINATION_REASONS_NAME_TB_XPATH_LOC[0],
                                            lp.TERMINATION_REASONS_NAME_TB_XPATH_LOC[1], "Name")
        self.helper.enter_text(name, "Sree")
        self.helper.click_on(name, '')
        time.sleep(5)
        save = self.helper.identify_element(lp.TERMINATION_REASONS_SAVE_BT_XPATH_LOC[0],
                                            lp.TERMINATION_REASONS_SAVE_BT_XPATH_LOC[1], "click_save")
        save.click()
        time.sleep(5)

    def get_termination_reason_records(self):
        termination_reason = self.helper.identify_element(lp.TERMINATION_REASONS_RECORDS_BT_XPATH_LOC[0],
                                                lp.TERMINATION_REASONS_RECORDS_BT_XPATH_LOC[1], "Termination Reasons")
        termination_reason.click()
        time.sleep(5)

    def import_data(self):
        pass

if __name__ == "__main__":

    dm = DriverManager()
    #obj = PIMPage(dm.driver)
    #obj_optional_fields = PIMConfigurationPage(dm.driver)
    #obj_optional_fields.disable_optional_fields("Show SSN field in Personal Details", "Show SIN field in Personal Details")
    #obj_optional_fields.disable_optional_fields(**{"v2": "Show SIN field in Personal Details"})
    #time.sleep(5)
    #obj_optional_fields = PIMConfigurationPage(dm.driver)
    #obj_optional_fields.enable_optional_fields("Show SSN field in Personal Details", "Show SIN field in Personal Details")
    #obj_optional_fields.enable_optional_fields(**{"v2": "Show SIN field in Personal Details"})
    #time.sleep(5)
    #obj_enable_optional_fields = PIMConfigurationPage(dm.driver)
    #obj_enable_optional_fields.enable_all_optional_fields()
    #time.sleep(2)
    #obj_disable_optional_fields = PIMConfigurationPage(dm.driver)
    #obj_disable_optional_fields.disable_all_optional_fields()
    #time.sleep(2)
    #custom_field = PIMConfigurationPage(dm.driver)
    #custom_field.add_custom_fields(**{'Field NAME':'Aadhar'})
    #obj_custom_field = PIMConfigurationPage(dm.driver)
    #obj_custom_field.get_custom_filed_records()
    #obj_reporting_method = PIMConfigurationPage(dm.driver)
    #obj_reporting_method.get_reporting_method_records()
    #reporting_method = PIMConfigurationPage(dm.driver)
    #reporting_method.add_reporting_method()
    #obj_termination_reasons = PIMConfigurationPage(dm.driver)
    #obj_termination_reasons.get_termination_reason_records()
    termination_reasons = PIMConfigurationPage(dm.driver)
    termination_reasons.add_termination_reason()



