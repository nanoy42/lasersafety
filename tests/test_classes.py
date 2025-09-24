import unittest

from lasersafety.classes import LaserClass


class ClassesTest(unittest.TestCase):
    def test_classes(self):
        self.assertTrue(LaserClass.ONE == 1)
        self.assertTrue(LaserClass.ONE_M == 1)
        self.assertTrue(LaserClass.ONE_C == 1)
        self.assertTrue(LaserClass.TWO == 2)
        self.assertTrue(LaserClass.TWO_M == 2)
        self.assertTrue(LaserClass.THREE_R == 3)
        self.assertTrue(LaserClass.THREE_B == 3)
        self.assertTrue(LaserClass.FOUR == 4)

        self.assertTrue(LaserClass.TWO == LaserClass.TWO)

        self.assertFalse(LaserClass.TWO == LaserClass.TWO_M)

        self.assertTrue(LaserClass.TWO < 4)

        self.assertTrue(LaserClass.ONE < LaserClass.ONE_M)
        self.assertTrue(LaserClass.ONE_M < LaserClass.ONE_C)
        self.assertTrue(LaserClass.ONE_C < LaserClass.TWO)
        self.assertTrue(LaserClass.TWO < LaserClass.TWO_M)
        self.assertTrue(LaserClass.TWO_M < LaserClass.THREE_B)
        self.assertTrue(LaserClass.THREE_R < LaserClass.THREE_B)
        self.assertTrue(LaserClass.THREE_B < LaserClass.FOUR)

        with self.assertRaises(TypeError):
            LaserClass.ONE < ""

        self.assertFalse(LaserClass.ONE == "")

        self.assertEqual(str(LaserClass.ONE), "1")
        self.assertEqual(str(LaserClass.ONE_M), "1M")
        self.assertEqual(str(LaserClass.ONE_C), "1C")
        self.assertEqual(str(LaserClass.TWO), "2")
        self.assertEqual(str(LaserClass.TWO_M), "2M")
        self.assertEqual(str(LaserClass.THREE_R), "3R")
        self.assertEqual(str(LaserClass.THREE_B), "3B")
        self.assertEqual(str(LaserClass.FOUR), "4")
