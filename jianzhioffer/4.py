"""
请实现一个函数，把字符串中的每个空格替换成“%20”。例如输入“We are happy.”，则输出“We%20are%20happy.”。
"""

test_str = 'We are happy.'
# print(test_str[4])

def replace_blank(test_str):
    """
    思路：穷举
    时间复杂度：O(n)
    :param test_str:
    :return:
    """
    test_list = list(test_str)
    for index, item in enumerate(test_list):
        if item == ' ':
            test_list[index] = '%20'
    return ''.join(test_list)


def replace_blank_2(string):
    """
    思路：双指针
    时间复杂度：O(n)，空间复杂度：O(m)
    :param string:
    :return:
    """
    if string is None or len(string) == 0:
        return

    original_length = len(string)
    number_of_blank = 0
    for item in string:
        if item == ' ':
            number_of_blank += 1

    new_length = original_length + number_of_blank * 2
    index_of_original = original_length - 1
    index_of_new = new_length - 1

    new_string = ['' for i in range(new_length)]
    while 0 <= index_of_original:
        if string[index_of_original] == ' ':
            new_string[index_of_new] = '0'
            index_of_new -= 1
            new_string[index_of_new] = '2'
            index_of_new -= 1
            new_string[index_of_new] = '%'
        else:
            new_string[index_of_new] = string[index_of_original]

        index_of_new -= 1
        index_of_original -= 1

    print(new_string)
    return ''.join(new_string)


print(replace_blank_2(test_str))
