from .lexer import tokenize

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
        elif token[0] == "PR":
            self.eat("PR")
            self.eat("LPAREN")
            expr_node = self.expr()
            self.eat("RPAREN")
            return Node("PR", left=expr_node)
        elif token[0] == "IND":
            self.eat("IND")
            self.eat("LPAREN")
            self.eat("RPAREN")
            return Node("IND")
        elif token[0] == "ST":
            self.eat("ST")
            self.eat("LPAREN")
            expr_node = self.expr()
            self.eat("RPAREN")
            return Node("ST", left=expr_node)
        elif token[0] == "SR":
            self.eat("SR")
            self.eat("LPAREN")
            expr_node = self.expr()
            self.eat("RPAREN")
            return Node("SR", left=expr_node)
        elif token[0] == "STRING":
            self.eat("STRING")
            return Node("STRING", token[1][1:-1])
        elif token[0] == "LPAREN":
            self.eat("LPAREN")
            node = self.expr()
            self.eat("RPAREN")
            return node
        elif token[0] == "COLON":
            self.eat("COLON")
            return Node("COLON")
        elif token[0] == "DEV":
            self.eat("DEV")
            self.eat("LPAREN")
            node1 = self.expr()
            self.eat("COMMA")
            node2 = self.expr()
            self.eat("RPAREN")
            return Node("TRY_FUNC", left=node1, right=node2)
        else:
            raise SyntaxError("Ожидался NUMBER, PR, IND, ST, SR, STRING, COLON или скобки")

    def term(self):
        node = self.factor()
        while self.pos < len(self.tokens) and self.tokens[self.pos][0] in ("MUL", "DIV"):
            token = self.tokens[self.pos]
            if token[0] == "MUL":
                self.eat("MUL")
                node = Node("MUL", left=node, right=self.factor())
            elif token[0] == "DIV":
                self.eat("DIV")
                node = Node("DIV", left=node, right=self.factor())
        return node

    def expr(self):
        node = self.term()
        while self.pos < len(self.tokens) and self.tokens[self.pos][0] in ("PLUS", "MINUS"):
            token = self.tokens[self.pos]
            if token[0] == "PLUS":
                self.eat("PLUS")
                node = Node("PLUS", left=node, right=self.term())
            elif token[0] == "MINUS":
                self.eat("MINUS")
                node = Node("MINUS", left=node, right=self.term())
        return node

    def parse(self):
        return self.expr()
