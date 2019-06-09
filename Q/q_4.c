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
