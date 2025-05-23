from selenium import webdriver
from config.config import Config
from webdriver_manager.chrome import ChromeDriverManager

class DriverFactory:
    @staticmethod
    def get_driver():
        if Config.BROWSER.lower() == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("--start-maximized")
            options.add_argument("--disable-infobars")
            options.add_argument("--disable-popup-blocking")
            options.add_argument("--remote-allow-origins=*") 
            driver = webdriver.Chrome(service=webdriver.ChromeService(ChromeDriverManager().install()))  # No comma here
            return driver
        else:
            raise ValueError(f"Browser {Config.BROWSER} is not supported.")
