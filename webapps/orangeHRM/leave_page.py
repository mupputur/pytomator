from home_page import HomePage


class LeavePage:

    def __init__(self, driver):
        home_page = HomePage(driver)
        home_page.navigate_to_leave()

    def navigate_to_apply(self):
        pass

    def navigate_to_my_leave(self):
        pass

    def navigate_entitlements(self, option):
        pass

    def navigate_reports(self, option):
        pass

    def navigate_configure(self, option):
        pass

    def navigate_leave_list(self):
        pass

    def navigate_assign_leave(self):
        pass


if __name__ == "__main__":
    # Test code or Driver code
    from libUtils.seleniumUtils.driver_manager import DriverManager
    # Driver Initialization
    dm = DriverManager()
    # Navigate to Home --> PIM
    obj = LeavePage(dm.driver)
