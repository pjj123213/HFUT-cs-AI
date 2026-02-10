# 利用列表实现筛选法求素数，输出小于特定输入数字的所有素数组成的列表。
import math
# 判断素数的函数
def is_Prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n%i == 0:
            return False
    return True
# 获取素数列表的函数
def get_primes_list(n):
    primes = []
    for i in range(n):
        if is_Prime(i):
            primes.append(i)
    return primes
while True:
    try:
        n = int(input("请输入一个大于2的自然数:"))
        print(f"小于这个数字的所有素数组成的列表为:",get_primes_list(n))
        break
    except ValueError:
        print("输入错误，请重新输入一个大于2的自然数！")
        continue