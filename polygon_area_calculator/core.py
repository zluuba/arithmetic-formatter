class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __repr__(self):
        return f"{__class__.__name__}(width={self.width}, height={self.height})"

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        area = self.width * self.height
        return area

    def get_perimeter(self):
        perimeter = 2 * (self.width + self.height)
        return perimeter

    def get_diagonal(self):
        diagonal = (self.width ** 2 + self.height ** 2) ** 0.5
        return diagonal

    def get_picture(self, fill="*"):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        row = fill * self.width
        lines = [row] * self.height
        return "\n".join(lines)

    def get_amount_inside(self, shape):
        area = self.get_area()
        shape_area = shape.get_area()
        return area // shape_area


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __repr__(self):
        return f"{__class__.__name__}(side={self.width})"

    def set_side(self, side):
        self.set_width(side)
        self.set_height(side)
