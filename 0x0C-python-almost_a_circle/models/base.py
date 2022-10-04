#!/usr/bin/python3
"""
A model that contains a Base class to manage
the id attribute of all classes that extend
from Base and avoid duplicate the same code.
"""

import csv
from os import path
import json
import turtle


class Base:
    """
    ...
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        ...
        """

        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + '.json'

        with open(filename, mode='w', encoding='utf-8') as f:
            if list_objs is None:
                return f.write(cls.to_json_string(None))

            json_attrs = []

            for elem in list_objs:
                json_attrs.append(elem.to_dictionary())

            return f.write(cls.to_json_string(json_attrs))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == 'Square':
            dummy = cls(3)

        if cls.__name__ == 'Rectangle':
            dummy = cls(3, 3)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + '.json'

        if path.exists(filename) is False:
            return []

        with open(filename, mode='r', encoding='utf-8') as f:
            objs = cls.from_json_string(f.read())
            instances = []

            for elem in objs:
                instances.append(cls.create(**elem))

            return instances

    @classmethod
    def load_from_file_csv(cls):
        class_name = cls.__name__

        result_arr = []
        try:
            with open(f"{class_name}.csv", 'r') as file:
                if class_name == "Rectangle":
                    arr = ["id", "width", "height", "x", "y"]
                elif class_name == "Square":
                    arr = ["id", "size", "x", "y"]
                else:
                    return
                csv_reader = csv.reader(file)
                for row in csv_reader:
                    result_arr.append(cls.create(
                        **({arr[i]: int(row[i]) for i in range(len(row))})))
        except (FileNotFoundError,):
            pass
        return result_arr

    @classmethod
    def save_to_file_csv(cls, list_objs):
        class_name = cls.__name__
        with open(f"{class_name}.csv", 'w') as file:
            if class_name == "Rectangle":
                arr = ["id", "width", "height", "x", "y"]
            elif class_name == "Square":
                arr = ["id", "size", "x", "y"]
            else:
                return
            csv_writer = csv.DictWriter(file, fieldnames=arr)
            for r in list_objs:
                csv_writer.writerow(r.to_dictionary())

    @staticmethod
    def draw(list_rectangles, list_squares):
        if len(list_squares) == 0 and len(list_rectangles) == 0:
            return

        if list_rectangles is not []:
            turtle.color('red', 'yellow')
            for obj in list_rectangles:
                turtle.down()
                turtle.write("Rectangle", align="right")
                turtle.begin_fill()
                turtle.forward(obj.width)
                turtle.left(90)
                turtle.forward(obj.height)
                turtle.left(90)
                turtle.forward(obj.width)
                turtle.left(90)
                turtle.forward(obj.height)
                turtle.left(90)
                turtle.end_fill()
                turtle.up()
                turtle.forward(obj.width+50)

        if list_squares is not []:
            turtle.color('blue', 'green')
            turtle.home()
            turtle.setpos((0, 200))
            turtle.forward(obj.width*2)
            for obj in list_squares:
                turtle.down()
                turtle.write("Square", align="right")
                turtle.begin_fill()
                turtle.forward(obj.width)
                turtle.left(90)
                turtle.forward(obj.height)
                turtle.left(90)
                turtle.forward(obj.width)
                turtle.left(90)
                turtle.forward(obj.height)
                turtle.left(90)
                turtle.end_fill()
                turtle.up()
                turtle.forward(obj.width+50)
        turtle.done()
