import re

TOKEN_IDENTIFIER = [
    ("NUMBER", r"\d+"),
    ("LET", r"let"),
    ("IN", r"in"),
    ("DEFINE", r"\:\="),
    ("SUCC", r"succ"),
    ("PRED", r"pred"),
    ("MINUS", r"\-"),
    ("PLUS", r"\+"),
    ("LPAREN", r"\("),
    ("RPAREN", r"\)"),
    ("VAR", r"[a-zA-Z_][a-zA-Z0-9_]*"),
    ("SPACE", r"\s+"),
]


class Lexer:
    def __init__(self):
        self.identifier = TOKEN_IDENTIFIER

    def tokenize(self, code):
        ret_tokens = []
        position = 0
        while position < len(code):
            for token_type, pattern in self.identifier:
                matches = re.match(pattern, code[position:])
                if matches:
                    if token_type != "SPACE":
                        token = (token_type, matches.group())
                        ret_tokens.append(token)
                        # print(f"[Lexer] Token: {token}")
                    position += len(matches.group())
                    break
            else:
                raise SyntaxError(f"Unexpected character: '{code[position]}'")
        print(f"[Lexer] All Tokens: {ret_tokens}")
        return ret_tokens
