#!/usr/bin/env lua

-- 二叉树
-- 其中 dep 是深度
function CreateTree( dep )
	local root = { lchild = nil, rchild = nil, parent = nil, seq = 1, dep = 1 }
	root.lchild = CreateNode(root, 0, dep)
	root.rchild = CreateNode(root, 1, dep)

	return root
end

function CreateNode( node, position, dep )
	-- dep 是节点数
	print(node.dep, dep)
	if node.dep >= dep then return end

	local new_node = { parent = node, lchild = nil, rchild = nil, 
	seq = (position == 0 and node.seq*2 or node.seq*2 + 1), dep = node.dep + 1 }
	-- new_node there is a problem
	new_node.lchild = CreateNode(new_node, 0, dep)
	new_node.rchild = CreateNode(new_node, 1, dep)

	return new_node
end


-- input
-- 无重复节点
preIn = {1, 2, 4, 7, 3, 5, 6, 8}
midIn = {4, 7, 2, 1, 5, 3, 8, 6}

function PrintTree( node )
	print(node.seq)
	if node.lchild then 
		PrintTree(node.lchild)
	end
	if node.rchild then
		PrintTree(node.rchild)
	end
end

local tree = CreateTree(4)
PrintTree(tree)

-- 8
midSeq = {'d', 'b', 'h', 'e', 'i', 'a', 'f', 'c', 'g'}

-- 树
-- 找出中序遍历序列的下一个节点
function GetNext( pNode )
	if pNode == nil then return end
	pNext = nil
	if pNode.rchild ~= nil then
		pRight = pNode.rchild
		while pRight.lchild ~= nil do
			pRight = pRight.lchild
		end
		pNext = pRight
	elseif pNode.parent ~= nil then
		pCurrent = pNode
		pParent = pNode.parent
		while pParent ~= nil and pCurrent == pParent.rchild do
			pCurrent = pParent
			pParent = pParent.parent
		end
		pNext = pParent
	end
	return pNext
end


