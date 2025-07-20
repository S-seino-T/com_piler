from src.lex import Lexer
from src.parse import Parser
from src.interpret import Interpretter


def main():
    lex = Lexer()
    parse = Parser()
    inter = Interpretter()
    tokens = lex.tokenize("succ (pred (succ (-x)))")
    nodes = parse.parse(tokens)
    print(inter.evaluate(nodes, 42))


if __name__ == "__main__":
    main()
