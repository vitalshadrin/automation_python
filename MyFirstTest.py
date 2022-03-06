from page_objects.herokuapp.hovers_page import HoversPage
from utils.base_test import BaseTest
from page_objects.herokuapp.home_page import HomePage


class TestClass(BaseTest):

    def test(self):
        self.get(HomePage).open().click_link('Hovers')
        self.get(HoversPage).check_title()  
        self.driver.close()


test = TestClass()
test.test()
