from selenium.webdriver.common.by import By
from pages.base_page import BasePage



class VerifyCartPage(BasePage):
    PRODUCT_QUANTITY=(By.XPATH,"//td[contains(@class,'cart_quantity')]")

    def get_cart_product_quantity(self):
        return self.driver.find_element(*self.PRODUCT_QUANTITY).get_attribute("value")