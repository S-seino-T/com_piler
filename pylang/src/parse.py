class Int:
    def __init__(self, num):
        self.num = int(num)

    def __repr__(self):
        return f"(Int {self.num})"


class Var:
    def __init__(self):
        pass

    def __repr__(self):
        return f"(Var x)"


class Succ:
    def __init__(self, expr):
        self.expr = expr

    def __repr__(self):
        return f"(Succ {self.expr})"


class Pred:
    def __init__(self, expr):
        self.expr = expr

    def __repr__(self):
        return f"(Pred {self.expr})"


class Neg:
    def __init__(self, expr):
        self.expr = expr

    def __repr__(self):
        return f"(Neg {self.expr})"


class Parser:
    def __init__(self):
        self.bpos = 0
        self.epos = 0

    def parse(self, tokens):
        self.epos = len(tokens) - 1
        ret = self.expr(tokens)
        print(ret)
        return ret

    def expr(self, tokens):
        token_type, token_value = tokens[0]
        if token_type == "SUCC":
            return Succ(self.factor(tokens[1:]))
        elif token_type == "PRED":
            return Pred(self.factor(tokens[1:]))
        elif token_type == "NEG":
            return Neg(self.factor(tokens[1:]))
        else:
            return self.factor(tokens)

    def factor(self, tokens):
        first_token_type, first_token_value = tokens[0]
        last_token_type, last_token_value = tokens[-1]
        if first_token_type == "LPAREN":
            if last_token_type == "RPAREN":
                return self.expr(tokens[1:-1])
            else:
                raise SyntaxError(f"Unexpected token: {tokens[0]}")
        elif first_token_type == "VAR":
            return Var()
        elif first_token_type == "NUMBER":
            return Int(first_token_value)
        else:
            raise SyntaxError(f"Unexpected token: {tokens[0]}")
