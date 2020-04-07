# 18-1 在O(1)时间内删除链表节点
def delete_node(listHead, toBeDeleted):
	# python nil is None
	if not listHead or not toBeDeleted:
		return

	if toBeDeleted.pNext != None: # 要删除的不是最后一个
		pNext = toBeDeleted.pNext
		toBeDeleted.nValue = pNext.nValue
		toBeDeleted.pNext = pNext.pNext
		pNext = None
	else if listHead == toBeDeleted: # 是最后一个节点，但只有一个
		toBeDeleted = None
		listHead = None
	else: # 是最后一个节点，需要找到前一个节点
		pNode = listHead
		while pNode.pNext != toBeDeleted:
			pNode = pNode.pNext

		pNode.pNext = None
		toBeDeleted = None

# 18-2 删除表中重复节点
def delete_duplication(listNode):
	if listNode == None:
		return

	preNode = None
	pNode = listNode

	while pNode != None:
		pNext = pNode.pNext
		needDelete = false
		# 需要进行删除操作的条件
		if pNext != None and pNext.nValue == pNode.nValue:
			needDelete = true

		if not needDelete:
			preNode = pNode
			pNode = pNode.pNext
		else:
			value = pNode.nValue
			toBeDelNode = pNode
			# 删除连续重复节点
			while toBeDelNode != None and toBeDelNode.nValue == value:
				pNext = toBeDeleted.pNext
				toBeDelNode = None
				toBeDelNode = pNext
			# 重置pre指针
			if preNode != None:
				listNode = pNext
			else:
				preNode.pNext = pNext
			# 重置node指针
			pNode = pNext

# 19 正则表达式匹配
def match(characters, pattern):
	if characters == None || pattern == None:
		return

	return match_core(characters, pattern, 0, 0)

def match_core(characters, pattern, ci, pi):
	if characters == "" and pattern == "":
		return true

	if characters != "" and pattern == "":
		return false

	# notice: pattern have '*' or '.'
	# characters have not them	
	# pattern length > 1 
	# characters length >= 0
	if pattern[pi+1] == "*":
		if pattern[pi] == characters[ci] or
		(pattern[pi] == "." and characters[ci] != ""):
			return match_core(characters, pattern, ci+1, pi+1) # move on the next state
			|| match_core(characters, pattern, ci+1, pi) # stay on the current state
			|| match_core(characters, pattern, ci, pi+2) # ignore a '*'
	else:
		match_core(characters, pattern, ci, pi+2)

	# characters and pattern both length > 1
	if pattern[pi] == characters[ci] or
		(pattern[pi] == "." and characters[ci] != ""):
		return  match_core(characters, pattern, ci+1, pi+1)

	return false

