# 23 链表中环的入口节点
def meeting_node(pHead):
	if pHead == None:
		return None

	slowNode = pHead.next if pHead.next != None else None
	if slowNode == None:
		return
	fastNode = slowNode if slowNode.next != None else None
	# Python and 会返回值，而 C 中&& 只会返回 True or False 
	while fastNode != None && slowNode != None:
		if fastNode == slowNode:
			return fastNode

		slowNode = slowNode.next
		fastNode = fastNode.next
		if fastNode != None:
			fastNode = fastNode.next

	return None


def entry_node_of_loop(pHead):
	# 三件事：
	# 1. 证明有环；
	meetingNode = meeting_node(pHead)
	if meetingNode == None:
		return None

	# 2. 计算环节点数；
	nodesNum = 1
	tmpNode = meetingNode
	while tmpNode.next != meetingNode:
		tmpNode = tmpNode.next
		nodesNum += 1

	# 3. 找到环入口；
	fastNode = pHead
	for i in xrange(1,nodesNum):
		fastNode = fastNode.next

	slowNode = pHead
	while fastNode != slowNode:
		fastNode = fastNode.next
		slowNode = slowNode.next

	return slowNode

# 24. 反转链表
def reverse_list(pHead):
	resHead = None
	curNode = pHead
	preNode = None

	while curNode != None:
		nextNode = curNode.next
		if nextNode == None:
			resHead = curNode

		curNode.next = preNode
		preNode = curNode
		curNode = nextNode

	return resHead


# 25. 合并两个排序的链表
def merge_sorted_list(head1, head2):
	if head1 == None:
		return head2
	else if head2 == None:
		return head1

	mergeHead = None
	if head1.value <= head2.value:
		mergeHead = head1
		mergeHead.next = merge_sorted_list(head1.next, head2)
	else:
		mergeHead = head2
		mergeHead.next = merge_sorted_list(head1, head2.next)

	return mergeHead


# 26. 树的子结构
def has_sub_tree(rootTree, rootSub):
	res = False

	if rootTree != None && rootSub != None:
		res = dose_root_have_sub(rootTree, rootSub)

	if !res:
		res = has_sub_tree(rootTree.leftNode, rootSub)

	if !res:
		res = has_sub_tree(rootTree.rightNode, rootSub)

	return res

def dose_root_have_sub(rootTree, rootSub):
	if rootSub == None:
		return True

	if rootTree == None:
		return False

	if rootTree.value != rootSub.value:
		return False

	return dose_root_have_sub(rootTree.leftNode, rootSub.leftNode) &&
	dose_root_have_sub(rootTree.rightNode, rootSub.rightNode)


# 27. 二叉树的镜像
def mirror_recursively(pNode):
	if pNode == None:
		return

	if pNode.leftNode == None && pNode.rightNode == None:
		return

	tmpNode = pNode.leftNode
	pNode.leftNode = pNode.rightNode
	pNode.rightNode = tmpNode

	if pNode.leftNode != None:
		mirror_recursively(pNode.leftNode)

	if pNode.rightNode != None:
		mirror_recursively(pNode.rightNode)


# 28. 对称的二叉树
def is_symmetrical(pRoot1, pRoot2):
	if pRoot1 == None && pRoot2 == None:
		return True

	if pRoot1 == None || pRoot2 == None:
		return False

	if pRoot1.value != pRoot2.value:
		return False

	return is_symmetrical(pRoot1.leftNode, pRoot2.leftNode) &&
	is_symmetrical(pRoot1.rightNode, pRoot2.rightNode)

def judge_symmetrical(pRoot):
	if pRoot == None:
		return True
	return is_symmetrical(pRoot.leftNode, pRoot.rightNode)

# 29. 顺时针打印矩阵
def print_matrix_clockwisely(nums, rows, columns):
	if nums == None || len(nums) == 0
	|| rows <= 0 || columns <= 0:
	return

	pot = 0

	while rows > pot * 2 && columns > pot * 2:
		print_matrix_in_circle(nums, rows, columns, pot)
		pot += 1

def print_matrix_in_circle(nums, rows, columns, pot):
	endX = columns - 1 - pot
	endY = rows - 1 - pot

	//从左到右打印一行
	for x in xrange(pot,endX):
		print(nums[pot][x])
	//从上到下打印一列
	if pot < endY:
		for x in xrange(pot+1,endY):
			print(nums[x][endX])
	//从右到左打印一行
	if pot < endX && pot < endY:
		for x in xrange(pot,endX-1):
			print(nums[endY][x])
	//从下到上打印一列
	if pot < endX && pot < endY - 1:
		for x in xrange(pot,endY-1):
			print(nums[x][pot])










