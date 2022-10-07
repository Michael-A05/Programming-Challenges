import unittest
from C3 import*

class TestValue(unittest.TestCase):
    def calculation(self):
        self.assertIsEqual(calculation(15), 15)

if __name__ == '__main__':
    unittest.main()
