from constants import OPERATORS
from helpers import is_float

def line_has_a_comment(line):
    return line.find("//")

def separate_line_by_operators(line):
    new_line = ""
    for i in range(len(line)):
        if line[i] in OPERATORS and line[i] != "-" and line[i] != "+":
            new_line += f" {line[i]} "
        elif line[i] == "-" or line[i] == "+":
            if len(line)> 1 and is_float(line[i+1]):
                new_line += line[i]
            else:
                new_line += f" {line[i]} "
        else:
            new_line += line[i]
    return new_line