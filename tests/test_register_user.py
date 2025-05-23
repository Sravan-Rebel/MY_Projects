import pytest
from pages.registration_page import RegistrationPage
from utils.json_util import JSONUtil
from utils.take_screenshot import ScreenshotHelper

def test_register_user(setup):
    driver = setup
    registration_page = RegistrationPage(driver)

    # Load data from JSON file
    data_file = "data/test_data.json"
    test_data = JSONUtil.read_json(data_file)
    user_details = test_data["user_details"]

    registration_page.register_user(user_details)
    ScreenshotHelper.take_screenshot(driver, "registered_page.png")