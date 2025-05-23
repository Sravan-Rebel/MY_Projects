import pytest
from pages.verify_products_quantity_page import ProductsQuantityPage
from pages.verfity_cart_page import VerifyCartPage
from utils.take_screenshot import ScreenshotHelper

def test_verify_product_quantity_in_cart(setup):
    driver=setup
    products_page=ProductsQuantityPage(driver)
    cart_page=VerifyCartPage(driver)

    products_page.click_view_product()
    products_page.set_product_quantity(4)
    products_page.click_add_to_cart()
    products_page.click_view_cart()

    cart_page.get_cart_product_quantity()
    ScreenshotHelper.take_screenshot(driver,"verify_cart_page.png")