import re

from language_spec import *

def is_part_of_op(char):
    for op in operators:
        if char in op:
            return True
    return False

def is_id(token):
    return re.match(r'^[a-zA-Z]([a-zA-Z]|[0-9]|_){,7}$', token) is not None

def is_const(token):
    return re.match('^(0|[\+\-]?[1-9][0-9]*)$|^\".*\"$', token) is not None

def split_Line(line):
    element = ''
    index = 0

    while index < len(line):
        if line[index] == '"':
            if element:
                yield element
            element = '"'
            index += 1
            while index < len(line) and line[index] != '"':
                element += line[index]
                index += 1
            element += line[index]
            index += 1
            yield element
            element = ''

        elif is_part_of_op(line[index]):
            if element:
                yield element
            element = ''
            while index < len(line) and is_part_of_op(line[index]):
                element += line[index]
                index += 1
            yield element
            element = ''

        elif line[index] in separators:
            if element:
                yield element
            element = line[index]
            index += 1
            yield element
            element = ''

        else:
            element += line[index]
            index += 1

    if element:
        yield element
