import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

"""from webdriver.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver.microsoft import EdgeChromiumDriverManager"""


class DriverManager:

    def __init__(self):
        self.driver = None

    def initialize_driver(self, browser, url):
        print(browser)
        print(url)

        if browser == 'chrome':
            op = webdriver.ChromeOptions()
            self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        elif browser == 'firefox':
            op = Options()
            self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        elif browser == 'edge':
            self.driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install())

        self.driver.get(url)
        self.driver.implicitly_wait(15)
        self.driver.delete_all_cookies()
        self.driver.maximize_window()

    """def initialize_driver(self,browser,url):
        try:
            path ="C:\\Users\\training\\PycharmProjects\\pythonProject1\\Upputuri\\lawsonium\\drivers\\chrome\\chromedriver1.exe"
            self.driver_path = Service(executable_path=path)
            self.driver = webdriver.Chrome(service=self.driver_path)

            if url == "LAWSON-US":
                self.driver.get("https://oro-staging.lawsonproducts.com/")
            elif url == "LAWSON-CA":
                self.driver.get("htps://oro-staging.lawsonproducts.ca/")
            elif url == "KENT-US":
                self.driver.get("https://oro-staging.kent-automotive.com/")
            elif url == "KENT-CA":
                self.driver.get("https://oro-staging.kent-automotive.ca/")
            self.driver.maximize_window()


        except Exception as e:
            raise Exception("Unable to launch the app {} ".format(str(e)))
            return self.driver
"""

    def close_session(self):
        self.driver.close()



