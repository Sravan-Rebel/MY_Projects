from selenium.webdriver.common.by import By

class ScrollHelper:
    def __init__(self,driver):
        self.driver=driver
    
    def scroll_by_pixels(self,x,y):
        """
        scrolls the page by the specified number of pixels
        param x: Horizonal pixel(positive for right,negative for left)
        param y: Vertical pixel(postive for down,negative for up)
        """
        self.driver.execute_script(f"window.scrollBy({x},{y});")
    
    def scroll_to_bottom(self):
        """ 
        Scrolls to the bottom of the page
        """
        self.driver.execute_script(f"window.scrollTo(0,document.body.scrollHeight);")
    
    def scroll_to_top(self):
        """ 
        Scrolls to the top of the page.
        """
        self.driver.execute_script(f"window.scrollTo(0,0);")
    
    def scroll_to_element(self,element):
        """
        Scrolls the page to make the given element visible
        : param element: WebElement to scroll to 
        """
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

