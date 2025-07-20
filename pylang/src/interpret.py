from src import parse


class Interpretter:
    def __init__(self):
        self.var_dict = {}

    def evaluate(self, node, var=None):
        if isinstance(node, parse.Int):
            return node.num
        elif isinstance(node, parse.Let):
            self.var_dict[node.varname] = self.evaluate(node.expr1)
            return self.evaluate(node.expr2)
        elif isinstance(node, parse.Var):
            varname = node.varname
            value = self.var_dict.get(varname, None)
            if value != None:
                return value
            else:
                raise Exception(f"Variable is not defined: {varname}")
        elif isinstance(node, parse.Succ):
            return self.evaluate(node.expr, var) + 1
        elif isinstance(node, parse.Pred):
            return self.evaluate(node.expr, var) - 1
        elif isinstance(node, parse.Neg):
            return -self.evaluate(node.expr, var)
        elif isinstance(node, parse.Add):
            return self.evaluate(node.expr, var) + self.evaluate(node.atom, var)
        else:
            raise Exception(f"Unknown Nodes: {node}")
