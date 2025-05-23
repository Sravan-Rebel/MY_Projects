import pytest
from pages.exist_register_page import RegistrationPage
from utils.json_util import JSONUtil
from utils.take_screenshot import ScreenshotHelper


def test_exist_register_user(setup):
    driver = setup
    register_page = RegistrationPage(driver)

    data_file = "data/test_data.json"
    test_data = JSONUtil.read_json(data_file)
    existing_login_details = test_data["existing_login_details"]

    register_page.register_user(existing_login_details["name"], existing_login_details["email"])
    register_page.verify_login_exist()
    ScreenshotHelper.take_screenshot(driver, "exist_user_page.png")