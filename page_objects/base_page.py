from selenium.webdriver.wpewebkit.webdriver import WebDriver

class BasePage: 
   driver = None
   
   def __init__(self, driver : WebDriver) -> None:
      self.driver = driver 
       
