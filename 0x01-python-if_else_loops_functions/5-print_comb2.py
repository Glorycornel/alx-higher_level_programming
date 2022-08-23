#!/usr/bin/python3
for n in range(00, 100):
    if n == 99:
        print("{0:d}".format(n))
    else:
        print("{0:02}".format(n), end=', ')
