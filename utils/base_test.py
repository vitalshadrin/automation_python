from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class BaseTest():
    driver = None
    
    def get(self, clazz):
        if self.driver is None : 
            self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        return clazz(self.driver)
    