import pytest
from pages.testcase_page import TestCasesPage
from utils.take_screenshot import ScreenshotHelper

def test_tescases(setup):
    driver = setup
    test_cases_page = TestCasesPage(driver)
    test_cases_page.open_test_cases_page()
    test_cases_page.verify_test_cases_page()
    ScreenshotHelper.take_screenshot(driver, "testcases_page.png")