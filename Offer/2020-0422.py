# 32-2 分行从上到下打印二叉树
import queue
def print_binary_tree(treeRoot):
	if treeRoot == None:
		return

	qNode = queue.Queue()
	qNode.put(treeRoot)

	nextLevel = 0
	toBePrinted = 1

	while not qNode.empty():
		node = qNode.get()
		print("%d " % node.value)

		if node.leftNode != None:
			qNode.put(node.leftNode)
			nextLevel += 1

		if node.rightNode != None:
			qNode.put(node.rightNode)
			nextLevel += 1

		toBePrinted -= 1

		if toBePrinted == 0:
			print("\n")
			toBePrinted = nextLevel
			nextLevel = 0

# 32-3 之字形打印二叉树
def print_brnary(treeRoot):
	if treeRoot == None:
		return

	levels = [] * 2

	current = 0
	nextLevel = 1

	levels[current].append(treeRoot)

	while len(levels[0]) > 0 || len(levels[1]) > 0:
		node = levels[current][-1]
		levels[current].pop()

		print("%d " % node.value)

		if current == 0:
			if node.leftNode != None:
				levels[nextLevel].append(node.leftNode)
			if node.rightNode != None:
				levels[nextLevel].append(node.rightNode)
		else:
			if node.rightNode != None:
				levels[nextLevel].append(node.rightNode)
			if node.leftNode != None:
				levels[nextLevel].append(node.leftNode)

		if len(levels[current]) == 0:
			print("\n")
			current, nextLevel = nextLevel, current


# 33 二叉搜索树的后序遍历序列
def verify_sequence_of_bst(sequence):
	if sequence == None:
		return False
	n = len(sequence)
	if n <= 0:
		return False

	root = sequence[-1]

	i = 0
	for x in xrange(0,n-1):
		if sequence[x] > root:
			break
		i += 1

	for x in xrange(i+1, n-1):
		if sequence[x] < root:
			return False

	left = True
	if i > 0:
		left = verify_sequence_of_bst(sequence[:i])
	right = True
	if i > 0:
		right = verify_sequence_of_bst(sequence[i+1:])

	return left && right

# 34 二叉树中和为某一值的路径
def find_paths(treeRoot, expectedSum):
	if treeRoot == None:
		return

	path = []
	currentSum = 0
	find_paths_recursive(treeRoot, path, expectedSum, currentSum)

def find_paths_recursive(treeRoot, path, expectedSum, currentSum):
	currentSum += treeRoot.value
	path.append(treeRoot.value)

	isLeaf = treeRoot.leftNode == None && treeRoot.rightNode == None
	if currentSum == expectedSum && isLeaf:
		for p in path:
			print(p)

	if treeRoot.leftNode != None:
		find_paths_recursive(treeRoot.leftNode, path, expectedSum, currentSum)
	if treeRoot.rightNode != None:
		find_paths_recursive(treeRoot.rightNode, path, expectedSum, currentSum)

	path.pop()








