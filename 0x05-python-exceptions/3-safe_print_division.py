#!/usr/bin/python3

def safe_print_division(a, b):
    c = None
    print("Inside result: ", end='')
    try:
        c = str(a/b)

    except (ZeroDivisionError,):
        pass

    finally:
        print("{}".format(c))
    return c
