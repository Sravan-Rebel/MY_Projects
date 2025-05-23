from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SearchProductsPage(BasePage):
    PRODUCTS_BUTTON = (By.XPATH, "//a[text()=' Products']")
    ALL_PRODUCTS_HEADER = (By.XPATH, "//h2[text()='All Products']")
    SEARCH_INPUT = (By.NAME, "search")
    SEARCH_BUTTON = (By.ID, "submit_search")
    SEARCHED_PRODUCTS_HEADER = (By.XPATH, "//h2[text()='Searched Products']")
    PRODUCT_LIST = (By.CLASS_NAME, "features_items")

    def open_all_products_page(self):
        self.click_element(self.PRODUCTS_BUTTON)
        self.is_visible(self.ALL_PRODUCTS_HEADER)

    def search_product(self, product_name):
        self.enter_text(self.SEARCH_INPUT, product_name)
        self.click_element(self.SEARCH_BUTTON)

    def verify_search_results(self):
        self.is_visible(self.SEARCHED_PRODUCTS_HEADER)
        len(self.driver.find_elements(*self.PRODUCT_LIST)) > 0