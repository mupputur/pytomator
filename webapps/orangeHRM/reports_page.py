__authors__ = ['mupputuri', 'Srivani']
import time
from libUtils.seleniumUtils.weblocate_helper import WebLocateHelper
from pim_page import PIMPage
from libUtils.seleniumUtils.driver_manager import DriverManager
from selenium.webdriver.common.action_chains import ActionChains
from libUtils.seleniumUtils.locators import ReportPageLocators as lp
class ReportPage:

    def __init__(self,driver):
        pim_page = PIMPage(driver)
        pim_page.navigate_to_reports()
        self.helper = WebLocateHelper(driver)


    def search(self, report_name):
        reportsname=self.helper.identify_element(lp.REPORTS_NAME_TB_XPATH_LOC[0],lp.REPORTS_NAME_TB_XPATH_LOC[1],"reportsname")
        reportsname.send_keys(report_name)
        time.sleep(3)
        sub= self.helper.identify_element(lp.SUB_BT_XPATH_LOC[0],lp.SUB_BT_XPATH_LOC[1], "click_search")
        sub.click()
        time.sleep(5)



    def reset(self):
        resetsname=self.helper.identify_element(lp.RESETS_NAME_TB_XPATH_LOC[0],lp.RESETS_NAME_TB_XPATH_LOC[1],"reportsname")
        self.helper.enter_text(resetsname,"PIM Sample Report")
        self.helper.click_on(resetsname,'')
        time.sleep(5)
        reset=self.helper.identify_element(lp.RESET_BT_XPATH_LOC[0],lp.RESET_BT_XPATH_LOC[1],"click_reset")
        reset.click()
        time.sleep(5)
        reset.click()
        time.sleep(5)


    def get_records(self):
        """
        get_list=self.helper.identify_element(lp.GET_LIST_XPATH_LOC[0],lp.GET_LIST_XPATH_LOC[1],"recods")
        list_vales=[]
        for i in range(len(get_list)):
            text=get_list[i].text
            list_vales.append(text)
        print(list_vales)
        """
        report = self.helper.identify_element(lp.REPORT_BT_XPATH_LOC[0],lp.REPORT_BT_XPATH_LOC[1], "report")
        report.click()
        time.sleep(3)


if __name__ == "__main__":
    dm = DriverManager()
    obj_reports = ReportPage(dm.driver)
    #obj_reports.search("Employee Job Details")
    #obj_reports.reset()
    obj_reports.get_records()
