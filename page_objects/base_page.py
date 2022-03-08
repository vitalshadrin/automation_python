from selenium.webdriver.wpewebkit.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class BasePage:
    By = None
    driver = None

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.By = By

    def click_link(self, link: str):
        self.driver.find_element(by=self.By.LINK_TEXT, value=link).click()

    def click(self, element: WebElement):
        self.driver.find_element(value=element).click()

    def open(self, url: str):
        self.driver.get(url)
