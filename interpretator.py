def evaluate(node):
	"""Функция для вычисления значения AST"""
	if node.type == "NUMBER":
		return int(node.value) 
	elif node.type == "PLUS":
		return evaluate(node.left) + evaluate(node.right) 
	elif node.type == "MINUS":
		return evaluate(node.left) - evaluate(node.right) 
tokens = tokenz("3 + 5 * (10 - 2)") 
parser = Parser(token) 
ast = parser.parse() 
print(evaluate(ast)) 