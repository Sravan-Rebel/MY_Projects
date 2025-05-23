from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from pages.base_page import BasePage

class ContactUsPage(BasePage):
    CONTACT_US = (By.XPATH, "//a[text()=' Contact us']")
    NAME_INPUT = (By.NAME, "name")
    EMAIL_INPUT = (By.NAME, "email")
    SUBJECT_INPUT = (By.NAME, "subject")
    MESSAGE_TEXT_AREA = (By.ID, "message")
    SUBMIT_BUTTON = (By.XPATH, "//input[@value='Submit']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(text(), 'Success! Your details have been submitted successfully.')]")
    HOME_BUTTON = (By.XPATH, "//span[text()=' Home']")

    ALERT_TEXT = "Press OK to proceed!"

    def fill_contact_form(self, name, email, subject, message):
        self.click_element(self.CONTACT_US)
        self.enter_text(self.NAME_INPUT, name)
        self.enter_text(self.EMAIL_INPUT, email)
        self.enter_text(self.SUBJECT_INPUT, subject)
        self.enter_text(self.MESSAGE_TEXT_AREA, message)

        # Click submit button
        self.click_element(self.SUBMIT_BUTTON)

        # Handle alert popup
        self.handle_alert()

    def handle_alert(self):
        """Handles the alert popup and clicks OK if text matches."""
        try:
            alert = Alert(self.driver)
            alert_text = alert.text  # Get alert message

            print(f"Alert detected: {alert_text}")

            if alert_text == self.ALERT_TEXT:
                alert.accept()  # Click the "OK" button
                print("Clicked 'OK' on the alert.")
            else:
                alert.dismiss()  # Click "Cancel" if text doesn't match
                print("Alert dismissed.")

        except Exception as e:
            print(f"No alert found or error occurred: {e}")

    def verify_submission_success(self):
        return self.is_visible(self.SUCCESS_MESSAGE)

    def navigate_to_home(self):
        self.click_element(self.HOME_BUTTON)