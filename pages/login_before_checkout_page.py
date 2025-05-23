from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class LoginPage(BasePage):
    SIGNUP_LOGIN_BUTTON = (By.XPATH, "//a[contains(text(), ' Signup / Login')]")
    LOGIN_TEXT = (By.XPATH, "//h2[text()='Login to your account']")
    EMAIL_INPUT = (By.XPATH, "//input[@data-qa='login-email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@data-qa='login-password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@data-qa='login-button']")
    LOGGED_IN_TEXT = (By.XPATH, "//a[contains(text(),'Logged in as')]")

    def login_user(self, email, password):
        self.click_element(self.SIGNUP_LOGIN_BUTTON)
        self.enter_text(self.EMAIL_INPUT, email)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click_element(self.LOGIN_BUTTON)
        self.is_visible(self.LOGGED_IN_TEXT)

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

class CartPage(BasePage):
    PROCEED_TO_CHECKOUT = (By.XPATH, "//a[text()='Proceed To Checkout']")

    def click_on_proceed_to_checkout(self):
        self.click_element(self.PROCEED_TO_CHECKOUT)

class CartDetails(BasePage):
    TEXT_MESSAGE = (By.NAME, "message")
    PLACE_ORDER = (By.XPATH, "//a[text()='Place Order']")
    CARD_NAME_INUPT = (By.NAME, "name_on_card")
    CARD_NUMBER = (By.NAME, "card_number")
    CVC = (By.NAME, "cvc")
    EXPIRY_MONTH =(By.NAME, "expiry_month")
    EXPIRY_YEAR =(By.NAME, "expiry_year")
    PAY_AND_CONFIRM_ORDER_BUTTON = (By.XPATH, "//button[@id='submit']")
    SUCCESS_MESSAGE = (By.XPATH, "//p[text()='Congratulations! Your order has been confirmed!']")

    def again_click_on_proceed_to_checkout(self, text_message):
        self.enter_text(self.TEXT_MESSAGE, text_message["message"])
        self.click_element(self.PLACE_ORDER)

    def enter_payment_details(self, card_details):
        self.enter_text(self.CARD_NAME_INUPT, card_details["card_name"])
        self.enter_text(self.CARD_NUMBER, card_details["card_number"])
        self.enter_text(self.CVC, card_details["cvc"])
        self.enter_text(self.EXPIRY_MONTH, card_details["expiry_month"])
        self.enter_text(self.EXPIRY_YEAR, card_details["expiry_year"])
        self.click_element(self.PAY_AND_CONFIRM_ORDER_BUTTON)
        self.is_visible(self.SUCCESS_MESSAGE)  
