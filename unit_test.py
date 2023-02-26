import unittest
import requests

class TestWebsiteAccessibility(unittest.TestCase):
    
    def test_website_accessibility(self):
        # Replace "https://www.example.com" with the URL of the website you want to test
        response = requests.get("https://atg.world")
        # Assert that the status code is 200, which indicates that the website is accessible
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
