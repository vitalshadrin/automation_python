from page_objects.base_page import BasePage


class HoversPage(BasePage):

    def __init__(self, driver) -> None:
        super().__init__(driver)
        
    def check_title(self):
        assert self.driver.find_element_by_tag_name('h3').is_displayed()
        return self    
