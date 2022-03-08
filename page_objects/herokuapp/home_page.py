from page_objects.base_page import BasePage


class HomePage(BasePage):

    def __init__(self, driver) -> None:
        super().__init__(driver)

    def open(self):
        super().open('http://the-internet.herokuapp.com/')
        return self

    def click_link(self, link: str):
        super().click_link(link)
        return self
