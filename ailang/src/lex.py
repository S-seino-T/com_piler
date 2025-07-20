import re

TOKEN_REGEX = [
    ("NUMBER", r"\d+"),
    ("LET", r"let"),
    ("PLUS", r"\+"),
    ("MINUS", r"-"),
    ("TIMES", r"\*"),
    ("DIVIDE", r"/"),
    ("EQUAL", r"="),
    ("LPAREN", r"\("),
    ("RPAREN", r"\)"),
    ("IDENT", r"[a-zA-Z_][a-zA-Z0-9_]*"),
    ("SPACE", r"\s+"),
]


def tokenize(code):
    tokens = []
    pos = 0
    while pos < len(code):
        for token_type, pattern in TOKEN_REGEX:
            matches = re.match(pattern, code[pos:])
            if matches:
                if token_type != "SPACE":
                    token = (token_type, matches.group())
                    tokens.append((token_type, matches.group()))
                    # print(f"[Lexer] Token: {token}")
                pos += len(matches.group())
                break
        else:
            raise SyntaxError(f"Unexpected character: '{code[pos]}'")
    print(f"[Lexer] All Tokens: {tokens}")
    return tokens
