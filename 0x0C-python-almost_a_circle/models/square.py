#!/usr/bin/python3
"""Square Module"""
try:
    Rectangle = __import__("rectangle").Rectangle
except ModuleNotFoundError:
    from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class inherits from Rectangle
    Args:
        Rectangle (class): base for the square
    """

    def __init__(self, size, x=0, y=0, id=None):
        """initializes the class instance
        Args:
            size (int): size of the square
            x (int, optional): the number of spaces. Defaults to 0.
            y (int, optional): the number of newline. Defaults to 0.
            id (int, optional): unique id for the square. Defaults to None.
        """
        super().__init__(size, size, x, y, id)
        self.__size = self.check_integer_parameter(size, "size")

    def __str__(self):
        """handles the print of this class
        Returns:
            str: custom print string
        """
        return "[Square] (:d) {:d}/{:d} - {:d}".format(
                self.id, self.x, self.y, self.size
            )

    @property
    def size(self):
        """getter for size
        Returns:
            int: returns the value of size
        """
        return self.__size

    @size.setter
    def size(self, value: int):
        """setter for the size
        Args:
            value (int): the value to be set
        """
        super().update(height=value, width=value)
        self.__size = self.check_integer_parameter(value, "size")

    def update(self, *args, **kwargs):
        """updates the value of the instance
        """
        arr = ["id", "size", "x", "y"]
        if len(args) > len(arr):
            return
        for i in range(len(args)):
            setattr(self, arr[i], args[i])

        for key, value in kwargs.items():
            if key in arr:
                setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a square
        Returns:
            dict: dictionary containing the square details
        """
        arr = ["id", "size", "x", "y"]
        return {arr[i]: getattr(self, arr[i]) for i in range(len(arr))}
