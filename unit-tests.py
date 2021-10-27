# -*- coding: utf-8 -*-
#!/usr/bin/python3

import unittest

# Module to be test.
import basic_stats as bs

class TestBasicStats(unittest.TestCase):

    def setUp(self):
        self._dc = bs.DataCapture()

    def test_no_values(self):
        stats = self._dc.build_stats()
        for i in range(bs.MAX_INTEGER_VALUE):
            self.assertEqual(stats.less(i), 0)
            self.assertEqual(stats.greater(i), 0)
        for i in range(bs.MAX_INTEGER_VALUE):
            for j in range(i, bs.MAX_INTEGER_VALUE):
                self.assertEqual(stats.between(i, j), 0)

    def test_one_value(self):
        for i in range(bs.MAX_INTEGER_VALUE):
            self._dc.add(i)
        stats = self._dc.build_stats()
        for i in range(bs.MAX_INTEGER_VALUE):
            self.assertEqual(stats.less(i), i)
            self.assertEqual(stats.greater(i), bs.MAX_INTEGER_VALUE - i - 1)

    def test_add_invalid_value(self):
        self.assertRaises(ValueError, self._dc.add, -1)
        self.assertRaises(ValueError, self._dc.add, bs.MAX_INTEGER_VALUE)
        self.assertRaises(ValueError, self._dc.add, bs.MAX_INTEGER_VALUE + 1)

    def test_less_invalid_value(self):
        stats = self._dc.build_stats()
        self.assertRaises(ValueError, stats.less, -1)
        self.assertRaises(ValueError, stats.less, bs.MAX_INTEGER_VALUE)
        self.assertRaises(ValueError, stats.less, bs.MAX_INTEGER_VALUE + 1)

    def test_greater_invalid_value(self):
        stats = self._dc.build_stats()
        self.assertRaises(ValueError, stats.greater, -1)
        self.assertRaises(ValueError, stats.greater, bs.MAX_INTEGER_VALUE)
        self.assertRaises(ValueError, stats.greater, bs.MAX_INTEGER_VALUE + 1)

    def test_between_invalid_value(self):
        stats = self._dc.build_stats()
        self.assertRaises(ValueError, stats.between, -1, 1)
        self.assertRaises(ValueError, stats.between, 0, bs.MAX_INTEGER_VALUE)
        self.assertRaises(ValueError, stats.between, 0, bs.MAX_INTEGER_VALUE + 1)

    def test_between_invalid_range(self):
        stats = self._dc.build_stats()
        self.assertRaises(IndexError, stats.between, 1, 0)
        self.assertRaises(IndexError, stats.between, bs.MAX_INTEGER_VALUE,  bs.MAX_INTEGER_VALUE - 1)
        self.assertRaises(IndexError, stats.between, bs.MAX_INTEGER_VALUE,  0)

    def test_normal_1(self):
        for x in [3, 9, 3, 4, 6]:
            self._dc.add(x)
        stats = self._dc.build_stats()
        self.assertEqual(stats.less(4), 2)
        self.assertEqual(stats.between(3, 6), 4)
        self.assertEqual(stats.greater(4), 2)

    def test_normal_2(self):
        """Sorted elements for easy check: [0, 0, 0, 2, 5, 6, 22, 44, 66, 100, 100, 100, 200, 500, 999]"""

        for x in [0, 0, 999, 100, 2, 44, 66, 100, 0, 5, 22, 100, 200, 500, 6]:
            self._dc.add(x)
        stats = self._dc.build_stats()
        self.assertEqual(stats.between(0, 0), 3)
        self.assertEqual(stats.less(2), 3)
        self.assertEqual(stats.between(2, 2), 1)
        self.assertEqual(stats.less(10), 6)
        self.assertEqual(stats.less(100), 9)
        self.assertEqual(stats.between(100, 100), 3)
        self.assertEqual(stats.between(150, 150), 0)
        self.assertEqual(stats.greater(100), 3)
        self.assertEqual(stats.greater(400), 2)

if __name__ == '__main__':
    unittest.main()
