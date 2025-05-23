from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select

class RegistrationPage(BasePage):
    SIGNUP_LOGIN_BUTTON = (By.XPATH, "//a[contains(text(), ' Signup / Login')]")
    NEW_USER_SIGNUP_TEXT = (By.XPATH, "//h2[contains(text(),'New User Signup!')]")
    NAME_INPUT = (By.NAME, "name")
    EMAIL_INPUT = (By.XPATH, "//input[@data-qa='signup-email']")
    SIGNUP_BUTTON = (By.XPATH, "//button[@data-qa='signup-button']")
    EXIST_ERROR_MESSAGE=(By.XPATH,"//p[text()='Email Address already exist!']")

    def register_user(self,name,email):
        self.click_element(self.SIGNUP_LOGIN_BUTTON)
        assert self.is_visible(self.NEW_USER_SIGNUP_TEXT)
        self.enter_text(self.NAME_INPUT,name)
        self.enter_text(self.EMAIL_INPUT,email)
        self.click_element(self.SIGNUP_BUTTON)

    def verify_login_exist(self):
        assert self.is_visible(self.EXIST_ERROR_MESSAGE)    