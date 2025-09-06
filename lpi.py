import re

# Лексер: определим токены и функцию токенизации
token_specs = [
    ("NUMBER", r"\d+"),
    ("PLUS", r"\+"),
    ("MINUS", r"-"),
    ("WHITESPACE", r"\s+"),
]

def tokenize(code):
    tokens = []
    while code:
        for name, pattern in token_specs:
            match = re.match(pattern, code)
            if match:
                value = match.group(0)
                if name != "WHITESPACE":
                    tokens.append((name, value))
                code = code[len(value):]
                break
        else:
            raise SyntaxError(f"Неизвестный символ: {code[0]}")
    return tokens

# Парсер: строим AST 
class Node:
    def __init__(self, type, value=None, left=None, right=None):
        self.type = type
        self.value = value
        self.left = left
        self.right = right

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def eat(self, token_type):
        if self.pos < len(self.tokens) and self.tokens[self.pos][0] == token_type:
            self.pos += 1
        else:
            raise SyntaxError(f"Ожидалось {token_type}")

    def factor(self):
        token = self.tokens[self.pos]
        if token[0] == "NUMBER":
            self.eat("NUMBER")
            return Node("NUMBER", int(token[1]))
        else:
            raise SyntaxError("Ожидалось число")

    def expr(self):
        node = self.factor()
        while self.pos < len(self.tokens) and self.tokens[self.pos][0] in ("PLUS", "MINUS"):
            token = self.tokens[self.pos]
            if token[0] == "PLUS":
                self.eat("PLUS")
                node = Node("PLUS", left=node, right=self.factor())
            elif token[0] == "MINUS":
                self.eat("MINUS")
                node = Node("MINUS", left=node, right=self.factor())
        return node

    def parse(self):
        return self.expr()

# Интерпретатор: вычисляем значение AST
def evaluate(node):
    if node.type == "NUMBER":
        return node.value
    elif node.type == "PLUS":
        return evaluate(node.left) + evaluate(node.right)
    elif node.type == "MINUS":
        return evaluate(node.left) - evaluate(node.right)
    
def run_code(code):
    tokens = tokenize(code)
    parser = Parser(tokens)
    ast = parser.parse()
    return evaluate(ast)

# Пример 
if __name__ == "__main__":
    code = "3 + 5 - 2"
    result = run_code(code)
    print(result)  # Вывод: 6

