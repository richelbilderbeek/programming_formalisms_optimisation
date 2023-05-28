"""Test the functions in src.pfoptimisation_richelbilderbeek.pythonpool."""
import unittest

from src.pfoptimisation_richelbilderbeek.pythonpool import (
    isprime_1,
    isprime_2,
    isprime_3,
    isprime_4,
    isprime_5,
    isprime_6,
    isprime_7,
)


class TestPythonpool(unittest.TestCase):

    """Class to test the functions in 'pythonpool.py'."""

    def test_isprime_all(self):
        """Test the 'is_prime_[x]' functions."""
        for i in range(2, 100):
            a = isprime_1(i)
            b = isprime_2(i)
            c = isprime_3(i)
            d = isprime_4(i)
            e = isprime_5(i)
            f = isprime_6(i)
            g = isprime_7(i)
            self.assertEqual(a, b)
            self.assertEqual(a, c)
            self.assertEqual(a, d)
            self.assertEqual(a, e)
            self.assertEqual(a, f)
            self.assertEqual(a, g)
