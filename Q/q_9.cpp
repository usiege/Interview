//栈和队列

//用两个栈实现队列
template <typename T> class CQueue {
private:
    /* data */
    stack<T> stack1;
    stack<T> stack2;


public:
    CQueue (void);
    virtual ~CQueue ();

    void appendTail(const T& node);
    T deleteHead();
};

template <typename T> class CQueue<T>::appendTail(const T& element)
{
    stack1.push(element);
}

template <typename T> class CQueue<T>::deleteHead()
{
    if (stack2.size() <= 0) {
        while (stack1.size() > 0) {
            T& data = stack1.top();
            stack1.pop();
            stack2.push(data);
        }
    }

    if (stack2.size() == 0) {
        throw new exception("queue is empty");
    }

    T head = stack2.top();
    stack2.pop();

    return head;
}
