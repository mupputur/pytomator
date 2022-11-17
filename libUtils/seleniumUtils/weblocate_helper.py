from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
import os


class WebLocateHelper:

    def __init__(self, driver):
        self.driver = driver

    def identify_element(self, locator, locator_type, element_text):
        element = None
        # wait = WebDriverWait(self.driver, 10)
        # return wait.until(ec._element_if_visible())
        try:
            """if locator_type == "XPATH":
                element_loc = wait.until(ec._element_if_visible(By.XPATH, locator))
            elif locator_type == "NAME":
                element_loc = wait.until(ec._element_if_visible(By.NAME, locator))
            elif locator_type == "ID":
                element_loc = wait.until(ec._element_if_visible(By.ID, locator))"""

            if locator_type == "XPATH":
                element = self.driver.find_element(By.XPATH, locator)
            elif locator_type == "NAME":
                element = self.driver.find_element(By.NAME, locator)
            elif locator_type == "ID":
                element = self.driver.find_element(By.ID, locator)

        except Exception as e:
            raise Exception("Unable to locate the element {} and Error: ".format(element_text, str(e)))
        # return element_loc
        return element
        # return wait.until(ec._element_if_visible(element_loc))

    def click_on(self, element, element_text):
        try:
            element.click()
        except Exception as e:
            raise Exception("Unable to click on {}, error: {}".format(element_text, str(e)))

    def enter_text(self, element, element_text, name, max_quantity=None):
        for i in range(10):
            element.send_keys(Keys.BACK_SPACE)

        try:
            if max_quantity is not None:
                element.send_keys(name)
            else:
                element.send_keys(element_text)
                # print("***********************************************************")

        except Exception as e:
            raise Exception("Unable to enter the text on {}, error: {}".format(element_text, str(e)))

    def run_script(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def capture_screen_shot(self, name):
        path = "C:\\Users\\training\\PycharmProjects\\pythonProject1\\Upputuri\\lawsonium\\ScreenCaptures"
        file_name = name + ".png"
        path = os.path.join(path, file_name)
        self.driver.save_screenshot(path)
