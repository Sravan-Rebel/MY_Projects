from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def is_visible(self, by_locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
            return True
        except Exception:
            return False
        
    def click_element(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator)).click()

    def enter_text(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)
    
    def verify_element(self, by_locator, expected_text=None):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        assert element.is_displayed(), f"Element {by_locator} is not visible"
        if expected_text:
            actual_text = element.text.strip()
            assert actual_text == expected_text, f"Expected text '{expected_text}', but got '{actual_text}'"
        return True
    
    def enter_text(self, by_locator, text):
        element=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        element.clear()
        element.send_keys(text)

    def set_input_value(self, locator, value):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator),
            message=f"Element with locator {locator} not found"
        )
        element.clear()
        element.send_keys(str(value))