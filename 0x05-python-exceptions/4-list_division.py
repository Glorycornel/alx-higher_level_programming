#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    res = []
    for j in range(0, list_length):
        sum_buf = 0
        try:
            sum_buf = my_list_1[j] / my_list_2[j]
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        except ZeroDivisionError:
            print("division by 0")
        finally:
            res.append(sum_buf)
    return res
