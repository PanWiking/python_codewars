import unittest

from isograms.resolve_1 import is_isogram


class TestResolve1(unittest.TestCase):
    def test_isogram(self):
        self.assertEqual(is_isogram("isogram"), True)

    def test_aba(self):
        self.assertEqual(is_isogram("aba"), False)

    def test_big_small(self):
        self.assertEqual(is_isogram("aA"), False)

    def test_empty(self):
        self.assertEqual(is_isogram(""), True)
