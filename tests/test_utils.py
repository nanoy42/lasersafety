import unittest

from lasersafety.utils import (
    validate_wavelength_en207,
    validate_wavelength_en208,
    validate_strictly_positive_number,
    format_value,
)


class UtilsTest(unittest.TestCase):
    def test_validate_wavelength(self):
        with self.assertRaises(ValueError):
            validate_wavelength_en207("a")

        with self.assertRaises(ValueError):
            validate_wavelength_en207(None)

        with self.assertRaises(ValueError):
            validate_wavelength_en207(100e-9)

        with self.assertRaises(ValueError):
            validate_wavelength_en207(1)

        validate_wavelength_en207(400e-9)

    def test_validate_wavelength_en208(self):
        with self.assertRaises(ValueError):
            validate_wavelength_en208("a")

        with self.assertRaises(ValueError):
            validate_wavelength_en208(None)

        with self.assertRaises(ValueError):
            validate_wavelength_en208(100e-9)

        with self.assertRaises(ValueError):
            validate_wavelength_en208(900e-9)

        with self.assertRaises(ValueError):
            validate_wavelength_en208(1)

        validate_wavelength_en208(400e-9)

    def test_validate_strictly_positive_number(self):
        with self.assertRaises(ValueError):
            validate_strictly_positive_number("a")

        with self.assertRaises(ValueError):
            validate_strictly_positive_number(None)

        with self.assertRaises(ValueError):
            validate_strictly_positive_number(0)

        with self.assertRaises(ValueError):
            validate_strictly_positive_number(-1)

        validate_strictly_positive_number(10)

    def test_format_value(self):
        self.assertEqual(format_value(1e0), "1.0 ")
        self.assertEqual(format_value(1e1), "10.0 ")
        self.assertEqual(format_value(1e2), "100.0 ")
        self.assertEqual(format_value(1e3), "1.0 k")
        self.assertEqual(format_value(1e4), "10.0 k")
        self.assertEqual(format_value(1e5), "100.0 k")
        self.assertEqual(format_value(1e6), "1.0 M")
        self.assertEqual(format_value(1e7), "10.0 M")
        self.assertEqual(format_value(1e8), "100.0 M")
        self.assertEqual(format_value(1e9), "1.0 G")

        self.assertEqual(format_value(1e-1), "100.0 m")
        self.assertEqual(format_value(1e-2), "10.0 m")
        self.assertEqual(format_value(1e-3), "1.0 m")
        self.assertEqual(format_value(1e-4), "100.0 μ")
        self.assertEqual(format_value(1e-5), "10.0 μ")
        self.assertEqual(format_value(1e-6), "1.0 μ")
        self.assertEqual(format_value(1e-7), "100.0 n")
        self.assertEqual(format_value(1e-8), "10.0 n")
        self.assertEqual(format_value(1e-9), "1.0 n")
        self.assertEqual(format_value(1e-10), "100.0 p")
        self.assertEqual(format_value(1e-11), "10.0 p")
        self.assertEqual(format_value(1e-12), "1.0 p")
        self.assertEqual(format_value(1e-13), "100.0 f")
        self.assertEqual(format_value(1e-14), "10.0 f")
        self.assertEqual(format_value(1e-15), "1.0 f")

        self.assertEqual(format_value(1e-16), "1e-16")

        self.assertEqual(format_value(-1e0), "-1.0 ")
        self.assertEqual(format_value(-1e-13), "-100.0 f")

        self.assertEqual(format_value(0), "0")

        with self.assertRaises(ValueError):
            format_value(None)

        with self.assertRaises(ValueError):
            format_value("a")
