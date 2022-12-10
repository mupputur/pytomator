__authors__ = ['mupputuri', 'Srivani']
import time
from libUtils.seleniumUtils.weblocate_helper import WebLocateHelper
from pim_page import PIMPage
from libUtils.seleniumUtils.driver_manager import DriverManager
from selenium.webdriver.common.action_chains import ActionChains

class ReportPage:

    def __init__(self,driver):
        pim_page = PIMPage(driver)
        pim_page.navigate_to_reports()
        self.helper = WebLocateHelper(driver)


    def search(self, report_name):
        reportsname=self.helper.identify_element('//*[@placeholder="Type for hints..."]',"XPATH","reportsname")
        reportsname.send_keys(report_name)
        time.sleep(3)
        sub= self.helper.identify_element("//*[text()=' Search ']", "XPATH", "click_search")
        sub.click()
        time.sleep(5)



    def reset(self):
        resetsname=self.helper.identify_element('//*[@placeholder="Type for hints..."]',"XPATH","reportsname")
        self.helper.enter_text(resetsname,"PIM Sample Report")
        self.helper.click_on(resetsname,'')
        time.sleep(5)
        reset=self.helper.identify_element('//*[text()=" Reset "]',"XPATH","click_reset")
        reset.click()
        time.sleep(5)
        reset.click()
        time.sleep(5)


    def get_records(self):
        """
        get_list=self.helper.identify_element("/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[2]/div","XPATH",'recods')
        list_vales=[]
        for i in range(len(get_list)):
            text=get_list[i].text
            list_vales.append(text)
        print(list_vales)
        """
        report = self.helper.identify_element("(//a[@class='oxd-topbar-body-nav-tab-item'])[3]", "XPATH", "report")
        report.click()
        time.sleep(3)


if __name__ == "__main__":
    dm = DriverManager()
    obj_reports = ReportPage(dm.driver)
    obj_reports.search("Employee Job Details")
    #obj_reports.reset()
    #obj_reports.get_records()
