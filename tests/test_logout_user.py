import pytest
from pages.logout_page import LoginPage
from utils.json_util import JSONUtil
from utils.take_screenshot import ScreenshotHelper

def test_logout_user(setup):
    driver = setup
    login_page = LoginPage(driver)

    data_file = "data/test_data.json"
    test_data = JSONUtil.read_json(data_file)
    login_details = test_data["login_details"]

    login_page.login_user(login_details["email"], login_details["password"])

    login_page.logout_user()

    ScreenshotHelper.take_screenshot(driver, "logout.png")