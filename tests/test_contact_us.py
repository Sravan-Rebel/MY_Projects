import pytest
from pages.contact_us_page import ContactUsPage
from utils.json_util import JSONUtil
from utils.take_screenshot import ScreenshotHelper
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoAlertPresentException

def test_contact_us_form(setup):
    driver = setup
    contact_us_page = ContactUsPage(driver)

    # Handle any unexpected alerts at the start
    try:
        alert = Alert(driver)
        alert.accept()
        print("Unexpected alert handled at the beginning.")
    except NoAlertPresentException:
        print("No alert present at the beginning.")

    # Load test data from JSON
    data_file = "data/test_data.json"
    test_data = JSONUtil.read_json(data_file)
    contact_details = test_data["contact_us_details"]

    # Fill the contact us form
    contact_us_page.fill_contact_form(
        name=contact_details["name"],
        email=contact_details["email"],
        subject=contact_details["subject"],
        message=contact_details["message"]
        # file_path=contact_details["file_path"] if needed
    )

    # Submit the form and handle alert
    try:
        contact_us_page.handle_alert()
        print("Alert handled successfully after form submission.")
    except NoAlertPresentException:
        print("No alert appeared after form submission.")

    # Verify submission success
    assert contact_us_page.verify_submission_success(), "Submission failed, success message not visible"

    # Navigate to home page after form submission
    contact_us_page.navigate_to_home()

    # Take a screenshot after submission
    ScreenshotHelper.take_screenshot(driver, "contact_us_page.png")

    print("Test completed successfully.")