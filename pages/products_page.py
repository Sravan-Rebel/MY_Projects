from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductsPage(BasePage):
    PRODUCT_BUTTON=(By.XPATH,"//a[text()=' Products']")
    ALL_PRODUCTS_HEADER=(By.XPATH,"//h2[text()='All Products']")
    PRODUCT_LIST=(By.CLASS_NAME,"features_items")
    VIEW_PRODUCT_BUTTON=(By.XPATH,"//a[text()='View Product']")
    PRODUCT_NAME=(By.XPATH,"//h2[text()='Blue Top']")
    PRODUCT_CATEGORY=(By.XPATH,"//p[contains(text(), 'Category')]")
    PRODUCT_PRICE=(By.XPATH,"//span[text()= 'Rs. 500']")
    PRODUCT_AVAILABILITY=(By.XPATH,"//b[text()= 'Availability:']")
    PRODUCT_CONDITION=(By.XPATH,"//b[text()= 'Condition:']")
    PRODUCT_BRAND=(By.XPATH,"//b[text()= 'Brand:']")

    def open_all_products_page(self):
        self.click_element(self.PRODUCT_BUTTON)
    def verify_products_list(self):
        self.verify_element(self.PRODUCT_LIST)
    
    def open_first_product_details(self):
        self.click_element(self.VIEW_PRODUCT_BUTTON)

    def verify_product_details(self):
        self.verify_element(self.PRODUCT_NAME)
        self.verify_element(self.PRODUCT_CATEGORY)
        self.verify_element(self.PRODUCT_PRICE)
        self.verify_element(self.PRODUCT_AVAILABILITY)
        self.verify_element(self.PRODUCT_CONDITION)
        self.verify_element(self.PRODUCT_BRAND)