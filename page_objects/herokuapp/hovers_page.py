from page_objects.base_page import BasePage


class HoversPage(BasePage):
    title = 'h3'
    subTitle = 'p'

    def __init__(self, driver) -> None:
        super().__init__(driver)

    def check_title(self):
        assert self.driver.find_element(
            by=self.By.TAG_NAME, value=self.title).is_displayed()
        return self

    def check_sub_title(self):
        assert self.driver.find_element(
            by=self.By.TAG_NAME, value=self.subTitle).is_displayed()
        return self
