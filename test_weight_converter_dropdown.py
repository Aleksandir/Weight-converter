import unittest

from weight_converter_dropdown import convert


class TestConvert(unittest.TestCase):
    def test_kg_to_lb(self):
        conversion_info = ("Kg to Lb", 2.20462)
        self.assertEqual(convert(100, conversion_info), "220.5 Lb")
        self.assertEqual(convert(1, conversion_info), "2.2 Lb")
        self.assertEqual(convert(0, conversion_info), "0 Lb")
        self.assertEqual(convert(0.5, conversion_info), "1.1 Lb")
        self.assertEqual(convert(0.05, conversion_info), "0.1 Lb")
        self.assertEqual(convert(0.005, conversion_info), "0.011 Lb")
        self.assertEqual(convert(0.0005, conversion_info), "0.0011 Lb")
        self.assertEqual(convert(-100, conversion_info), "-220.5 Lb")
        self.assertEqual(convert(-10, conversion_info), "-22.0 Lb")
        self.assertEqual(convert(-1, conversion_info), "-2.2 Lb")
        self.assertEqual(convert(-0.1, conversion_info), "-0.2 Lb")
        self.assertEqual(convert(-0.01, conversion_info), "-0.022 Lb")
        self.assertEqual(convert(-0.001, conversion_info), "-0.0022 Lb")

    def test_lb_to_kg(self):
        conversion_info = ("Lb to Kg", 0.453592)
        self.assertEqual(convert(100, conversion_info), "45.4 Kg")
        self.assertEqual(convert(1, conversion_info), "0.5 Kg")
        self.assertEqual(convert(0, conversion_info), "0 Kg")
        self.assertEqual(convert(0.5, conversion_info), "0.2 Kg")
        self.assertEqual(convert(0.05, conversion_info), "0.0227 Kg")
        self.assertEqual(convert(-100, conversion_info), "-45.4 Kg")
        self.assertEqual(convert(-10, conversion_info), "-4.5 Kg")
        self.assertEqual(convert(-1, conversion_info), "-0.5 Kg")
        self.assertEqual(convert(-0.1, conversion_info), "-0.0454 Kg")

    def test_lb_to_oz(self):
        conversion_info = ("Lb to Oz", 16)
        self.assertEqual(convert(100, conversion_info), "1,600 Oz")
        self.assertEqual(convert(1, conversion_info), "16 Oz")
        self.assertEqual(convert(0, conversion_info), "0 Oz")
        self.assertEqual(convert(0.5, conversion_info), "8 Oz")
        self.assertEqual(convert(0.05, conversion_info), "0.8 Oz")
        self.assertEqual(convert(0.005, conversion_info), "0.08 Oz")
        self.assertEqual(convert(0.0005, conversion_info), "0.008 Oz")
        self.assertEqual(convert(-100, conversion_info), "-1,600 Oz")
        self.assertEqual(convert(-10, conversion_info), "-160 Oz")
        self.assertEqual(convert(-1, conversion_info), "-16 Oz")
        self.assertEqual(convert(-0.1, conversion_info), "-1.6 Oz")
        self.assertEqual(convert(-0.01, conversion_info), "-0.2 Oz")
        self.assertEqual(convert(-0.001, conversion_info), "-0.016 Oz")


if __name__ == "__main__":
    unittest.main()
