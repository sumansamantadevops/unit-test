import unittest
from selenium import webdriver

class TestWebsite(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_website_loads_properly(self):
        self.driver.get("https://www.atg.world")
        self.assertEqual(self.driver.title, "ATG - Your Travel Guide")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
