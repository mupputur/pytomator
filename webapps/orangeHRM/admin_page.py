from home_page import HomePage


class AdminPage:

    def __init__(self, driver):
        home_page = HomePage(driver)
        home_page.navigate_to_admin()

    def navigate_to_user_management(self, option):
        print("Navigating to user management page ...")
        # Write your logic here
        print(f"Successfully user management page.")

    def navigate_to_job(self, option):
        pass

    def navigate_to_organization(self):
        pass

    def navigate_to_qualifications(self):
        pass

    def navigate_to_nationalities(self):
        pass

    def navigate_to_corporate_branding(self):
        pass

    def navigate_to_configuration(self, option):
        pass

if __name__ == "__main__":
    # Test code or Driver code
    from libUtils.seleniumUtils.driver_manager import DriverManager

    # Driver Initialization
    dm = DriverManager()
    # Navigate to Home --> PIM
    obj = AdminPage(dm.driver)
