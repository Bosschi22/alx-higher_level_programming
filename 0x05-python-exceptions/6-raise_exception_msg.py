#!/usr/bin/python3
def raise_exception_msg(message=""):
    try:
        raise NameError(message)
    except NameError:
        print("Caught a name error with message:", message)
