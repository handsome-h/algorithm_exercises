"""
二进制计算
"""

# &：两个位都为1时，结果才为1（统计奇数）即全1为1。
a1 = 10
b1 = 9
"""
10 = 0b1010
9  = 0b1001
8  = 0b1000
"""
print(bin(a1))
print(bin(b1))
print(a1 & b1)  # 8
print(int("0b1000", 2))

# |：两个位都为0时，结果才为0（统计偶数）即全0为0。
a2 = 10
b2 = 9
"""
10 = 0b1010
9  = 0b1001
11 = 0b1011
"""
print(bin(a2))
print(bin(b2))
print(a2 | b2)  # 11
print(int("0b1011", 2))

# ^：两个位相同为0，相异为1(常用统计不相同数）即不同为1。
a3 = 10
b3 = 9
"""
10 = 0b1010
9  = 0b1001
3  = 0b0011
"""
print(bin(a3))
print(bin(b3))
print(a3 ^ b3)  # 11
print(int("0b0011", 2))

# ~：0变1，1变0，相当于 -x-1
a4 = 10
"""
10 = 0b1010
-x-1 = -11
"""
print(bin(a4))
print(~a4)  # -11
print(int("-0b1011", 2))

# 求相反数
print(~a4 + 1)  # -10

# <<：各二进位全部左移若干位，高位丢弃，低位补0，即：x << n = x * (2 ** n)
a5 = 10
"""
10 = 0b1010
x = 10 * 2 ** 3 = 10 * 2 * 2 * 2
"""
b5 = a5 << 3
print(bin(b5))
print(b5)  # 80
print(int("0b1010000", 2))

# >>：各二进位全部右移若干位，对无符号数，高位补0，有符号数进行补符号位（算术右移），或者补0（逻辑右移）。
#     即：x << n = x / (2 ** n)
a6 = 64
"""
64 = 0b1000000
x = 64 / (2 ** 3) = 64 / (2 * 2 * 2)
"""
b6 = a6 >> 3
print(bin(b6))
print(b6)  # 8

# 经典案例：使用 ^ 找出出现一次的数
a7 = 1 ^ 1 ^ 2
a8 = 1 ^ 2 ^ 1
a9 = 2 ^ 1 ^ 1
print(a7)
print(a8)
print(a9)

# 统计原始方法和位运算方法花费的时间
import time

loop = 30000000
start1 = time.time()
odd_list1 = []

for i in range(loop):
    if i & 1 == 1:
        odd_list1.append(i)
end1 = time.time()
print(f"time1:{end1 - start1}")

start2 = time.time()
odd_list2 = []

for i in range(loop):
    if i % 2 == 1:
        odd_list1.append(i)
end2 = time.time()
print(f"time2:{end2 - start2}")
# time1:5.262001037597656
# time2:4.736037492752075

print('算法')
"""
请实现一个函数，输入一个整数，输出该数二进制表示中1的个数。例如把9表示成二进制是1001，有2位是1。因此如果输入9，该函数输出2。
"""


