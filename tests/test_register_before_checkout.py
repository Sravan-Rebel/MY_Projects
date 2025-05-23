import pytest
from pages.register_before_checkout_page import HomePage, CartPage, RegistrationPage, CartDetails, OrderPage
from utils.json_util import JSONUtil
from utils.take_screenshot import ScreenshotHelper

def test_register_before_checkout(setup):
    driver = setup

    home_page = HomePage(driver)
    cart_page = CartPage(driver)
    registration_page = RegistrationPage(driver)
    cart_details = CartDetails(driver)
    order_page = OrderPage(driver)

    data_file = "data/test_data.json"
    test_data = JSONUtil.read_json(data_file)
    register_details = test_data["register_details1"]
    text_message = test_data["text_message"]
    card_details = test_data["card_details"]

    home_page.click_products()

    registration_page.register_user(register_details)

    home_page.add_first_product_to_cart()
    home_page.click_continue_shopping()
    home_page.click_on_cart()

    cart_page.click_on_proceed_to_checkout()
    cart_details.again_click_on_proceed_to_checkout(text_message)

    cart_details.enter_payment_details(card_details)

    order_page.click_on_delete_account()

    ScreenshotHelper.take_screenshot(driver, "register_before_checkout.png")