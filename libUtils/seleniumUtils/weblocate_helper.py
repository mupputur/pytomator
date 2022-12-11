from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
import os
from selenium.webdriver.support import expected_conditions as EC



class WebLocateHelper:

    def __init__(self, driver):
        self.driver = driver

    def identify_element(self, locator, locator_type, element_text):
        element = None
        try:
            if locator_type == "XPATH":
                element = self.driver.find_element(By.XPATH, locator)
            elif locator_type == "NAME":
                element = self.driver.find_element(By.NAME, locator)
                print(element)
            elif locator_type == "ID":
                element = self.driver.find_element(By.ID, locator)
        except Exception as e:
            raise Exception("Unable to locate the element {} and Error: ".format(element_text, str(e)))
            pass


        # return element_loc
        return element
        # return wait.until(ec._element_if_visible(element_loc))

    def click_on(self, element, element_text):
        try:
            element.click()
        except Exception as e:
            raise Exception("Unable to click on {}, error: {}".format(element_text, str(e)))

    def enter_text(self, element, element_text):
        #try:
            element.send_keys(element_text)
        #except Exception as e:
            #print("Unable to send the text ")
    def identify_elements(self, locator, locator_type, element_text):
        elements = None
        try:
            if locator_type == "XPATH":
                elements = self.driver.find_elements(By.XPATH, locator)
        except:
            print("unble to locate full xpath")
        return elements
    def wait(self,locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located((By.XPATH,locator)))
        return element

    def run_script(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def capture_screen_shot(self, name):
        path = "C:\\Users\\training\\PycharmProjects\\pythonProject1\\Upputuri\\lawsonium\\ScreenCaptures"
        file_name = name + ".png"
        path = os.path.join(path, file_name)
        self.driver.save_screenshot(path)
