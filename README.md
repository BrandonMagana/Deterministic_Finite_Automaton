Deterministic Finite Automaton 
=======
This program implements a Deterministic Finite Automaton (DFA) in order to figure out the type of each of the tokens on a .txt file.

## Requirements
* Python version 3.7.0 or higher

## How to Use
* Run `main.py` file with python and give a path to a file as an argument in order to analize it
```
  python main.py -path-to-file-
```
## Input Example (.txt File)
```
    b = 7

    a = 32.4 *(-8.6 - b)/       6.1E-8

    d = a ^ b

    // c=35*19 ^ 3.     Esto es un comentario

    _a25 // error
    
```

## Output Example
```
    ------------------
    | TOKEN --> Tipo |
    ------------------

    b --> Variable
    = --> Asignacion
    7 --> Entero
    a --> Variable
    = --> Asignacion
    32.4 --> Real
    * --> Multiplicacion
    ( --> Parentesis que abre
    -8.6 --> Real
    - --> Resta
    b --> Variable
    ) --> Parentesis que cierra
    / --> Division
    6.1E-8 --> Real
    d --> Variable
    = --> Asignacion
    a --> Variable
    ^ --> Potencia
    b --> Variable
    // c=35*19 ^ 3.     Esto es un comentario --> Comentario
    _a25 --> ERROR
    // error --> Comentario

    ------------------
```

## Credits
- Author: Brandon Josué Magaña Mendoza | A01640162

