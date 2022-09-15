import unittest
from C1 import*

class TestSum(unittest.TestCase):

    def test_metres(self):
        self.assertEqual(getmeters(10), 50.292)

    def test_furlongs(self):
        self.assertEqual(getfurlongs(10), 0.25)
    

if __name__ == '__main__':
    unittest.main()
    
                
