//树
struct BinaryTreeNode
{
    int                 m_nValue;
    BinaryTreeNode*     m_pLeft;
    BinaryTreeNode*     m_pRight;
};

//根据前序遍历序列和中序遍历序列重建二叉树
BinaryTreeNode* construct(int* preorder, int* inorder, int length)
{
    if (preorder == nullptr || inorder == nullptr || length <= 0) {
        return nullptr
    }

    return constructCore(preorder, preorder + length - 1,
                        inorder, inorder + length - 1)
}

BinaryTreeNode* constructCore
(
    int* startPreorder, int* endPreorder,
    int* startInorder, int* endInorder
)
{
    //前序遍历序列的第一个数字是根节点的值
    int rootValue = startPreorder[0];
    BinaryTreeNode* root = new BinaryTreeNode();
    root->m_nValue = rootValue;
    root->m_pLeft = root->m_pRight = nullptr;

    if (startPreorder == endPreorder) {
        if (startInorder == endInorder && *startPreorder == *startInorder) {
            return root;
        }
        else{
            throw std::exception("Invalid input.");
        }
    }
    //when I wrote this, only God and I understand what I was doing.
    //Now, God only knows.

    //在中序遍历序列中找到根节点的值
    int* rootInorder = startInorder;
    while (rootInorder <= endInorder && *rootInorder != rootValue) {
        ++rootInorder;
    }

    if (rootInorder == endInorder && *rootInorder != rootValue) {
        throw std::exception("Invalid input.")
    }

    int leftLength = rootInorder - startInorder;
    int* leftPreorderEnd = startPreorder + leftLength;
    if (leftLength > 0) {
        //构建左子树
        root->m_pLeft = constructCore(startPreorder + 1, leftPreorderEnd,
                        startInorder, rootInorder - 1);
    }
    if (leftLength < endPreorder - startPreorder) {
        //构建右子树
        root->m_pRight = constructCore(leftPreorderEnd + 1, endPreorder,
                        rootInorder + 1, endInorder)
    }

    return root;
}
