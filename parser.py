class Node:
    def __init__(self, type, value=None, right=None, left=None):
        self.type = type
        self.value = value
        self.right = right
        self.left = left

class Parser:
    def __init__(self, tok):
        self.tok = tok
        self.pos = 0

    def fet(self, tok_type):
        if self.pos < len(self.tok) and self.tok[self.pos][0] == tok_type:
            self.pos += 1
        else:
            raise SyntaxError(f"Ожидалось {tok_type}, но получено {self.tok[self.pos][0]}")

    def expr(self):
        """Обрабатывает сложение и вычитание"""
        node = self.term()
        while self.pos < len(self.tok) and self.tok[self.pos][0] in ("PLUS", "MINUS"):
            token = self.tok[self.pos]
            self.pos += 1
            node = Node(token[0], left=node, right=self.term())
        return node

    def parse(self):
        """Запускает процесс разбора и возвращает AST"""
        return self.expr()

        
