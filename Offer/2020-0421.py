# 30 包含min函数的栈
class StackWithMin(object):
	"""docstring for StackWithMin"""
	mData = [] # 数据栈
	mMinTmp = [] # 辅助栈

	def __init__(self, arg):
		super(StackWithMin, self).__init__()
		self.arg = arg

	def push(self, value):
		self.mData.append(value)

		if len(mMinTmp) == 0 || value < self.mMinTmp[0]:
			self.mMinTmp.append(value)
		else:
			self.mMinTmp.append(self.mMinTmp[-1])

	def pop(self):
		assert(len(self.mData) > 0 && len(self.mMinTmp) > 0)

		self.mData.pop()
		self.mMinTmp.pop()

	def min(self):
		assert(len(self.mData) > 0 && len(self.mMinTmp) > 0)

		return self.mMinTmp[-1]


# 31 栈的压入弹出序列
def is_pop_order(pushList, popList):
	isPossible = False

	if pushList == None:
		return False
	if popList == None:
		return False

	n = len(pushList)

	if n == 0:
		return False

	nextPushIndex = 0 # 当前入栈序列索引
	nextPopIndex = 0 # 当前出栈序列索引

	dataStack = []
	while nextPopIndex < n:
		while len(dataStack) == 0 || dataStack[-1] != popList[nextPopIndex]:
			if nextPushIndex == n:
				break
			dataStack.append(pushList[nextPushIndex])
			nextPushIndex += 1
		if dataStack[-1] == popList[nextPopIndex]:
			break
		dataStack.pop()
		nextPopIndex += 1

	if len(dataStack) == 0  && nextPopIndex == n:
		isPossible = True

	return isPossible		
	 	
# 32 从上到下打印二叉树(层次遍历)
import queue
def print_from_top_to_bottom(treeRoot):
	if treeRoot == None:
		return

	qNode = queue.Queue()
	qNode.put(treeRoot) # 入队

	while not qNode.empty():
		node = qNode.get() # 出队

		print(node.value)

		if node.leftNode != None:
			qNode.put(node.leftNode)
		if node.rightNode != None:
			qNode.put(node.rightNode)


# 32-2 分行从上到下打印二叉树






