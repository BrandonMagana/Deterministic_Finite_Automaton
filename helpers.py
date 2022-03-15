from constants import TRANSITION_TABLES, VALID_STATES, OPERATORS
from DFA.dfa import DFA, One_Symbol_DFA

def create_all_dfas():
    dfas = [] 
    dfas.append(DFA("Real", TRANSITION_TABLES["real_numbers"], VALID_STATES["real_numbers"]))
    dfas.append(DFA("Entero", TRANSITION_TABLES["integer_numbers"], VALID_STATES["integer_numbers"]))
    dfas.append(DFA("Variable", TRANSITION_TABLES["variables"], VALID_STATES["variables"]))
    one_symbol_dfas = create_one_symbol_dfas()
    return dfas + one_symbol_dfas

def create_one_symbol_dfas():
    one_symbol_dfas = []
    for token, dfa_type in OPERATORS.items():
        one_symbol_dfas.append(One_Symbol_DFA(dfa_type, token))
    return one_symbol_dfas

def print_token_type(token, dfas):
    for dfa in dfas:
        if dfa.test_token(token):
            print(token, "-->", dfa.dfa_type)
            return
    print(token, "--> ERROR")
            
def is_float(num):
    try:
        float(num)
        return True
    except ValueError:
        return False