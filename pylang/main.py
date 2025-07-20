from src.lex import Lexer
from src.parse import Parser


def main():
    lex = Lexer()
    parse = Parser()
    tokens = lex.tokenize("succ (succ (succ x))")
    print(parse.parse(tokens))


if __name__ == "__main__":
    main()
