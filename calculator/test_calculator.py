import unittest

from calculator import add_numbers


class TestAddNumbers(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(add_numbers(2, 3), 5)

    def test_negative(self):
        self.assertEqual(add_numbers(-1, -1), -2)

    def test_float(self):
        self.assertAlmostEqual(add_numbers(0.1, 0.2), 0.3, places=7)


if __name__ == "__main__":
    unittest.main()
