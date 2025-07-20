from src.lex import Lexer
from src.parse import Parser
from src.interpret import Interpretter


def main():
    lex = Lexer()
    parse = Parser()
    inter = Interpretter()
    tokens = lex.tokenize("succ (pred (succ (-1)))")
    nodes = parse.parse(tokens)
    print(inter.evaluate(nodes, 42))
    tokens = lex.tokenize("3 + 4")
    nodes = parse.parse(tokens)
    print(inter.evaluate(nodes, 42))
    tokens = lex.tokenize("succ 3 + 4")
    nodes = parse.parse(tokens)
    print(inter.evaluate(nodes, 42))
    tokens = lex.tokenize("pred (succ 3 + 4)")
    nodes = parse.parse(tokens)
    print(inter.evaluate(nodes, 42))
    tokens = lex.tokenize("let x := pred (succ 3 + 4) in -x+1")
    nodes = parse.parse(tokens)
    print(inter.evaluate(nodes, 42))
    tokens = lex.tokenize("(2+4) + (4+2)")
    nodes = parse.parse(tokens)
    print(inter.evaluate(nodes, 42))


if __name__ == "__main__":
    main()
