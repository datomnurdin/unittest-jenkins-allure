import unittest
from scrap_scenario import scraping

class TestParseFunction(unittest.TestCase):

    def setUp(self):
        self.output = scraping('https://www.theedgemarkets.com/categories/corporate?page=', 1)

    def tearDown(self):
        self.output = []

    def test_output_is_not_none(self):
        self.assertIsNotNone(self.output)

    def test_output_is_a_list(self):
        self.assertTrue(isinstance(self.output, list))

    def test_output_is_a_list_of_dicts(self):
        self.assertTrue(all(isinstance(elem, dict) for elem in self.output))


if __name__ == '__main__':
    unittest.main()