#!/usr/bin/python3

"""
Desc:
        a function that replaces all occurrences of an element by in a new list
"""


def search_replace(my_list, search, replace):
    new_list = list(map(lambda x: replace if x == search else x, my_list))
    return new_list
