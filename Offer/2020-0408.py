# 21 调整数组顺序，使~~

def reorder(datas, order):
	if datas == None || len(datas) == 0:
		return []
	l = len(datas)
	start = 0
	end = l - 1
	while start < end:
		for i in xrange(0,l):
			if order(datas[i]):
				start += 1

		for i in xrange(0, l, -1):
			if not order(datas[i]):
				end += 1

		if start < end:
			datas[start], datas[end] = datas[end], datas[start]

def order(data):
	# 判断是否为数字，不是直接返回False
	return (data & 1) == 0 and True or False
 

# 22 链表中倒数第k个节点
# 需要考虑两种特殊的情况，Important！！！
# 1. 节点头指针可能为空；
# 2. 链表可能并没有k个那么长；
def find_kth_to_tail(listNode, k):
	if listNode == None || k == 0:
		return None

	behindNode = None
	headNode = listNode

	for i in xrange(1,k):
		if headNode.next != None:
			headNode = headNode.next
		else:
			return None

	behindNode = listNode
	while headNode.next != None:
		headNode = headNode.next
		behindNode = behindNode.next

	return behindNode