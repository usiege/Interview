//替换空格
//实现一个函数，把字符串中的空格替换成"%20"

//length 最大长度
void replaceBlank(char string[], int length) {
    if (string == nullptr || length <= 0) {
        return;
    }

    int original_length = 0;
    int number_of_blank = 0;
    int i = 0;
    while (string[i] != '\0') {
        ++original_length;
        if (string[i] == ' ') {
            ++number_of_blank;
        }
        ++i;
    }

    int new_length = original_length + number_of_blank * 2;
    if (new_length > length) {
        return;
    }

    int index_of_original = original_length;    //原数组指针
    int index_of_new = new_length;              //新数组指针

    while (index_of_original >= 0 && index_of_new > index_of_original) {
        if (string[index_of_original] == ' ') {
            string[index_of_new--] = '0';
            string[index_of_new--] = '2';
            string[index_of_new--] = '%';
        } else {
            string[index_of_new--] = string[index_of_original];
        }
        --index_of_original;
    }
}


//回顾，这个算法的思路就是倒着进行复制，即先整体把握结果数组的大小
//只是一个从前往后到从后往前的转换，思路一下就清晰了
