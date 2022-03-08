
import unittest
from utils.web_driver import CreateWebDriver


class BaseTest(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = CreateWebDriver.createWebDriver(CreateWebDriver.drivers.chrome)

    def get(self, clazz):
        return clazz(self.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
