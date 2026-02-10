import random
import string
# 生成长度不超过max_length的随机字符串，包含数字和字符
def generate_random_string(max_length):
    # 随机确定字符串长度，范围1到max_length
    length = random.randint(1, max_length)
    # 设定可能的字符集：数字 + 大小写字母
    characters = string.digits + string.ascii_letters
    # 随机选择字符并拼接成字符串
    return ''.join(random.choice(characters) for _ in range(length))
# 生成含有n个元素的嵌套列表，每个元素是包含随机字符串的列表
def generate_nested_list(n, m):
    nested_list = []
    for _ in range(n):
        # 每个子列表的长度随机（1到5之间，可根据需要调整）
        sublist_length = random.randint(1, 5)
        sublist = [generate_random_string(m) for _ in range(sublist_length)]
        nested_list.append(sublist)
    return nested_list
# 把嵌套列表展平，并按照字符串的长度降序排序
def flatten_and_sort(nested_list):
    # 展平嵌套列表
    flat_list = [s for sublist in nested_list for s in sublist]
    # 按字符串长度降序排序，如果长度相同则按字母顺序排序
    flat_list.sort(key=lambda x: (-len(x), x))
    return flat_list
def main():
    try:
        # 用户输入
        n = int(input("请输入嵌套列表的元素个数n: "))
        m = int(input("请输入字符串的最大长度m: "))
        if n <= 0 or m <= 0:
            print("n和m必须是正整数")
            return
        # 生成嵌套列表
        nested_list = generate_nested_list(n, m)
        print("\n生成的嵌套列表:")
        print(nested_list)
        for i, sublist in enumerate(nested_list, 1):
            print(f"子列表{i}: {sublist}")
        # 展平并排序
        sorted_list = flatten_and_sort(nested_list)
        print("\n按字符串长度降序排序后的结果:")
        print(sorted_list)
    except ValueError:
        print("输入错误，请输入整数")

if __name__ == "__main__":
    main()
