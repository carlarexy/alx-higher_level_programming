#!/usr/bin/python3

def uppercase(str):
    """Print a string in uppercase."""
    for b in str:
        if ord(b) >= 97 and ord(b) <= 122:
            b = chr(ord(b) - 32)
        print("{}".format(b), end="")
    print("")
