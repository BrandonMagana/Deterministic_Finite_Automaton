from helpers import create_all_dfas, print_token_type
from File.File import File
from Token_Splitter.Token_Splitter import Token_Splitter
import sys

def lexerAritmetico(archivo):
    dfas = create_all_dfas()
    file = File(archivo)
    lines = file.read_file()
    token_separator = Token_Splitter(lines)
    tokens = token_separator.split()
    print("\n------------------")
    print("| TOKEN --> Tipo |")
    print("------------------\n")
    for token in tokens:
        print_token_type(token,dfas)
    print("\n------------------\n")



if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise "Path of file expected as an argument in command line"
    lexerAritmetico(sys.argv[1])
