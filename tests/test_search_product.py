import pytest
from pages.search_product_page import SearchProductsPage
from utils.take_screenshot import ScreenshotHelper

def test_product_details(setup):
    driver = setup
    search_products_page = SearchProductsPage(driver)

    search_products_page.open_all_products_page()
    search_products_page.is_visible(search_products_page.ALL_PRODUCTS_HEADER)
    search_products_page.search_product("Tops")
    search_products_page.verify_search_results()

    ScreenshotHelper.take_screenshot(driver, "search_product_page.png")