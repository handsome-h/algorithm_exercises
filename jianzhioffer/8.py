"""
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
"""


# 方法1，顺序遍历一遍，时间复杂度O(n)


def min_in_order(array):
    result = array[0]
    for item in array:
        if result > item:
            result = item

    return result


def c_min(array):
    if array is None or len(array) == 0:
        return

    index_pre = 0
    index_post = len(array) - 1
    index_mid = index_pre
    while array[index_pre] >= array[index_post]:
        if index_post - index_pre == 1:
            index_mid = index_post
            break

        index_mid = (index_pre + index_post) // 2

        if array[index_pre] == array[index_post] and array[index_mid] == array[index_pre]:
            return min_in_order(array[index_pre: index_post])

        if array[index_mid] >= array[index_pre]:
            index_pre = index_mid
        elif array[index_mid] <= array[index_post]:
            index_post = index_mid

    return array[index_mid]


a = [3, 4, 5, 1, 2]
print(c_min(a))
