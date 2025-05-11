import unittest

from lasersafety.en207 import continuous_scale_number, pulsed_scale_number


class ModeTest(unittest.TestCase):

    def test_continous_scale_number(self):
        self.assertEqual(continuous_scale_number(10, 1.25e-5, 1064e-9), 5)
        self.assertEqual(continuous_scale_number(0.9, 7.06e-6, 800e-9), 5)
        self.assertEqual(continuous_scale_number(20e-3, 7.06e-6, 1500e-9), 1)

    def test_continous_scale_numbe_checks(self):
        with self.assertRaises(ValueError):
            continuous_scale_number(-1, 1, 1550e-9)

        with self.assertRaises(ValueError):
            continuous_scale_number(1, -1, 1550e-9)

        with self.assertRaises(ValueError):
            continuous_scale_number(1, 1, -1)

        with self.assertRaises(ValueError):
            continuous_scale_number(1, 1, 100e-9)

        with self.assertRaises(ValueError):
            continuous_scale_number(1, 1, 10)

        with self.assertRaises(ValueError):
            continuous_scale_number("a", 1, 1550e-9)

        with self.assertRaises(ValueError):
            continuous_scale_number(1, "a", 1550e-9)

        with self.assertRaises(ValueError):
            continuous_scale_number(1, 1, "a")
