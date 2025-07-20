class Number:
    def __init__(self, value):
        self.value = int(value)

    def __repr__(self):
        return f"Number({self.value})"


class BinOp:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def __repr__(self):
        return f"BinOp({self.left}, '{self.op}', {self.right})"


class VarAssign:
    def __init__(self, name, expr):
        self.name = name
        self.expr = expr

    def __repr__(self):
        return f"VarAssign({self.name} = {self.expr})"


class VarRef:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"VarRef({self.name})"


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else (None, None)

    def eat(self, expected_type):
        if self.current()[0] == expected_type:
            self.pos += 1
            return self.tokens[self.pos - 1][1]
        else:
            raise SyntaxError(f"Expected {expected_type}, got {self.current()[0]}")

    def parse(self):
        if self.current()[0] == "LET":
            self.eat("LET")
            return self.letblock()
        node = self.expr()
        print(f"[Parser] Parsed AST: {node}")
        return node

    def lookahead(self, offset):
        return (
            self.tokens[self.pos + offset]
            if self.pos + offset < len(self.tokens)
            else (None, None)
        )

    def letblock(self):
        if self.current()[0] == "IDENT" and self.lookahead(1)[0] == "EQUAL":
            name = self.eat("IDENT")
            self.eat("EQUAL")
            expr = self.expr()
            return VarAssign(name, expr)
        else:
            raise SyntaxError(
                f"Unexpected token: {self.current()[0]} {self.lookahead(1)[0]}"
            )

    def expr(self):
        node = self.term()
        while self.current()[0] in ("PLUS", "MINUS"):
            op = self.eat(self.current()[0])
            node = BinOp(node, op, self.term())
        return node

    def term(self):
        node = self.factor()
        while self.current()[0] in ("TIMES", "DIVIDE"):
            op = self.eat(self.current()[0])
            node = BinOp(node, op, self.factor())
        return node

    def factor(self):
        token_type, value = self.current()
        if token_type == "NUMBER":
            self.eat("NUMBER")
            return Number(value)
        elif token_type == "IDENT":
            name = self.eat("IDENT")
            return VarRef(name)
        elif token_type == "LPAREN":
            self.eat("LPAREN")
            node = self.expr()
            self.eat("RPAREN")
            return node
        else:
            raise SyntaxError(f"Unexpected token: {token_type}")
