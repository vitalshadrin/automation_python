from page_objects.base_page import BasePage

class HomePage(BasePage):

    def __init__(self, driver) -> None:
        super().__init__(driver)

    def open(self):
        self.driver.get('http://the-internet.herokuapp.com/')
        return self

    def click_link(self, link: str):
        self.driver.find_element_by_link_text(link).click()
        return self