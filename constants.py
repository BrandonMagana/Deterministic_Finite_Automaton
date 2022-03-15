ALPHABET  = set("QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm")
NUMBERS = set("123456789")

TRANSITION_TABLES = {
    "real_numbers" : {
        "q0" : {"0" : "q2", "#" : "q1", "." : "q9", "-" : "q6"},
        "q1" : {"0" : "q1", "#" : "q1", "E" : "q5", "e": "q5", "." : "q3"},
        "q2" : {"0" : "q2", "#" : "q1" , "." : "q3" },
        "q3" : {"0" : "q4", "#" : "q4"},
        "q4" : {"0" : "q4", "#" : "q4", "E" : "q5", "e": "q5"},
        "q5" : {"-" : "q7", "+": "q7", "#": "q8"},
        "q6" : {"0" : "q2", "#" : "q1", "." : "q3"},
        "q7" : {"0" : "q7", "#" : "q8"}, 
        "q8" : {"0" : "q8", "#" : "q8"},
        "q9" : {"#" : "q4", "0": "q4"}
    },
    "variables" : {
        "q0": {"L" : "q1"},
        "q1": {"L" : "q1", "#" : "q1", "_" : "q1"}
    },

    "integer_numbers" : {
        "q0" : {"#" : "q1", "0" : "q1" , "-": "q2", "+": "q2"},
        "q1" : {"#" : "q1", "0" : "q1"},
        "q2" : {"#" : "q1"}
    }
}

VALID_STATES = {
    "real_numbers" : ["q3","q4","q8"],
    "variables" : ["q1"],
    "integer_numbers" : ["q1"]
} 

OPERATORS = {
    "//" : "Comentario",
    "+": "Suma",
    "-": "Resta", 
    "*": "Multiplicacion",
    "/": "Division",
    "^": "Potencia", 
    "=": "Asignacion",
    "(": "Parentesis que abre",
    ")": "Parentesis que cierra"
}

