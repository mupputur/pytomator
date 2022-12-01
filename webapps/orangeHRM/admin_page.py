import time

from home_page import HomePage
from libUtils.seleniumUtils.weblocate_helper import WebLocateHelper



class AdminPage:

    def __init__(self, driver):
        home_page = HomePage(driver)
        home_page.navigate_to_admin()
        self.helper = WebLocateHelper(driver)

    def navigate_to_user_management(self, option):
        print("Navigating to user management page ...")
        user_management = self.helper.identify_element("//span[@class='oxd-topbar-body-nav-tab-item']", "XPATH", "Admin")
        user_management.click()
        time.sleep(3)
        sub_module = self.helper.identify_element(option, "XPATH", "user_management")
        sub_module.click()
        time.sleep(3)
        print("Successfully navigated user management page.")

    def navigate_to_job(self, option):
        print("Navigating to job page ...")
        job = self.helper.identify_element("(//span[@class='oxd-topbar-body-nav-tab-item'])[2]", "XPATH", "Admin")
        job.click()
        time.sleep(3)
        sub_module = self.helper.identify_element(option, "XPATH", "job")
        sub_module.click()
        time.sleep(3)
        print("Successfully navigated job page.")

    def navigate_to_organization(self, option):
        print("Navigating to organization page ...")
        organization = self.helper.identify_element("(//i[@class='oxd-icon bi-chevron-down'])[3]", "XPATH", "Admin")
        organization.click()
        time.sleep(3)
        sub_module = self.helper.identify_element(option, "XPATH", "organization")
        sub_module.click()
        time.sleep(3)
        print("Successfully navigated organization page.")



    def navigate_to_qualifications(self, option):
        print("Navigating to qualifications page ...")
        qualifications = self.helper.identify_element('//*[text()="Qualifications "]', "XPATH", "Admin")
        qualifications.click()
        time.sleep(3)
        sub_module = self.helper.identify_element(option, "XPATH", "qualifications")
        sub_module.click()
        time.sleep(3)
        print("Successfully navigated qualifications page.")

    def navigate_to_nationalities(self):
        print("Navigating to nationalities page ...")
        nationalities = self.helper.identify_element('//*[text()="Nationalities"]', "XPATH", "Nationalities")
        nationalities.click()
        time.sleep(3)
        print("Successfully navigated nationalities page.")



    def navigate_to_corporate_branding(self):
        print("Navigating to corporate_branding page ...")
        corporate_branding = self.helper.identify_element('//*[text()="Corporate Branding"]', "XPATH", "Corporate Branding")
        corporate_branding.click()
        time.sleep(3)
        print("Successfully navigated corporate_branding page.")

    def navigate_to_configuration(self, option):
        print("Navigating to configuration page ...")
        configuration = self.helper.identify_element('//*[text()="Configuration "]', "XPATH", "Configuration")
        configuration.click()
        time.sleep(3)
        sub_module = self.helper.identify_element(option, "XPATH", "Configuration")
        sub_module.click()
        time.sleep(3)
        print("Successfully navigated configuration page.")


if __name__ == "__main__":
    # Test code or Driver code
    from libUtils.seleniumUtils.driver_manager import DriverManager

    # Driver Initialization
    dm = DriverManager()
    # Navigate to Home --> PIM
    obj = AdminPage(dm.driver)
    #USER_MANAGEMENT
    users = "//a[@class='oxd-topbar-body-nav-tab-link']"
    obj.navigate_to_user_management(users)
    #JOB:--------
    #job_titles = "(//span[@class='oxd-topbar-body-nav-tab-item'])[2]"
    #obj.navigate_to_job(job_titles)
    #pay_grades = "(//a[@href='#'])[2]"
    #obj.navigate_to_job(pay_grades)
    #employment_status = "(//a[@href='#'])[3]"
    #obj.navigate_to_job(employment_status)
    #job_categories = "(//a[@href='#'])[4]"
    #obj.navigate_to_job(job_categories)
    #work_shifts = "(//a[@href='#'])[5]"
    #obj.navigate_to_job(work_shifts)
    #   ORGANIZATIONS
    #general_information = "//*[text()='General Information']"
    #obj.navigate_to_organization(general_information)
    #locations = "(//a[@href='#'])[2]"
    #obj.navigate_to_organization(locations)
    #structure = "(//a[@href='#'])[3]"
    #obj.navigate_to_organization(structure)
    #skills = "(//a[@href='#'])[2]"
        # QUALIFICATIONS
    #obj.navigate_to_qualifications(skills)
    #education = "(//a[@href='#'])[2]"
    #obj.navigate_to_qualifications(education)
    #licenses = "(//a[@href='#'])[3]"
    #obj.navigate_to_qualifications(licenses)
    #languages = "(//a[@href='#'])[4]"
    #obj.navigate_to_qualifications(languages)
    #memberships = "(//a[@href='#'])[5]"
    #obj.navigate_to_qualifications(memberships)
             #nationalities
    #obj.navigate_to_nationalities()
    #obj.navigate_to_corporate_branding()
    # configuration
    #email_configuration = '//*[text()="Email Configuration"]'
    #obj.navigate_to_configuration(email_configuration)
    #email_subscriptions = '//*[text()="Email Subscriptions"]'
    #obj.navigate_to_configuration(email_subscriptions)
    #localization = '//*[text()="Localization"]'
    #obj.navigate_to_configuration(localization)
    #language_packages = '//*[text()="Language Packages"]'
    #obj.navigate_to_configuration(language_packages)
    #modules = '//*[text()="Modules"]'
    #obj.navigate_to_configuration(modules)
    #social_media_authentication = '//*[text()="Social Media Authentication"]'
    #obj.navigate_to_configuration(social_media_authentication)
    #register_oauth_client = '//*[text()="Register OAuth Client"]'
    #obj.navigate_to_configuration(register_oauth_client)
    #ldap_configuration = '//*[text()="LDAP Configuration"]'
    #obj.navigate_to_configuration(ldap_configuration)





