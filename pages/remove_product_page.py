from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class HomePage(BasePage):
    PRODUCTS_BUTTON = (By.XPATH, "//a[text()=' Products']")
    FIRST_PRODUCT = (By.XPATH, "/html/body/section[2]/div[1]/div/div[2]/div/div[2]")
    ADD_TO_CART_BUTTON1 = (By.XPATH, "//a[text()='Add to cart']")
    CONTINUE_SHOPPING_BUTTON = (By.XPATH, "//button[text()='Continue Shopping']")
    CART_BUTTON = (By.XPATH, "//a[text()=' Cart']")

    def click_products(self):
        self.click_element(self.PRODUCTS_BUTTON)

    def add_first_product_to_cart(self):
        try:
            first_product_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.FIRST_PRODUCT)
            )

            self.driver.execute_script("arguments[0].scrollIntoView();", first_product_element)

            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.FIRST_PRODUCT)
            )
        except TimeoutException:
            print("First product element was not found or could not be clicked")
            raise
        self.click_element(self.ADD_TO_CART_BUTTON1)

    def click_continue_shopping(self):
        self.click_element(self.CONTINUE_SHOPPING_BUTTON)

    def click_on_cart(self):
        self.click_element(self.CART_BUTTON)


class RemoveProduct(BasePage):
    REMOVE_PRODUCT_BUTTON=(By.XPATH,"//a[@class='cart_quantity_delete']")
    REMOVED_MESSAGE=(By.XPATH,"//p[@class='text-center']")

    def click_on_remove_button(self):
        self.click_element(self.REMOVE_PRODUCT_BUTTON)
    
    def verify_removed_message(self):
        self.is_visible(self.REMOVED_MESSAGE)
