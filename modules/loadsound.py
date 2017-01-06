#!/usr/bin/python
import os

def listfiles(dirs):
    
    for root,dirs,files in os.walk(dirs):
        pass
    return files

if __name__ == "__main__":
    x = listfiles("../sounds/")
    for f in x:
        print f;
