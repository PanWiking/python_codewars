import unittest

from sum_of_digits.resolve_1 import digital_root


class TestResolve1(unittest.TestCase):

    def test_number_22(self):
        self.assertEqual(digital_root(22), 4)

    def test_number_29(self):
        self.assertEqual(digital_root(29), 2)
