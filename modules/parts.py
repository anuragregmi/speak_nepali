#!/usr/bin/python
import sys

def part(string):
    """
    breaks nepali string into  characters and returns the list of characters
    note:one nepali character is  made of three ascii characters
    """
    characters = [] 
    count = 0
    st = ""
    for char in string:
        st += char
        count += 1
        if count == 3:
            characters.append(st)
            st = ""
            count = 0

    return characters


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print  part(sys.argv[1])
