"""
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。
"""

array = [2, 1, 4, 5, 6, 3]


def change(array):
    """
    时间复杂度O(n)
    :param array:
    :return:
    """
    if array is None or len(array) <= 1:
        return array

    pre_index = 0
    post_index = len(array) - 1
    while pre_index != post_index:
        # 偶数
        if array[pre_index] % 2 == 0 and array[post_index] % 2 == 0:
            post_index -= 1
        elif array[pre_index] % 2 == 0 and array[post_index] % 2 == 1:
            array[pre_index], array[post_index] = array[post_index], array[pre_index]
        elif array[pre_index] % 2 == 1:
            pre_index += 1

    return array

change(array)
print(array)
