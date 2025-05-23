from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductsQuantityPage(BasePage):
    PRODUCTS_BUTTON = (By.XPATH, "//a[text()=' Products']")
    VIEW_FIRST_PRODUCT = (By.XPATH,"//a[text()='View Product']")
    QUANTITY_INPUT =(By.ID, "quantity")
    ADD_TO_CART_BUTTON =(By.XPATH, "//button[@class='btn btn-default cart']")
    VIEW_CART_BUTTON = (By.XPATH, "//u[text()='View Cart']")

    def click_view_product(self):
        self.click_element(self.VIEW_FIRST_PRODUCT)
    
    def set_product_quantity(self, quantity):
        self.set_input_value(self.QUANTITY_INPUT, quantity)
    
    def click_add_to_cart(self):
        self.click_element(self.ADD_TO_CART_BUTTON)
    
    def click_view_cart(self):
        self.click_element(self.VIEW_CART_BUTTON)