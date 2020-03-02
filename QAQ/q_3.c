//题目1
//找出数组中重复的数字
//所有数字都在 0~n-1 范围内
bool duplicate(int numbers[], int length, int* duplication)
{
    if (numbers == nullptr || length <= 0) {
        /* code */
        return false;
    }
    for (size_t i = 0; i < length; i++) {
        if (numbers[i] < 0 || numbers[i] > length-1) {
            /* code */
            return false;
        }
    }
    for (size_t i = 0; i < length; i++) {
        while (numbers[i] != i) {
            if (numbers[i] == numbers[numbers[i]]) {
                *duplicate = numbers[i];
                return true;
            }
        }

        //swap numbers[i] and numbers[numbers[i]]
        int temp = numbers[i];
        numbers[i] = numbers[temp];
        numbers[temp] = temp;
    }
}


//题目2
//不修改数组找出重复的数字
//所有数字都在 1~n 范围内
//不能修改原数组
int getDuplication(const int* numbers, int length)
{
    if (numbers == nullptr || length <= 0) {
        return -1;
    }

    int start = 1;
    int end = length - 1;
    while (end >= start) {
        int middle = ((end - start) >> 1) + start;
        int count = countRange(numbers, length, start, middle);
        if (end == start) {
            if (count > 1) {
                return start;
            } else {
                break;
            }
            if (count > (middle - start + 1)) {
                end = middle;
            } else {
                start = middle + 1;
            }
        }
    }
    return -1;
}
int countRange(const int* numbers, int length, int start, int end)
{
    if (numbers == nullptr) {
        return 0;
    }

    int count = 0;
    for (size_t i = 0; i < length; i++) {
        if (numbers[i] >= start && numbers[i] <= end) {
            ++count;
        }
    }
    return count;
}
