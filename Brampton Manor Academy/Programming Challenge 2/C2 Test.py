import unittest
from C2 import*

class TestSum(unittest.TestCase):

    def test_joules(self):
        self.assertEqual(richtertojoules(0), 63095.7344480193)

    def test_tnt(self):
        self.assertEqual(joulestotnt(0), 15080242458895.625)

if __name__ == '__main__':
    unittest.main()
