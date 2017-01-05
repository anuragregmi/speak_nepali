#!/usr/bin/python
#vim: set fileencoding: utf-8
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
        if char == " ":
            characters.append(char)
            count = 0
        else:
            st += char
            count += 1
        
        if count == 3:
            characters.append(st)
            st = ""
            count = 0

    return characters

def sabdaharu(characters):
    """
    returns list of "shabda" of characters
    """
    letters = ["क", "ख", "ग", "घ", "ड॒", "च", "छ", "ज", "झ", "ञ", "ट", "ठ", "ड", "ढ", "ण", "त", "थ" ,"द", "ध", "न", "प", "फ", "ब", "भ", "म", "य", "र", "ल", "व", "श", "ष", "स", "ह", "अ", "आ", "इ", "ई", "उ", "ऊ", "ए", "ऐ", "ओ" ]
    shabda = []
    st = ""
    for ch in characters:
        if ch == " ":
            shabda.append(ch)
        else:
            if ch in letters:
                shabda.append(st)
                st = ch
            else:
                st += ch
    shabda.append(st)
    shabda.pop(0)
    return  shabda


if __name__ == "__main__":
    s = sabdaharu(part(sys.argv[1]))
    for char in s:
        print "[ "+char+" ]",
