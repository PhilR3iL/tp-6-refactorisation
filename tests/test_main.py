import unittest
from main import compute_area, find_max, multiply_and_add

class TestRefactorisation(unittest.TestCase):
    def test_compute_area(self):
        self.assertAlmostEqual(compute_area(3), 28.27431, places=5)
        self.assertAlmostEqual(compute_area(0), 0)

    def test_find_max(self):
        self.assertEqual(find_max(1, 2, 3), 3)
        self.assertEqual(find_max(5, 3, 1), 5)
        self.assertEqual(find_max(1, 7, 7), 7)

    def test_multiply_and_add(self):
        self.assertEqual(multiply_and_add(2, 3, 4), 10)
        self.assertEqual(multiply_and_add(0, 5, 1), 1)
        self.assertEqual(multiply_and_add(-2, 3, 4), -2)

if __name__ == '__main__':
    unittest.main()
