from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class TestCasesPage(BasePage):
    TEST_CASES_BUTTON=(By.LINK_TEXT,"Test Cases")
    TEST_CASES_PAGE_HEADER=(By.XPATH,"//b[text()='Test Cases']")

    def open_test_cases_page(self):
        self.click_element(self.TEST_CASES_BUTTON)
    
    def verify_test_cases_page(self):
        return self.is_visible(self.TEST_CASES_PAGE_HEADER)