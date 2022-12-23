import time

from home_page import HomePage
from libUtils.seleniumUtils.weblocate_helper import WebLocateHelper
from libUtils.seleniumUtils.locators import AdminPageLocators as lp


class AdminPage:

    def __init__(self, driver):
        home_page = HomePage(driver)
        home_page.navigate_to_admin()
        self.helper = WebLocateHelper(driver)

    def navigate_to_user_management(self, option,identifier):
        print("Navigating to user management page ...")
        user_management = self.helper.identify_element(lp.USER_MANAGEMENT_BT_XPATH_LOC[0],lp.USER_MANAGEMENT_BT_XPATH_LOC[1], "Admin")
        user_management.click()
        time.sleep(3)
        sub_module = self.helper.identify_element(option,identifier, "user_management")
        sub_module.click()
        time.sleep(3)
        print("Successfully navigated user management page.")

    def navigate_to_job(self, option,identifier):
        print("Navigating to job page ...")
        job = self.helper.identify_element(lp.JOB_BT_XPATH_LOC[0],lp.JOB_BT_XPATH_LOC[1], "Admin")
        job.click()
        time.sleep(3)
        sub_module = self.helper.identify_element(option,identifier, "job")
        sub_module.click()
        time.sleep(3)
        print("Successfully navigated job page.")

    def navigate_to_organization(self, option,identifier):
        print("Navigating to organization page ...")
        organization = self.helper.identify_element(lp.ORGANIZATION_BT_XPATH_LOC[0],lp.ORGANIZATION_BT_XPATH_LOC[1], "Admin")
        organization.click()
        time.sleep(3)
        sub_module = self.helper.identify_element(option,identifier, "organization")
        sub_module.click()
        time.sleep(3)
        print("Successfully navigated organization page.")



    def navigate_to_qualifications(self, option,identifier):
        print("Navigating to qualifications page ...")
        qualifications = self.helper.identify_element(lp.QUALIFICATIONS_BT_XPATH_LOC[0],lp.QUALIFICATIONS_BT_XPATH_LOC[1], "Admin")
        qualifications.click()
        time.sleep(3)
        sub_module = self.helper.identify_element(option,identifier, "qualifications")
        sub_module.click()
        time.sleep(3)
        print("Successfully navigated qualifications page.")

    def navigate_to_nationalities(self):
        print("Navigating to nationalities page ...")
        nationalities = self.helper.identify_element(lp.NATIONALITIES_BT_XPATH_LOC[0],lp.NATIONALITIES_BT_XPATH_LOC[1], "Nationalities")
        nationalities.click()
        time.sleep(3)
        print("Successfully navigated nationalities page.")



    def navigate_to_corporate_branding(self):
        print("Navigating to corporate_branding page ...")
        corporate_branding = self.helper.identify_element(lp.CORPORATE_BRANDING_BT_XPATH_LOC[0],lp.CORPORATE_BRANDING_BT_XPATH_LOC[1], "Corporate Branding")
        corporate_branding.click()
        time.sleep(3)
        print("Successfully navigated corporate_branding page.")

    def navigate_to_configuration(self, option,identifier):
        print("Navigating to configuration page ...")
        configuration = self.helper.identify_element(lp.CONFIGURATION_BT_XPATH_LOC[0],lp.CONFIGURATION_BT_XPATH_LOC[1], "Configuration")
        configuration.click()
        time.sleep(3)
        sub_module = self.helper.identify_element(option,identifier, "Configuration")
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
    #users = lp.USERS_BT_XPATH_LOC[0]
    #obj.navigate_to_user_management(users,lp.USERS_BT_XPATH_LOC[1])
    #JOB:--------
    #job_titles =lp.JOB_TITLES_BT_XPATH_LOC[0]
    #obj.navigate_to_job(job_titles,lp.JOB_TITLES_BT_XPATH_LOC[1])
    #pay_grades = lp.PAY_GRADES_BT_XPATH_LOC[0]
    #obj.navigate_to_job(pay_grades,lp.PAY_GRADES_BT_XPATH_LOC[1])
    #employment_status = lp.EMP_STATUS_BT_XPATH_LOC[0]
    #obj.navigate_to_job(employment_status,lp.EMP_STATUS_BT_XPATH_LOC[1])
    #job_categories =lp.JOB_CATEGORIES_BT_XPATH_LOC[0]
    #obj.navigate_to_job(job_categories,lp.JOB_CATEGORIES_BT_XPATH_LOC[1])
    #work_shifts =lp.WORK_SHIFTS_BT_XPATH_LOC[0]
    #obj.navigate_to_job(work_shifts,lp.WORK_SHIFTS_BT_XPATH_LOC[1])
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





