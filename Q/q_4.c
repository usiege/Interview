//在一个二维数组中，每一行从左到右递增,第一列从上到下递增；
//给定一个该二维数组及一个整数，判断该数组是否包含这个整数

bool find(int* matrix, int rows, int columns, int number)
{
    bool found = false;

    if (matrix != nullptr && rows > 0 && columns > 0) {
        int row = 0;
        int column = columns - 1;

        while (row < rows && column >= 0) {
            if (matrix[row * columns + column] == number) {
                found = true;
                break;
            }
            else if (matrix[row * columns + column] > number) {
                --column;
            }
            else {
                ++row;
            }
        }
    }
    return found;
}

//
int _tmain(int argc, _TCHAR* argv[])
{
    char str1[] = "hello world";
    char str2[] = "hello world";

    char* str3 = "hello world";
    char* str4 = "hello world";

    if (str1 == str2) {
        printf("str1 and str2 are same,\n", );
    } else {
        printf("str1 and str2 are not same,\n", ); //输出该行
    }

    if (str3 == str4) {
        printf("str3 and str4 are same,\n", ); //输出该行
    } else {
        printf("str3 and str4 are not same,\n", );
    }
    return 0;
}

//str3 str4 同时指向了字符常量“hello world”，它在内存中只有一个拷贝
