from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains

class VerifySubscriptionCart(BasePage):
    CART_BUTTON=(By.XPATH,"//a[text()=' Cart']")
    FOOTER=(By.ID,"footer")
    SUBSCRIPTION_TEXT=(By.XPATH,"//h2[text()='Subscription']")
    EMAIL_INPUT=(By.ID,"susbscribe_email")
    SUBSCRIBE_BUTTON=(By.ID,"subscribe")
    SUCCESS_MESSAGE=(By.CLASS_NAME,"alert-success alert")

    def go_to_cart(self):
        self.click_element(self.CART_BUTTON)

    def scroll_to_footer(self):
        footer_element=self.driver.find_element(*self.FOOTER)

        ActionChains(self.driver).move_to_element(footer_element).perform()
    
    def verify_subscription_text(self):
        self.is_visible(self.SUBSCRIPTION_TEXT)
    
    def subscribe_to_newsletter(self,email):
        self.enter_text(self.EMAIL_INPUT,email)
        self.click_element(self.SUBSCRIBE_BUTTON)

    def verify_success_message(self):
        self.is_visible(self.SUCCESS_MESSAGE)