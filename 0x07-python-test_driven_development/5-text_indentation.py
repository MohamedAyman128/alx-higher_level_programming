#!/usr/bin/python3
"""text_indentation
"""

def text_indentation(text):
    """text_indentation
    arg:
        text: text
    """
    if not isinstance(text, str):
            raise TypeError("text must be a string")
    new = ""
    for i in text:
        if (i == '.' or i == '?' or i == ':') :
            new += i
            new += '\n'*2
        else:
            new += i
    mylist = new.splitlines()
    for word in mylist:
        print(word.strip())
