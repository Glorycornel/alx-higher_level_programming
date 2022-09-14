#!/usr/bin/python3
from sys import stderr


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as err:
        print(f"Exception: {err.__str__()}", file=stderr)
        return False
    return True
