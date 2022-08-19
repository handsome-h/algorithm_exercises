"""
在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
"""

array = [
    [1, 2, 3, 4, 5],
    [2, 3, 4, 5, 6],
    [3, 4, 5, 6, 7]
]
num = 99


def find_1(array, num):
    """
    思路：穷举遍历
    时间复杂度：O(n^2)
    :param array:
    :param num:
    :return:
    """
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == num:
                return True

    return False


def find_2(array, num):
    """
    思路：从右上角的点开始，如果比该点的数小向左寻找，如果比该点的数大向下寻找
    时间复杂度：O(n)
    :param array:
    :param num:
    :return:
    """
    x = len(array[0])
    y = len(array)

    i = 0
    j = x - 1

    while True:
        if array[i][j] == num:
            return True
        elif array[i][j] > num:
            j -= 1
        elif array[i][j] < num:
            i += 1

        if i > y - 1 or j < 0:
            return False


print(find_2(array, num))
