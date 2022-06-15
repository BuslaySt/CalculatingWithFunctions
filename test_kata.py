from kata import *
import unittest

class Test_Generate_Hashtag(unittest.TestCase):
    def tests(self):
        self.assertEqual(seven(times(five())), 35)
        self.assertEqual(four(plus(nine())), 13)
        self.assertEqual(eight(minus(three())), 5)
        self.assertEqual(six(divided_by(two())), 3)

if __name__ == '__main__':
    unittest.main()
