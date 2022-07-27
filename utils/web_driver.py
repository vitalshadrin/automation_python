
import enum
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class CreateWebDriver:

    drivers = enum.Enum(value='drivers', names=('chrome firefox'))

    @classmethod
    def createWebDriver(self, driver: drivers):
        if(driver is self.drivers.chrome):
            return webdriver.Chrome(
                service=Service(ChromeDriverManager().install()))
        elif(driver is self.drivers.firefox):
            return webdriver.Firefox(
                service=Service(GeckoDriverManager().install()))
