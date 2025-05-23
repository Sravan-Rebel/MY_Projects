import pytest
from pages.brand_products_page import BrandPage,AnotherBrand
from utils.take_screenshot import ScreenshotHelper

def test_brand_product_details(setup):
    driver = setup
    brand_products_page =BrandPage(driver)
    another_brand_product_page=AnotherBrand(driver)

    brand_products_page.click_on_brand()
    another_brand_product_page.click_on_another_brand()

    ScreenshotHelper.take_screenshot(driver, "brand_product_page.png")