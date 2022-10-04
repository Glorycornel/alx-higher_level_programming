#!/usr/bin/python3
"""Rectangle Module"""
try:
    Base = __import__('base').Base
except ModuleNotFoundError:
    from models.base import Base


class Rectangle(Base):
    """Rectangle inherits from Base
    Args:
        Base (class): base for the rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes the class instance
        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
            x (int, optional): the number of spaces. Defaults to 0.
            y (int, optional): the number of newline. Defaults to 0.
            id (int, optional): unique id for the rectangle. Defaults to None.
        """
        super().__init__(id)
        self.__width = self.check_integer_parameter(width, "width")
        self.__height = self.check_integer_parameter(height, "height")
        self.__x = self.check_integer_parameter(x, "x")
        self.__y = self.check_integer_parameter(y, "y")

    def __str__(self):
        """handles the print of this class
        Returns:
            str: custom print string
        """
        return '[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}'.format(
            self.id, self.x, self.y, self.width, self.height
        )

    @property
    def width(self):
        """getter for width
        Returns:
            int: returns value of width
        """
        return self.__width

    @property
    def height(self):
        """getter for height
        Returns:
            int: returns the value of height
        """
        return self.__height

    @property
    def x(self):
        """getter for x
        Returns:
            int: returns the value of x
        """
        return self.__x

    @property
    def y(self):
        """getter for y
        Returns:
            int: returns the value of y
        """
        return self.__y

    @width.setter
    def width(self, value: int):
        """sets the width
        Args:
            value (int): the width
        """
        self.__width = self.check_integer_parameter(value, "width")

    @height.setter
    def height(self, value: int):
        """sets the height
        Args:
            value (int): the height
        """
        self.__height = self.check_integer_parameter(value, "height")

    @x.setter
    def x(self, value: int):
        """sets the value of x
        Args:
            value (int): the x
        """
        self.__x = self.check_integer_parameter(value, 'x')

    @y.setter
    def y(self, value: int):
        """sets the value of y
        Args:
            value (int): the value of the y to be set
        """
        self.__y = self.check_integer_parameter(value, 'y')

    def check_integer_parameter(self, value, param):
        """checks the type and value of the parameter
        Args:
            value (int): the value to be set
            param (str): the string that the value
        Raises:
            TypeError: _description_
            ValueError: _description_
            ValueError: _description_
        """
        if type(value) is not int:
            raise TypeError(param + ' must be an integer')

        if value <= 0 and param in ('width', 'height', 'size'):
            raise ValueError(param + ' must be > 0')

        if value < 0 and param in ('x', 'y'):
            raise ValueError(param + ' must be >= 0')
        return value

    def area(self):
        """computes the area of the rectangle
        Returns:
            int: the area
        """
        return self.height * self.width

    def display(self):
        """draws something to illustrate the rectangle
        """
        print("\n"*self.y, end='')
        for i in range(self.height):
            print(" "*self.x + '#' * self.width)

    def update(self, *args, **kwargs):
        """updates the values of the instance
        """
        arr = ["id", "width", "height", "x", "y"]
        if len(args) > len(arr):
            return
        if args is not None and args != ():
            for i in range(len(args)):
                setattr(self, arr[i], args[i])
        elif (args is None or args == ()) and kwargs is not None:
            for key, value in kwargs.items():
                if key in arr:
                    setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a rectangle
        Returns:
            dict: dictionary containing the rectangle details
        """
        arr = ["id", "width", "height", "x", "y"]
        return {arr[i]: getattr(self, arr[i]) for i in range(len(arr))}
