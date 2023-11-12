#!/usr/bin/python3
"""TestBase class for test"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """TestBase class"""

    def tets(self):
        a = Base()
        self.assertEqual(a.id, 1)

        a1 = Base()
        self.assertEqual(a1.id, 2)

        a2 = Base(12)
        self.assertEqual(a2.id, 12)
