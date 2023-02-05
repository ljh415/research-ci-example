import unittest

import main


class MainTest(unittest.TestCase):
    def test_helloworld(self):
        ret = main.helloworld("test")
        self.assertEqual(ret, "Hello World! test!")


if __name__ == "__main__":
    unittest.main()
