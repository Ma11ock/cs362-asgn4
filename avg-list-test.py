#!/usr/bin/env python

import avg_list
import unittest

class TestCalc(unittest.TestCase):
    def test_listpop(self):
        self.assertRaises(ValueError, avg_list.findAvg, [])

    def test_avg(self):
        self.assertEqual(avg_list.findAvg([1, 1, 1]), 1)

    # Will fail intentionally.
    def test_will_run(self):
        self.fail(avg_list.findAvg(10))


if __name__ == '__main__':
    unittest.main()

