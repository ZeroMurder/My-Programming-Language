from .parser import Parser
from .lexer import tokenize

functions = {}

def evaluate(node):
    if node.type == "NUMBER":
        return node.value
    elif node.type == "PLUS":
        return evaluate(node.left) + evaluate(node.right)
    elif node.type == "MINUS":
        return evaluate(node.left) - evaluate(node.right)
    elif node.type == "MUL":
        return evaluate(node.left) * evaluate(node.right)
    elif node.type == "DIV":
        return evaluate(node.left) / evaluate(node.right)
    elif node.type == "PR":
        value = evaluate(node.left)
        print(value)
    elif node.type == "IND":
        return input()
    elif node.type == "ST":
        style = evaluate(node.left)
        print(f"Подключён стиль: {style}")
    elif node.type == "SR":
        value = evaluate(node.left)
        return str(value)
    elif node.type == "STRING":
        return node.value
    elif node.type == "COLON":
        return ":"
    elif node.type == "FUNC_DEF":
        functions[node.value] = node.left
    elif node.type == "FUNC_CALL":
        if node.value in functions:
            return evaluate(functions[node.value])
        else:
            raise Exception(f"Функция {node.value} не найдена")
    elif node.type == "TRY_FUNC":
        try:
            return evaluate(node.left)
        except Exception:
            return evaluate(node.right)
    else:
        raise Exception(f"Неизвестный тип узла: {node.type}")

def run_code(code):
    tokens = tokenize(code)
    parser = Parser(tokens)
    ast = parser.parse()
    return evaluate(ast)

