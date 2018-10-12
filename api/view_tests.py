import unittest
import requests
import config as cfg


def test_body(url):
    r = requests.get(url)
    return r.content


class TestStringMethods(unittest.TestCase):

    def tests(self):
        self.assertEqual(test_body(cfg.BASE_URL), "I'm not a teapot")

        self.assertEqual(test_body(cfg.BASE_URL + cfg.API), "I'm not a teapot")


if __name__ == '__main__':
    unittest.main()
