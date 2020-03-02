struct ListNode
{
    int     m_nValue;
    ListNode* m_pNext;
};

//输入链表头节点，从尾到头反过来打印出每个节点的值

void printListReversingly_iteratively(ListNode* pHead) {
    std::stack<ListNode *> nodes;

    ListNode* pNode = pHead;
    while (pNode != nullptr) {
        nodes.push(pNode);
        pNode = pNode->m_pNext;
    }

    while (!nodes.empty()) {
        pNode = nodes.top();
        printf("%d \t", pNode->m_nValue);
        nodes.pop();
    }
}

//递归形式
void printListReversingly_recursively(ListNode* pHead)
{
    if (pHead != nullptr) {
        if (pHead->m_nValue != nullptr) {
            printListReversingly_recursively(pHead->m_pNext);
        }
        printf("%d \t", pHead->m_nValue);
    }
}
