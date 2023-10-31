#!/usr/bin/python3

"""
This is the "text_indentation" module.
The module supplies one function, text_indentation().
"""
def text_indentation(text):
    """
    function that prints a text with 2 new lines after
    each of these characters: ., ? and :
    """
    if type(text) != str:
        raise TypeError("text must be a string")

    was_new_line = False
    for c in text:
        if was_new_line and c == " ":
            was_new_line = False
            continue
        if c in [".", "?", ":"]:
            print(c, end="")
            print("\n")
            was_new_line = True
        else:
            print(c, end="")
    return
