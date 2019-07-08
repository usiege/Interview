//把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转
int min(int* numbers, int length)
{
    if (numbers == nullptr || length <= 0) {
        throw new std::exception("Invaild parameters");
    }

    int index1 = 0;
    int index2 = length - 1;
    int indexMid = index1;
    while (numbers[index1] >= numbers[index2]) {
        if(index2 - index1 == 1)
        {
            indexMid = index2;
            break;
        }

        indexMid = (index1 + index2) / 2;
        //插入部分
        if (numbers[index1] == numbers[index2] &&
            numbers[indexMid] == numbers[index1]) {
            return minInOrder(numbers, index1, index2);
        }

        //
        if (numbers[indexMid] >= numbers[index1]) {
            index1 = indexMid;
        } else if (numbers[indexMid] <= numbers[index2]){
            index2 = indexMid;
        }
    }
    return numbers[indexMid];
}

//需要考虑以下两种情况
//1. 当数组的前0个元素发生旋转，旋转数组是其本身；第一个数字就是最小的数字，返回；
//2. 考虑有重复数字的情况，边界值考虑；

int minInOrder(int* numbers, int index1, int index2)
{
    int result = numbers[index1];
    for (size_t i = index1 + 1; i < index2; i++) {
        if(result > numbers[i]){ //这里应该 < ？
            result = numbers[i];
        }
    }

    return result;
}
