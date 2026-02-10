def Fibonacci(n):
    Fib_list = []
    a, b = 0, 1  # 初始值（这里视斐波那契数列首项从0开始）
    # 先添加初始值（需判断是否小于等于n）
    if a <= n:
        Fib_list.append(a)
    if b <= n:  # 避免n=0时重复添加
        Fib_list.append(b)
    # 生成斐波那契数列后续项，直到超过n
    while True:
        a, b = b, a + b # 更新：a变为前一个b，b变为前a+b
        if b >= n:
            break  # 超过n则停止
        Fib_list.append(b)
    return Fib_list
while True:
    try:
        n = int(input("请输入一个整数值n:"))
        print(Fibonacci(n))
        break
    except ValueError:
        print("类型错误，请输入一个整数！")
        continue