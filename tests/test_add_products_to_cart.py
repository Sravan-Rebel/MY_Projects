import pytest
from pages.add_products_page import ProductsPage
from pages.add_products_cart_page import CartPage
from utils.take_screenshot import ScreenshotHelper


def test_add_products_to_cart(setup):
    driver=setup
    products_page=ProductsPage(driver)
    cart_page=CartPage(driver)

    products_page.click_products()
    products_page.add_first_product_to_cart()
    products_page.click_continue_shopping()
    products_page.add_second_product_to_cart()
    products_page.click_view_cart()

    assert cart_page.get_product_count()==2, "two products should added to cart" 
    assert len(cart_page.get_product_price())==2, "price of the products should be displayed"
    assert len(cart_page.get_product_quantity())==2, "quantity of the product should be displayed"
    assert len(cart_page.get_total_price())==2,"total price of the products should be displayed"

    ScreenshotHelper.take_screenshot(driver, "products_added_to_cart.png")


