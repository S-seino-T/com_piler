from src.parse import Parser, Number, BinOp
from src.interpret import evaluate
from src.lex import tokenize


def main():
    env = {}

    while True:
        try:
            code = input("> ")
            tokens = tokenize(code)
            parser = Parser(tokens)
            ast = parser.parse()
            result = evaluate(ast, env)
            print(f"Result: {result}")
        except (SyntaxError, TypeError) as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
