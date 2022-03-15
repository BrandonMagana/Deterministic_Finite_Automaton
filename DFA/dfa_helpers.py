from constants import ALPHABET, NUMBERS

def is_float(prefix):
    try:
        float(prefix)
        return True
    except ValueError:
        return False

def scientific_notation_number(token, token_index):
    prefix = token[:token_index]
    return is_float(prefix) and (token[token_index] == "E" or token[token_index] == "e")  and (token[token_index + 1] == "-" or token[token_index + 1] == "+" or token[token_index + 1] in NUMBERS)

def get_initial_state(transitiomn_table):
    initial_state = list(transitiomn_table.keys())[0]
    return initial_state

def standardize(token):
    standardized_token = ""

    for i in range(len(token)):
        if token[i] in ALPHABET and not scientific_notation_number(token, i):
            standardized_token += "L"
        elif token[i] in NUMBERS:
            standardized_token += "#"
        else:
            standardized_token += token[i]

    return standardized_token