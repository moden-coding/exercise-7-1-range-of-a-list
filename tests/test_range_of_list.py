#!/usr/bin/env python3

import contextlib
import io
import unittest

from src.range_of_list import range_of_list


class TestRangeOfList(unittest.TestCase):

    def test_worked_example(self):
        my_list = [3, 6, -4]
        result = range_of_list(my_list)
        self.assertEqual(
            result, 10,
            msg="range_of_list([3, 6, -4]) should be 10 (max 6 minus min -4). "
                "Got %r." % (result,))

    def test_various_lists(self):
        test_cases = [
            [1, 2, 3],
            [1, 3, 67, 7, 4, 23, 1, 5, 7, 4],
            [1],
            [33, 4, 4, 5, 7, 43, 32, 1, 3, 6, 7, 7, 4],
            [1, 1, 1, 1, 1, 1, 1],
            [0, 0, 1, 2, 3, 4, 5, 6, 7, 8],
            [-100, 10000, 2012, 123, -123, 3123, 323],
            [-123, 123, 43, 2345, 54564, 1234, 52, 6242],
        ]
        for values in test_cases:
            with self.subTest(values=values):
                expected = max(values) - min(values)
                result = range_of_list(values)
                self.assertIsNotNone(
                    result,
                    msg="range_of_list(%s) should return %s, not None. Make "
                        "sure your function uses return instead of print."
                        % (values, expected))
                self.assertEqual(
                    result, expected,
                    msg="range_of_list(%s) should be %s (max %s minus min "
                        "%s). Got %r." % (values, expected, max(values),
                                           min(values), result))

    def test_does_not_print(self):
        with contextlib.redirect_stdout(io.StringIO()) as out:
            range_of_list([1, 2, 3])
        printed = out.getvalue()
        self.assertEqual(
            printed, "",
            msg="range_of_list([1, 2, 3]) should not print anything itself; "
                "it should return the value and let the caller print it. Got "
                "printed output: %r." % (printed,))

    def test_single_element_list(self):
        result = range_of_list([42])
        self.assertEqual(
            result, 0,
            msg="range_of_list([42]) should be 0: with a single element, the "
                "max and min are the same value. Got %r." % (result,))


if __name__ == "__main__":
    unittest.main()
