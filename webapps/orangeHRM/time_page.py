from home_page import HomePage


class TimePage:

    def __init__(self, driver):
        home_page = HomePage(driver)
        home_page.navigate_to_time()

    def navigate_to_time_sheets(self, option):
        pass

    def navigate_to_attendance(self, option):
        pass

    def navigate_to_reports(self, option):
        pass

    def navigate_to_project_info(self, option):
        pass

if __name__ == "__main__":
    # Test code or Driver code
    from libUtils.seleniumUtils.driver_manager import DriverManager

    # Driver Initialization
    dm = DriverManager()
    # Navigate to Home --> PIM
    obj = TimePage(dm.driver)
