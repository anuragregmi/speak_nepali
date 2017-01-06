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
            characters.append("space")
        elif char =="?" or char == "," or char == ";" or char == ":":
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

def letters(characters):
    """
    returns list of letters formed by  characters
    """
    letters = ["क", "ख", "ग", "घ", "ड॒", "च", "छ", "ज", "झ", "ञ", "ट", "ठ", "ड", "ढ", "ण", "त", "थ" ,"द", "ध", "न", "प", "फ", "ब", "भ", "म", "य", "र", "ल", "व", "श", "ष", "स", "ह", "अ", "आ", "इ", "ई", "उ", "ऊ", "ए", "ऐ", "ओ" ]
    shabda = []
    st = ""
    for ch in characters:
        if ch == "space":
            shabda.append(st)
            st = ""
            shabda.append(ch)
        else:
            if ch in letters:
                if st != "":
                    shabda.append(st)
                st = ch
            else:
                st += ch

    
    shabda.append(st)
    for ch in shabda:
        if ch == "":
            shabda.remove(ch)
    return  shabda


if __name__ == "__main__":
    s = letters(part(sys.argv[1]))
    for char in s:
        print "[ "+char+" ]",
