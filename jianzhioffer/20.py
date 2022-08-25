"""
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。
"""

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]


def print_matrix_circle(matrix: list):
    """默认从(0, 0)起始"""
    end_x = len(matrix[0]) - 1
    end_y = len(matrix) - 1

    # 从左向右打印一行
    for i in range(end_x+1):
        print(matrix[0])
