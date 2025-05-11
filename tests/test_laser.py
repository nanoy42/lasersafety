import unittest

from lasersafety.laser import LaserBeam
from lasersafety.modes import Mode


class LaserTest(unittest.TestCase):
    def test_example_1(self):
        laser = LaserBeam(
            wavelength=1064e-9, average_power=10, beam_diameter=4e-3, repetition_rate=0
        )

        self.assertEqual(laser.en207_analysis(), [(Mode.D, 5)])

    def test_example_2(self):
        laser = LaserBeam(
            wavelength=532e-9, average_power=5, beam_diameter=2e-3, repetition_rate=0
        )

        self.assertEqual(laser.en208_analysis(), 4)

    def test_example_3(self):
        laser = LaserBeam(
            wavelength=800e-9,
            pulse_energy=4.5e-6,
            repetition_rate=200e3,
            pulse_duration=200e-15,
            beam_diameter=3e-3,
        )

        self.assertEqual(laser.en207_analysis(), [(Mode.D, 5), (Mode.M, 6)])

    def test_example_4(self):
        laser = LaserBeam(
            wavelength=1500e-9,
            average_power=20e-3,
            repetition_rate=200e3,
            pulse_duration=200e-15,
            beam_diameter=3e-3,
        )

        self.assertEqual(laser.en207_analysis(), [(Mode.D, 1), (Mode.M, 1)])
