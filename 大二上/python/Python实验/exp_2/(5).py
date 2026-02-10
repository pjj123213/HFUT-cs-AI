import random
# 使用生成器推导式生成包含n个不大于m的整数的元组，并过滤掉偶数
def generate_odd_tuple(n, m):
    # 生成器推导式：生成n个1到m之间的随机整数
    number_generator = (random.randint(1, m) for _ in range(n))
    # 将生成器结果转换为列表（可重复访问）
    original_list = list(number_generator)
    # 过滤掉偶数，转换为元组并返回
    filter_even_tuple = tuple(num for num in original_list if num % 2 != 0)
    return tuple(original_list),filter_even_tuple

def main():
    try:
        # 用户输入
        n = int(input("请输入要生成的整数数量n: "))
        m = int(input("请输入整数的最大值m: "))
        if n <= 0 or m <= 0:
            print("n和m必须是正整数")
            return
        # 调用函数获得结果
        original_tuple, result_tuple= generate_odd_tuple(n, m)
        # 输出
        print(f"\n生成的包含{n}个整数的元组为：")
        print(original_tuple)
        print(f"过滤掉偶数后：")
        print(result_tuple)

    except ValueError:
        print("输入错误，请输入整数")

if __name__ == "__main__":
    main()