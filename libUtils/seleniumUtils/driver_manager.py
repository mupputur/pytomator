from selenium import webdriver


class DriverManager:

    def __init__(self):
        self.driver = None
        self.url = "https://opensource-demo.orangehrmlive.com/"
        self.initialize_driver()

    def initialize_driver(self):
        try:
            self.driver = webdriver.Chrome(executable_path="C:\\Users\\91998\\Documents\\GitRepos\\pytomator\\dependencies\\webdrivers\\chromedriver.exe")
            self.driver.get(self.url)
            self.driver.implicitly_wait(15)
            self.driver.delete_all_cookies()
            self.driver.maximize_window()
        except Exception as e:
            raise Exception("Fail to initialize the driver")
            print(str(e))

    def close_session(self):
        self.driver.close()
