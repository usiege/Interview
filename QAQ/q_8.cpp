//给定一棵二叉树和其中的一个节点
//找出中序遍历的下一个节点
//树中的节点除了有左、右子节点指针，还有指向父结点指针

struct BinaryTreeNode
{
    int                 m_nValue;
    BinaryTreeNode*     m_pLeft;
    BinaryTreeNode*     m_pRight;
    BinaryTreeNode*     m_pParent;
};

BinaryTreeNode* getNext(BinaryTreeNode* pNode)
{
    if (pNode == nullptr) {
        return pNode;
    }

    BinaryTreeNode* pNext = nullptr;
    if (pNode->m_pRight != nullptr) {
        BinaryTreeNode* pRight = pNode->m_pRight;
        while (pRight->m_pLeft != nullptr) {
            pRight = pRight->m_pLeft;
        }
        pNext = pRight;
    }
    else if (pNode->m_pParent != nullptr) {
        BinaryTreeNode* pCurrent = pNode;
        BinaryTreeNode* pParent = pNode->m_pParent;
        while (pParent != nullptr && pCurrent == pParent->m_pRight) {
            pCurrent = pParent;
            pParent = pParent->m_pParent;
        }
        pNext = pParent;
    }

    return pNext;
}
