import os
from selenium import webdriver


class DriverManager:

    def __init__(self, base_url):
        self.driver = None
        self.url = base_url
        self._initialize_driver()

    def _initialize_driver(self):
        driver_location = "..\\..\\dependecies\\webdrivers\\chromedriver.exe"
        if not os.path.exists(driver_location):
            raise Exception("Chrome Driver is not present : {}".format(driver_location))
        self.driver = webdriver.Chrome(executable_path=driver_location)
        self.driver.get(self.url)


