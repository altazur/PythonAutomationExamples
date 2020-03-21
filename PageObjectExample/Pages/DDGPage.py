from BasePage import BasePage
from selenium.webdriver.common.by import By

class DDGSearchLocators:
    LOCATOR_DDG_SEARCH_FIELD = (By.ID, "search_form_input_homepage")
    LOCATOR_DDG_SEARCH_BUTTON = (By.ID, "search_button_homepage")
    LOCATOR_DDG_FIRST_RESULT = (By.ID, "r1-0")

class SearchHelper(BasePage):

    def enter_search(self, text):
        search_field = self.find_element(DDGSearchLocators.LOCATOR_DDG_SEARCH_FIELD)
        search_field.send_keys(text)
        search_field.click()
        return search_field

    def click_search_button(self):
        return self.find_element(DDGSearchLocators.LOCATOR_DDG_SEARCH_BUTTON, time=2).click()

    def get_first_result_text(self):
        return self.find_element(DDGSearchLocators.LOCATOR_DDG_FIRST_RESULT, time=5).text
