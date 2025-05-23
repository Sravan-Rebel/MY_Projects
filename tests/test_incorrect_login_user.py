import pytest
from pages.incorrect_login_page import LoginPage
from utils.json_util import JSONUtil
from utils.take_screenshot import ScreenshotHelper

def test_incorrect_login_user(setup):
    driver = setup
    login_page = LoginPage(driver)

    data_file = "data/test_data.json"
    test_data = JSONUtil.read_json(data_file)
    incorrect_login_details = test_data["incorrect_login_details"]

    login_page.login_user(incorrect_login_details["email"], incorrect_login_details["password"])

    ScreenshotHelper.take_screenshot(driver, "login_fail.png")