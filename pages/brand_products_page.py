from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BrandPage(BasePage):
    PRODUCTS_BUTTON = (By.XPATH, "//a[text()=' Products']")
    BRAND_BUTTON=(By.XPATH,"//h2[text()='Brands']")
    BRAND_PRODUCT=(By.XPATH,"//a[@href='/brand_products/Polo']")
    BRAND_PRODUCT_DETAILS=(By.XPATH,"//h2[text()='Brand - Polo Products']")
    '''
    def click_on_brand(self):
        self.click_element(self.PRODUCTS_BUTTON)
        self.is_visible(self.BRAND_BUTTON)
        self.click_element(self.BRAND_PRODUCT)
        self.is_visible(self.BRAND_PRODUCT_DETAILS)
    '''
    def click_on_brand(self):
        self.click_element(self.PRODUCTS_BUTTON)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.BRAND_BUTTON))
        self.click_element(self.BRAND_PRODUCT)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.BRAND_PRODUCT_DETAILS))

class AnotherBrand(BasePage):
    ANOTHER_BRAND_PRODUCT=(By.XPATH,"//a[@href='/brand_products/H&M']")
    ANOTHER_BRAND_PRODUCT_DETAILS=(By.XPATH,"//h2[text()='Brand - H&M Products']")
    '''
    def click_on_another_brand(self):
        self.click_element(self.ANOTHER_BRAND_PRODUCT)
        self.is_visible(self.ANOTHER_BRAND_PRODUCT_DETAILS)
    '''

    def click_on_another_brand(self):
        self.click_element(self.ANOTHER_BRAND_PRODUCT)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.ANOTHER_BRAND_PRODUCT_DETAILS))
