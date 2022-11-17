# from source.locators import CartItemLocators as cil
from libutils.weblocate_helper import WebLocateHelper


class AlertHandler:
    def __init__(self, driver):
        self.helper = WebLocateHelper(driver)

    def select_account(self, account_default=True, cil=None):
        ele_continue = self.helper.identify_element(cil.CONTINUE_BOX_XPATH, "XPATH", "continue")
        self.helper.click_on(ele_continue, "CONTINUE_BOX_XPATH")
