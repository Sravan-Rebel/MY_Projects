from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductsPage(BasePage):
    PRODUCT_BUTTON=(By.XPATH,"//a[text()=' Products']")
    FIRST_PRODUCT=(By.XPATH,"/html/body/section[2]/div[1]/div/div[2]/div/div[2]")
    SECOND_PRODUCT=(By.XPATH,"/html/body/section[2]/div[1]/div/div[2]/div/div[3]")
    ADD_TO_CART_BUTTON_1=(By.XPATH,"//a[@data-product-id='1']")
    ADD_TO_CART_BUTTON_2=(By.XPATH,"//a[@data-product-id='2']")
    CONTINUE_SHOPPING_BUTTON=(By.XPATH,"//button[text()='Continue Shopping']")
    VIEW_CART_BUTTON=(By.XPATH,"//u[text()='View Cart']")

    def click_products(self):
        self.click_element(self.PRODUCT_BUTTON)
    
    def add_first_product_to_cart(self):
        self.click_element(self.FIRST_PRODUCT)
        self.click_element(self.ADD_TO_CART_BUTTON_1)

    def click_continue_shopping(self):
        self.click_element(self.CONTINUE_SHOPPING_BUTTON)
    
    def add_second_product_to_cart(self):
        self.click_element(self.SECOND_PRODUCT)
        self.click_element(self.ADD_TO_CART_BUTTON_2)

    def click_view_cart(self):
        self.click_element(self.VIEW_CART_BUTTON)
