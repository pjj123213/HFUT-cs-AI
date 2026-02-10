import random
import string
from collections import Counter
# 法一：使用列表推导式 + 字典手动统计
def count_chars_methods_1():
    # 生成包含 1000 个随机字符的字符串
    random_chars = [random.choice(string.printable) for _ in range(1000)]
    random_string = ''.join(random_chars)
    # 建立字典进行统计
    chars_count = {}
    for char in random_string:
        # 字符在字典中存在则计数+1，不存在则初始化为1
        chars_count[char] = chars_count.get(char, 0) + 1
    return random_string[:20] + '...', chars_count

# 法二：列表推导式 + Counter自动统计
def count_chars_methods_2():
    random_str = ''.join([random.choice(string.printable) for _ in range(1000)])
    # 通过Counter(字典的子类) 进行统计
    char_count = Counter(random_str)
    return random_str[:20] + '...', char_count
# 测试
str1, count_1 = count_chars_methods_1()
print("------方法1：列表推导式+字典手动统计------")
print(f"随机字符串前20个字符：", str1)
print(f"前十个字符的统计结果：{dict(list(count_1.items())[:10])}")

str2, count_2 = count_chars_methods_2()
print("------方法2：列表推导式+Counter统计------")
print(f"随机字符串前20个字符：", str2)
print(f"前十个字符的统计结果：{dict(list(count_2.items())[:10])}")
