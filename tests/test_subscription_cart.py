import pytest
from pages.subscription_cart_page import VerifySubscriptionCart
from utils.take_screenshot import ScreenshotHelper

def test_verify_subscription(setup):
    driver=setup
    verify_subscription=VerifySubscriptionCart(driver)

    verify_subscription.go_to_cart()
    verify_subscription.scroll_to_footer()
    verify_subscription.verify_subscription_text()
    verify_subscription.subscribe_to_newsletter("meghanakanduluru@gmail.com")
    verify_subscription.verify_success_message()
    ScreenshotHelper.take_screenshot(driver, "verify_subscription_cart_page.png")