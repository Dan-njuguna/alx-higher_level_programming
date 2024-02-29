#!/usr/bin/python3
def add_integer(a, b=98):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("a must be an integer")
    if isinstance(a, float) or isinstance(b, float):
        a = int(a)
        b = int(a)
    
    return a + b

if __name__ == "__main__":
    import doctest
    doctest.testfile(r"./tests/0-add_integer.txt")