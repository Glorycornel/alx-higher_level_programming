#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    try:
        return float(fct(*args))
    except (IndexError, ValueError, ZeroDivisionError, TypeError) as err:
        print("Exception: {}".format(err.__str__()), file=stderr)
        return None
