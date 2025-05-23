import pytest
from pages.view_category_page import ViewCategory, ViewMenCategory
from utils.take_screenshot import ScreenshotHelper

def test_view_category_details(setup):
    driver = setup
    view_category_page = ViewCategory(driver)
    view_men_category_page = ViewMenCategory(driver)

    view_category_page.click_on_category()
    view_men_category_page.click_on_men_category()
    
    ScreenshotHelper.take_screenshot(driver, "view_category.png")