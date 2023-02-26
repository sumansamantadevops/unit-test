import unittest
import requests

class TestWebsite(unittest.TestCase):
    def test_website_access(self):
        url = "https://www.atg.world"
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
