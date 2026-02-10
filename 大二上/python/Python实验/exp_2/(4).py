import random
# 生成指定长度范围的随机整型列表
def generate_integer_list(length, min_val=0, max_val=100):
    return [random.randint(min_val, max_val) for _ in range(length)]
# 返回列表的副本
def get_original_list(lst):
    return lst.copy()
# 返回列表的逆序
def get_reversed_list(lst):
    return lst[::-1]  # 使用切片实现逆序
#返回列出具有偶数位置的元素列表。
def get_even_position_elements(lst):
    return lst[::2]  # 设置步长为2即可

def main():
    try:
        length = int(input("请输入列表的长度: "))
        if length <= 0:
            print("列表长度必须是正整数")
            return
        # 生成随机整型列表
        original = generate_integer_list(length)
        print(f"\n生成的整型列表: {original}")
        # 获取列表副本
        new_list = get_original_list(original)
        print(f"包含所有元素的新列表: {new_list}")
        #获取逆序列表
        reversed_list = get_reversed_list(original)
        print(f"逆序列表: {reversed_list}")
        # 获取偶数位置元素列表
        even_position_list = get_even_position_elements(original)
        print(f"偶数位置（0, 2, 4...）的元素列表: {even_position_list}")

    except ValueError:
        print("输入错误，请输入整数!")

if __name__ == "__main__":
    main()