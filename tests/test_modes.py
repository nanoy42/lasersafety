import unittest

from lasersafety.modes import get_test_by_pulse_duration, Mode


class ModeTest(unittest.TestCase):

    def test_get_mode_by_pulse_duration(self):
        self.assertEqual(get_test_by_pulse_duration(3), Mode.D)
        self.assertEqual(get_test_by_pulse_duration(0), Mode.D)
        self.assertEqual(get_test_by_pulse_duration(0.1), Mode.I)
        self.assertEqual(get_test_by_pulse_duration(1e-6), Mode.R)
        self.assertEqual(get_test_by_pulse_duration(1e-12), Mode.M)

    def test_get_mode_by_pulse_duration_checks(self):
        with self.assertRaises(ValueError):
            get_test_by_pulse_duration(None)

        with self.assertRaises(ValueError):
            get_test_by_pulse_duration(-5)

        with self.assertRaises(ValueError):
            get_test_by_pulse_duration("abc")
