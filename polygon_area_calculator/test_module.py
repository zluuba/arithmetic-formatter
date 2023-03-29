from polygon_area_calculator.core import Rectangle, Square

RECTANGLE_PIC = """**********
**********
**********"""

SQUARE_PIC = """****
****
****
****"""


def test_rectangle_and_square():
    rect = Rectangle(10, 5)
    assert rect.get_area() == 50

    rect.set_height(3)
    assert rect.get_perimeter() == 26
    assert f"{rect}" == "Rectangle(width=10, height=3)"
    assert rect.get_picture() == RECTANGLE_PIC

    sq = Square(9)
    assert sq.get_area() == 81
    sq.set_side(4)
    assert sq.get_diagonal() == 5.656854249492381
    assert f"{sq}" == "Square(side=4)"
    assert sq.get_picture() == SQUARE_PIC

    rect.set_height(8)
    rect.set_width(16)
    assert rect.get_amount_inside(sq) == 8
