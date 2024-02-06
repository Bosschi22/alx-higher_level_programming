#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    num = 0
    try:
        for n in range(x):
            try:
                print("{:d}".format(my_list[n]), end=' ')
                num += 1
            except ValueError:
                pass
    except IndexError:
        pass
    finally:
        print()
    return num
