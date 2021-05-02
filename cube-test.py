#!/usr/bin/env python

import cube
import unittest

class TestCalc(unittest.TestCase):
    def test_inputVal(self):
        self.assertIsInstance(cube.getUserInput(), int)

    def test_calc(self):
        self.assertEqual(cube.calc(3), 3 ** 3)

    def test_neg(self):
        self.assertRaises(ValueError, cube.calc, -1)


if __name__ == '__main__':
    unittest.main()
