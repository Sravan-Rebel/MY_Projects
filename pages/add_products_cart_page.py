from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    PRODUCTS=(By.XPATH,"//td[contains(@class,'cart_product')]")
    PRODUCT_PRICE=(By.XPATH,"//td[contains(@class,'cart_price')]")
    PRODUCT_QUANTITY=(By.XPATH,"//td[contains(@class,'cart_quantity')]")
    TOTAL_PRICE=(By.XPATH,"//td[contains(@class,'cart_total')]")

    def get_product_count(self):
        return len(self.driver.find_elements(*self.PRODUCTS))
    
    def get_product_price(self):
        return [price.text for price in self.driver.find_elements(*self.PRODUCT_PRICE)]
    
    def get_product_quantity(self):
        return [quantity.text for quantity in self.driver.find_elements(*self.PRODUCT_QUANTITY)]
    
    def get_total_price(self):
        return [total_price.text for total_price in self.driver.find_elements(*self.TOTAL_PRICE)]


