from src.parse import Number, BinOp, VarRef, VarAssign


def evaluate(node, env):
    if isinstance(node, Number):
        print(f"[Evaluator] Number: {node.value}")
        return node.value
    elif isinstance(node, BinOp):
        left_value = evaluate(node.left, env)
        right_value = evaluate(node.right, env)
        result = None
        if node.op == "+":
            result = left_value + right_value
        elif node.op == "-":
            result = left_value - right_value
        elif node.op == "*":
            result = left_value * right_value
        elif node.op == "/":
            result = left_value // right_value
        print(f"[Eval] {left_value} {node.op} {right_value} = {result}")
        return result
    elif isinstance(node, VarAssign):
        val = evaluate(node.expr, env)
        env[node.name] = val
        print(f"[Env] Set {node.name} = {val}")
        return val
    elif isinstance(node, VarRef):
        if node.name in env:
            val = env[node.name]
            print(f"[Env] Get {node.name} = {val}")
            return val
        else:
            raise NameError(f"Undefined variable: {node.name}")
    else:
        raise TypeError(f"Unknown node type: {type(node)}")
