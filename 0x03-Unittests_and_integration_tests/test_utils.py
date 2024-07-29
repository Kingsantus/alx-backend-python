#!/usr/bin/env python3
""" Unit Test that test that the method returns what it is supposed to return"""
import unittest
from parameterized import parameterized

class TestAccessNestedMap(unittest.TestCase):
    """ test case class """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ test if the requred is equal to expected """
        self.assertEqual(access_nested_map(nested_map, path), expected)
