import pytest
from pages.remove_product_page import HomePage, RemoveProduct
from utils.take_screenshot import ScreenshotHelper

def test_remove_product_from_cart(setup):
    driver = setup

    home_page = HomePage(driver)
    remove_product = RemoveProduct(driver)

    home_page.click_products()
    home_page.add_first_product_to_cart()
    home_page.click_continue_shopping()
    home_page.click_on_cart()

    remove_product.click_on_remove_button()
    remove_product.is_visible(remove_product.REMOVED_MESSAGE)

    ScreenshotHelper.take_screenshot(driver, "remove_product_page.png")