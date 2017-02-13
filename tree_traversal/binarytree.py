class Node:
	def __init__(self, value):
		self.left = None
		self.right = None
		self.data = value


class Tree:
	def __init__(self):
		self.root = None

	def addNode(self, node, value):
		if node is None:
			self.root = Node(value)
		else:
			if node.data < value:
				if node.left is None:
					node.left = Node(value)
				else:
					self.addNode(node.left, value)
			else:
				if node.right is None:
					node.right = Node(value)
				else:
					self.addNode(node.right, value)

	def printInorder(self, node):
		if node != None:
			self.printInorder(node.left)
			print node.data
			self.printInorder(node.right)

tree = Tree()
tree.addNode(tree.root, 10)
tree.addNode(tree.root, 5)
tree.addNode(tree.root, 8)
tree.addNode(tree.root, 68)
tree.addNode(tree.root, 70)
tree.printInorder(tree.root)
