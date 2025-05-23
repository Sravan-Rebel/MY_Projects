from selenium.webdriver.common.by import By
from pages.base_page import BasePage

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