from typing import Union


class Rectangle:
    def __init__(self, width: Union[int, float],
                 height: Union[int, float]) -> None:

        self.width = width
        self.height = height

    def __repr__(self) -> str:
        return f"{__class__.__name__}" \
               f"(width={self.width}, height={self.height})"

    def set_width(self, width: Union[int, float]) -> None:
        if type(width) in [int, float]:
            self.width = width

    def set_height(self, height: Union[int, float]) -> None:
        if type(height) in [int, float]:
            self.height = height

    def get_area(self) -> Union[int, float]:
        area = self.width * self.height
        return area

    def get_perimeter(self) -> Union[int, float]:
        perimeter = 2 * (self.width + self.height)
        return perimeter

    def get_diagonal(self) -> Union[int, float]:
        diagonal = (self.width ** 2 + self.height ** 2) ** 0.5
        return diagonal

    def get_picture(self, fill: str = "*") -> str:
        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        row = fill * self.width
        lines = [row] * self.height
        return "\n".join(lines)

    def get_amount_inside(self, shape: 'Rectangle') -> Union[int, float]:
        area = self.get_area()
        shape_area = shape.get_area()
        return area // shape_area


class Square(Rectangle):
    def __init__(self, side: Union[int, float]) -> None:
        super().__init__(side, side)

    def __repr__(self) -> str:
        return f"{__class__.__name__}(side={self.width})"

    def set_side(self, side: Union[int, float]) -> None:
        if type(side) in [int, float]:
            self.set_width(side)
            self.set_height(side)
