from DFA.dfa_helpers import standardize, get_initial_state

class DFA:
    def __init__(self, dfa_type,transition_table, valid_states):
        self.dfa_type= dfa_type
        self.transition_table = transition_table
        self.valid_states = valid_states

    def test_token(self, token):
        standardized_token = standardize(token)
        state  = get_initial_state(self.transition_table)
        for char in standardized_token:
            if self.transition_table[state].get(char): 
                state = self.transition_table[state][char]
            else:
                return False
        return state in self.valid_states


class One_Symbol_DFA:
    def __init__(self, dfa_type, token):
        self.dfa_type = dfa_type
        self.token = token
        

    def test_token(self,token):
        if self.dfa_type == "Comentario":
            return token[:2] == self.token
        return token == self.token