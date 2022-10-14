import unittest
from C4 import*

class TestSum(unittest.TestCase):

    def testQuantify(self):
        self.assertEqual(quantify(3.5, 18), -16.47884113003356)

if __name__ == '__main__':
    unittest.main()
