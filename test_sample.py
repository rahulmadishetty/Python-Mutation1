# test_sample.py

import unittest
from sample import add

class TestSample(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1, 2), 3)

if __name__ == '__main__':
    unittest.main()
