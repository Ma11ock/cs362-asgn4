#!/usr/bin/env python

import name
import unittest

class TestCalc(unittest.TestCase):
    def test_name_combine(self):
        self.assertEqual(name.genName("Kyle", "McDermott"), "Kyle McDermott")
    # Will fail intentionally.
    def test_name_combine_not_str(self):
        self.fail(name.genName("Andrena", []))
    # Will fail if you send C-d to stdin.
    def test_get_first_name(self):
        self.fail(name.getFirstName())

if __name__ == '__main__':
    unittest.main()
