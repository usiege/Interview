//链表

struct ListNode
{
    int     m_nValue;
    ListNode* m_pNext;
};

//链表末尾添加节点
void addToTail(ListNode** pHead, int value)
{
    ListNode* pNew = new ListNode();
    pNew->m_nValue = value;
    pNew->m_pNext = nullptr;

    if (*pHead == nullptr) {
        *pHead = pNew;
    } else {
        ListNode* pNode = *pHead;
        while (pNode->m_pNext != nullptr) {
            pNode = pNode->m_pNext;
        }

        pNode->m_pNext = pNew;
    }
}

//删除某节点
void removeNode(ListNode** pHead, int value)
{
    if (pHead == nullptr || *pHead == nullptr) {
        return;
    }

    //下面的这个过程其实是寻找链表中第一个碰到的value的节点
    ListNode* pToBeDeleted = nullptr;
    if ((*pHead)->m_nValue == value) {
        pToBeDeleted = *pHead;
        *pHead = (*pHead)->m_pNext;
    } else {
        ListNode* pNode = *pHead;
        while (pNode->m_pNext != nullptr && pNode->m_pNext->m_nValue != value) {
            pNode = pNode->m_pNext;
        }
        //处理value节点
        if (pNode->m_pNext != nullptr && pNode->m_pNext->m_nValue == value) {
            pToBeDeleted == pNode->m_pNext;
            pNode->m_pNext = pNode->m_pNext->m_pNext;
        }
    }

    //上述寻找的过程中
    //很重要的一点是将节点保存
    //以及保证原链表不会断链
    if (pToBeDeleted != nullptr) {
        delete pToBeDeleted;
        pToBeDeleted = nullptr;
    }
}
