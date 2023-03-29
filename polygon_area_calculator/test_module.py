from polygon_area_calculator.core import Rectangle, Square
import unittest

RECTANGLE_PIC = """**********
**********
**********"""

SQUARE_PIC = """****
****
****
****"""


class UnitTests(unittest.TestCase):
    def test_rectangle_class(self):
        rect = Rectangle(10, 5)
        result = rect.get_area()
        expected = 50
        self.assertEqual(result, expected)

        rect.set_height(3)
        result = rect.get_perimeter()
        expected = 26
        self.assertEqual(result, expected)

        result = str(rect)
        expected = "Rectangle(width=10, height=3)"
        self.assertEqual(result, expected)

        result = rect.get_picture()
        expected = RECTANGLE_PIC
        self.assertEqual(result, expected)

    def test_square_class(self):
        sq = Square(9)
        result = sq.get_area()
        expected = 81
        self.assertEqual(result, expected)

        sq.set_side(4)
        result = sq.get_diagonal()
        expected = 5.656854249492381
        self.assertEqual(result, expected)

        result = str(sq)
        expected = "Square(side=4)"
        self.assertEqual(result, expected)

        result = sq.get_picture()
        expected = SQUARE_PIC
        self.assertEqual(result, expected)

    def test_rectangle_and_square_classes(self):
        rect = Rectangle(8, 16)
        sq = Square(4)

        result = rect.get_amount_inside(sq)
        expected = 8
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
