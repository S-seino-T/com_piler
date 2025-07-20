from src import parse


class Interpretter:
    def __init__(self):
        pass

    def evaluate(self, node, var=None):
        if isinstance(node, parse.Int):
            return node.num
        elif isinstance(node, parse.Var):
            if var:
                return var
            else:
                raise Exception("We do not have any variables")
        elif isinstance(node, parse.Succ):
            return self.evaluate(node.expr, var) + 1
        elif isinstance(node, parse.Pred):
            return self.evaluate(node.expr, var) - 1
        elif isinstance(node, parse.Neg):
            return -self.evaluate(node.expr, var)
        else:
            raise Exception(f"Unknown Nodes: {node}")
