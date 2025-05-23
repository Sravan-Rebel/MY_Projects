from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class ViewCategory(BasePage):
    CATEGORY = (By.XPATH, "//h2[text()='Category']")
    WOMEN_CATEGORY = (By.XPATH, "//a[@href='#Women']")
    DRESS_BUTTON = (By.XPATH, "//a[text()='Dress ']")
    DRESS_PRODUCT = (By.XPATH, "//h2[@class='title text-center']")

    def click_on_category(self):
        self.is_visible(self.CATEGORY)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.CATEGORY)
            )
            
            women_category_element = self.driver.find_element(*self.WOMEN_CATEGORY)
            self.driver.execute_script("arguments[0].scrollIntoView();", women_category_element)

            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.WOMEN_CATEGORY)
            ).click()

            dress_button_element = self.driver.find_element(*self.DRESS_BUTTON)
            self.driver.execute_script("arguments[0].scrollIntoView();", dress_button_element)

            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.DRESS_BUTTON)
            ).click()

            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.DRESS_PRODUCT)
            )
        except TimeoutException as e:
            print("Timed out waiting for category elements to load or become clickable.")
            raise e

class ViewMenCategory(BasePage):  
    MEN_CATEGORY = (By.XPATH, "//a[@href='#Men']")
    MEN_SUBCATEGORY = (By.XPATH, "//a[text()='Tshirts ']")
    MEN_SUBCATEGORY_PRODUCT = (By.XPATH, "//h2[text()='Men - Tshirts Products']")

    def click_on_men_category(self):
        self.click_element(self.MEN_CATEGORY)
        self.click_element(self.MEN_SUBCATEGORY)
        self.is_visible(self.MEN_SUBCATEGORY_PRODUCT)