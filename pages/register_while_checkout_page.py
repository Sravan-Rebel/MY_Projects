from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select
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

class CartPage(BasePage):
    PROCEED_TO_CHECKOUT = (By.XPATH, "//a[text()='Proceed To Checkout']")
    REGISTER_OR_LOGIN_BUTTON= (By.XPATH, "//u[text()='Register / Login']")

    def click_on_proceed_to_checkout(self):
        self.click_element(self.PROCEED_TO_CHECKOUT)

    def click_on_register_or_login(self):
        self.click_element(self.REGISTER_OR_LOGIN_BUTTON)

class RegistrationPage(BasePage):
    SIGNUP_LOGIN_BUTTON = (By.XPATH, "//a[contains(text(), ' Signup / Login')]")
    NEW_USER_SIGNUP_TEXT = (By.XPATH, "//h2[contains(text(),'New User Signup!')]")
    NAME_INPUT = (By.NAME, "name")
    EMAIL_INPUT = (By.XPATH, "//input[@data-qa='signup-email']")
    SIGNUP_BUTTON = (By.XPATH, "//button[@data-qa='signup-button']")
    ACCOUNT_INFO_TEXT = (By.XPATH, "//b[text()='Enter Account Information']")
    PASSWORD_INPUT = (By.XPATH, "//input[@id='password']")
    NEWSLETTER_CHECKBOX = (By.XPATH, "//input[@id='newsletter']")
    OFFERS_CHECKBOX = (By.XPATH, "//input[@id='optin']")
    FIRST_NAME_INPUT = (By.XPATH, "//input[@id='first_name']")
    LAST_NAME_INPUT = (By.XPATH, "//input[@id='last_name']")
    COMPANY_INPUT = (By.XPATH, "//input[@id='company']")
    ADDRESS1_INPUT = (By.XPATH, "//input[@id='address1']")
    ADDRESS2_INPUT = (By.XPATH, "//input[@id='address2']")
    COUNTRY_DROPDOWN = (By.XPATH, "//*[@id='country']")
    STATE_INPUT = (By.XPATH, "//input[@id='state']")
    CITY_INPUT = (By.XPATH, "//input[@id='city']")
    ZIPCODE_INPUT = (By.XPATH, "//input[@id='zipcode']")
    MOBILE_NUMBER_INPUT = (By.XPATH, "//input[@id='mobile_number']")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[@data-qa='create-account']")
    ACCOUNT_CREATED_TEXT = (By.XPATH, "//b[text()='Account Created!']")
    CONTINUE_BUTTON = (By.XPATH, "//a[text()='Continue']")
    LOGGED_IN_TEXT = (By.XPATH, "//a[text()=' Logged in as ']")

    def register_user(self, register_details):
        self.click_element(self.SIGNUP_LOGIN_BUTTON)
        assert self.is_visible(self.NEW_USER_SIGNUP_TEXT)
        self.enter_text(self.NAME_INPUT, register_details["name"])
        self.enter_text(self.EMAIL_INPUT, register_details["email"])
        self.click_element(self.SIGNUP_BUTTON)
        self.enter_text(self.PASSWORD_INPUT, register_details["password"])
        self.driver.find_element(*self.NEWSLETTER_CHECKBOX)
        self.driver.find_element(*self.OFFERS_CHECKBOX)
        self.enter_text(self.FIRST_NAME_INPUT, register_details["first_name"])
        self.enter_text(self.LAST_NAME_INPUT, register_details["last_name"])
        self.enter_text(self.COMPANY_INPUT, register_details["company"])
        self.enter_text(self.ADDRESS1_INPUT, register_details["address1"])
        self.enter_text(self.ADDRESS2_INPUT, register_details["address2"])
        Select(self.driver.find_element(*self.COUNTRY_DROPDOWN)).select_by_visible_text(register_details["country"])
        self.enter_text(self.STATE_INPUT, register_details["state"])
        self.enter_text(self.CITY_INPUT, register_details["city"])
        self.enter_text(self.ZIPCODE_INPUT, register_details["zipcode"])
        self.enter_text(self.MOBILE_NUMBER_INPUT, register_details["mobile_number"])
        self.click_element(self.CREATE_ACCOUNT_BUTTON)
        assert self.is_visible(self.ACCOUNT_CREATED_TEXT)
        self.click_element(self.CONTINUE_BUTTON)
        assert self.is_visible(self.LOGGED_IN_TEXT)

class CartDetails(BasePage):
    CART_BUTTON = (By.XPATH, "//a[text()=' Cart']")
    PROCEED_TO_CHECKOUT = (By.XPATH, "//a[text()='Proceed To Checkout']")
    TEXT_MESSAGE = (By.NAME, "message")
    PLACE_ORDER = (By.XPATH, "//a[text()='Place Order']")
    CARD_NAME_INUPT = (By.NAME, "name_on_card")
    CARD_NUMBER = (By.NAME, "card_number")
    CVC = (By.NAME, "cvc")
    EXPIRY_MONTH =(By.NAME, "expiry_month")
    EXPIRY_YEAR =(By.NAME, "expiry_year")
    PAY_AND_CONFIRM_ORDER_BUTTON = (By.XPATH, "//button[@id='submit']")
    SUCCESS_MESSAGE = (By.XPATH, "//p[text()='Congratulations! Your order has been confirmed!']")
    
    def click_on_cart(self):
        self.click_element(self.CART_BUTTON)

    def again_click_on_proceed_to_checkout(self, text_message):
        self.click_element(self.PROCEED_TO_CHECKOUT)
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

class OrderPage(BasePage):
    DELETE_ACCOUNT_BUTTON = (By.XPATH, "//a[text()=' Delete Account']")
    ACCOUNT_DELETED_TEXT = (By.XPATH, "//b[text()='Account Deleted!']")
    CONTINUE =(By.XPATH, "//a[text()='Continue']")
    
    def click_on_delete_account(self):
        self.click_element(self.DELETE_ACCOUNT_BUTTON)
        self.is_visible(self.ACCOUNT_DELETED_TEXT)
        self.click_element(self.CONTINUE)