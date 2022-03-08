
import unittest
from page_objects.herokuapp.hovers_page import HoversPage
from utils.base_test import BaseTest
from page_objects.herokuapp.home_page import HomePage


class HoversPageTests(BaseTest):


    def test_1_hovers_page(self):
        self.get(HomePage).open().click_link('Hovers')
        self.get(HoversPage).check_title()
        pass
        
    def test_2_hover_data(self):
        self.get(HoversPage).check_sub_title()
        pass

if __name__ == '__main__':
    unittest.main()
