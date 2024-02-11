#!/usr/bin/python3
"""Module represent square"""
class square():
    """Square Class"""
    width = 0
    height = 0

    
    def __init__(self, *args, **kwargs):
        """function to initialize a new square instance"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def PermiterOfMySquare(self):
        """function to get perimiter of square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """function that represent string of square"""
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":

    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
