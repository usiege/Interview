//查找和排序
//新报的深度之眼每周有leecode代刷，我想我可能需要添加一个新的代码库；
//所以还是把之前的代码库利用起来吧；我把CNN-CUSTOM改成了KEEP-DEEP-LEARNING，希望keep这个系列的库能带飞我；
//说上面的时候我有点不那么自信了，捂脸的那个表情，这里打不出来，脑补下。。。
//回到正题

//2.4.2
//记得之前iOS的面试中，涉及到算法的时候，一般都会去问关于查找和排序的问题；
//有时候有可能只是简单的让写一个书上有的归并？冒泡？算法，然而。。。
//所以身为一个程序员，这些基础怎么可以不信手拈来？
//实现吧，骚年；

//下面我们来写一下快速排序

int partition(int data[], int length, int start, int end)
{
    if (data = nullptr || length <= 0 || start < 0 || end >= length) {
        throw new std::exception("Invalid parameters!");
    }
    //我觉得上面的参数检查是最好写的，这是一个细活，就是考虑传进来参数的问题，这在测试时是很有用的，
    //一般会在实际工程中有所体现，因为你永远不知道一个函数被传进来的是一些什么数据

    int index = random_in_range(start, end); //这个函数产生一个start到end之前的随机数
    swap(&data[index], &data[end]);

    int small = start - 1;
    for (index = start; index < end; index++) {
        if (data[index] < data[end]) {
            ++ small;
            if (small != index) {
                swap(&data[index], &data[small]);
            }
        }
    }

    ++ small;
    swap(&data[small], &data[end]);

    return small;
}

//上面的这个选择index的过程有点绕，但是要注意，该过程仅仅是寻找一个位置
//在寻找位置的过程发生的元素交换是该排序算法的唯一交换过程

void quickSort(int data[], int length, int start, int end)
{
    if (start == end) {
        return; //终止条件
    }

    int index = partition(data, length, start, end);

    if (index > start) {
        quickSort(data, length, start, index - 1);
    }

    if (index < end) {
        quickSort(data, length, index + 1, end);
    }
}
