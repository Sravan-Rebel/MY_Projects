import os
from datetime import datetime

class ScreenshotHelper:
    @staticmethod
    def take_screenshot(driver, file_name=None):
        if not file_name:
            file_name = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".png"
        screenshots_dir = "screenshots"
        if not os.path.exists(screenshots_dir):
            os.makedirs(screenshots_dir)
        file_path = os.path.join(screenshots_dir, file_name)
        driver.save_screenshot(file_path)
        print(f"Screenshot saved at {file_path}")