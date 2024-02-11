#!/usr/bin/python3
"""Module represent square"""


class Square():
    """Square Class

    Attributes:
        side (int): width of square
    """
    side = 0

    def __init__(self, *args, **kwargs):
        """function to initialize a new square

        Parameters:
        args (any): arguments
        kwargs (any): keyword args
        """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.side * 2

    def permiter_of_my_square(self):
        """function to get perimiter of square """
        return (self.side * 2) + (self.side * 2)

    def __str__(self):
        """function that represent string of square"""
        return "{}/{}".format(self.side, self.side)


if __name__ == "__main__":

    s = Square(side=12)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
