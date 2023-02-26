import unittest
import requests

class TestWebsiteAccessibility(unittest.TestCase):

    def test_website_accessibility(self):
        
        response = requests.get("https://www.atg.world")
        
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()


