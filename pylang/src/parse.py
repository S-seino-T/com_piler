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


class Add:
    def __init__(self, expr, atom):
        self.expr = expr
        self.atom = atom

    def __repr__(self):
        return f"(Add {self.expr} {self.atom})"


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
        return self.binary(tokens)

    def binary(self, tokens):
        # Addの解析: expr + factor の形式
        p_counter = 0
        for i in range(len(tokens)):
            token_type, token_value = tokens[i]
            if token_type == "LPAREN":
                p_counter += 1
            elif token_type == "RPAREN":
                p_counter -= 1
            elif token_type == "PLUS" and p_counter == 0:
                left_expr = self.expr(tokens[:i])
                right_factor = self.atom(tokens[i + 1 :])
                return Add(left_expr, right_factor)
        return self.unary(tokens)

    def unary(self, tokens):
        # 単項演算子の解析
        token_type, token_value = tokens[0]
        if token_type == "SUCC":
            return Succ(self.factor(tokens[1:]))
        elif token_type == "PRED":
            return Pred(self.factor(tokens[1:]))
        elif token_type == "MINUS":
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
        else:
            return self.atom(tokens)

    def atom(self, tokens):
        token_type, token_value = tokens[0]
        if token_type == "VAR":
            return Var()
        elif token_type == "NUMBER":
            return Int(token_value)
        else:
            raise SyntaxError(f"Unexpected token: {tokens[0]}")
