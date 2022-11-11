class SeleniumBase:

    def __init__(self, driver):
        self.driver =driver

    def identify_element(self, locator_value, locator_type, element_name):
        try:
            if locator_type == "ID":
                element = self.driver.find_element_by_id(locator_value)
            elif locator_type == "XPATH":
                self.driver.find_element_by_xpath(locator_value)
            return element
        except Exception as e:
            print("Unable to find the elemnet :{} ERROR: {}".format(element_name, str(e)))

    def click(self, element):
        try:
            element.click()
        except Exception as e:
            print(f"Unable to click the element: {str(e)}")

    def send_text(self, elem, text):
        try:
            elem.send_keys(text)
        except Exception as e:
            print(f"Unable to send the text: {str(e)}")
