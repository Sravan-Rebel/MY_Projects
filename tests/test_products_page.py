import pytest
from pages.products_page import ProductsPage
from utils.take_screenshot import ScreenshotHelper

def test_verify_all_products_and_product_details(setup):
    driver = setup
    products_page = ProductsPage(driver)

    products_page.open_all_products_page()
    products_page.verify_products_list()
    products_page.open_first_product_details()
    products_page.verify_product_details()

    ScreenshotHelper.take_screenshot(driver, "product_details.png")