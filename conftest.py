import pytest
from utils.driver_factory import DriverFactory
from config.config import Config

@pytest.fixture(scope="function")
def setup():
    driver = DriverFactory().get_driver()
    driver.set_page_load_timeout(300)
    driver.get(Config.BASE_URL)
    yield driver
    driver.quit()