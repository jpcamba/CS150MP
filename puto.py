from parser.lexer import runLexer
from parser.parser import runParser
import sys

def main():
    runParser(sys.argv[1])

if __name__ == "__main__":
    main()
