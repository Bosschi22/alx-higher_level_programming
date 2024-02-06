#!/usr/bin/python3
def raise_exception():
    try:
        raise TypeError("Example type error")
    except TypeError:
        print("Caught a type error")
