import pytest
from pages.verify_subscription_page import VerifySubscription
from utils.take_screenshot import ScreenshotHelper

def test_verify_subscription(setup):
    driver=setup
    verify_subscription=VerifySubscription(driver)

    verify_subscription.scroll_to_footer()
    verify_subscription.verify_subscription_text()
    verify_subscription.subscribe_to_newsletter("meghanakanduluru@gmail.com")
    verify_subscription.verify_success_message()
    ScreenshotHelper.take_screenshot(driver, "verify_subscription_page.png")