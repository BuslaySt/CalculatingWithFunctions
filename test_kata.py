from kata import *
import unittest


class Test_Generate_Hashtag(unittest.TestCase):
    def tests(self):
        # self.assertEqual(inc_dec.increment(3), 4)
        self.assertEquals(seven(times(five())), 35)
        self.assertEquals(four(plus(nine())), 13)
        self.assertEquals(eight(minus(three())), 5)
        self.assertEquals(six(divided_by(two())), 3)

if __name__ == '__main__':
    unittest.main()
