import support

import unittest

class Test(unittest.TestCase):

    def test_urlChecker(self):
        LulzParse = support.Lulz3Support()
        self.assertTrue(LulzParse.urlChecker('https://www.google.com'))
        self.assertFalse(LulzParse.urlChecker('https://ChrisSucksAtPython.com'))

if __name__ == '__main__':
    unittest.main()