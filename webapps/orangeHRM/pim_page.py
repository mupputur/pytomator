from home_page import HomePage


class PIMPage:

    def __init__(self, driver):
        home_page = HomePage(driver)
        home_page.navigate_to_pim()

    def navigate_to_configuration(self, option):
        print("Navigating to configuration page ...")
        # Write your logic here
        print(f"Successfully configuration page.")

    def navigate_to_employee_list(self):
        print("Navigating to employee list page ...")
        # Write your logic here
        print(f"Successfully navigated employee list page.")

    def navigate_to_add_employee(self):
        print("Navigating to add employee page ...")
        # Write your logic here
        print(f"Successfully navigated to add employee.")

    def navigate_to_reports(self):
        print("Navigating to report page ...")
        # Write your logic here
        print(f"Successfully navigated to reports page.")


if __name__ == "__main__":
    # Test code or Driver code
    from libUtils.seleniumUtils.driver_manager import DriverManager
    # Driver Initialization
    dm = DriverManager()
    # Navigate to Home --> PIM
    obj = PIMPage(dm.driver)
