import pytest
from pages.login_before_checkout_page import HomePage, CartPage, LoginPage, CartDetails
from utils.json_util import JSONUtil
from utils.take_screenshot import ScreenshotHelper

def test_login_before_checkout(setup):
    driver = setup
    home_page = HomePage(driver)
    cart_page = CartPage(driver)
    login_page = LoginPage(driver)
    cart_details = CartDetails(driver)

    data_file = "data/test_data.json"
    test_data = JSONUtil.read_json(data_file)
    login_details = test_data["login_details"]
    text_message = test_data["text_message"]
    card_details = test_data["card_details"]

    assert driver.title == "Automation Exercise", "Home page not loaded successfully"
    login_page.login_user(login_details["email"], login_details["password"])
    assert login_page.is_visible(login_page.LOGGED_IN_TEXT), "Login not successful"

    home_page.click_products()
    home_page.add_first_product_to_cart()
    home_page.click_continue_shopping()

    home_page.click_on_cart()
    assert "Shopping Cart" in driver.page_source, "Cart page not displayed"

    cart_page.click_on_proceed_to_checkout()
    cart_details.again_click_on_proceed_to_checkout(text_message)
    cart_details.enter_payment_details(card_details)
    assert cart_details.is_visible(cart_details.SUCCESS_MESSAGE), "Order confirmation failed"

    ScreenshotHelper.take_screenshot(driver, "login_before_checkout_page.png")