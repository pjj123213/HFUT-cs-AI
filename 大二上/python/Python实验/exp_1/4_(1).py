def connect_strings(str1, str2):
    # 计算可能重叠的最大长度
    max_length = min(len(str1),len(str2))
    # 通过lambda表达式来判断length长度的字符串是否为交叉子串
    is_cross = lambda length : str1[-length:] == str2[:length]
    # 最大的交叉长度，初始时为0
    cross_length = 0
    for i in range(max_length):
        if is_cross(i):
            cross_length = i
    return cross_length, str1 + str2[cross_length:]

str1 = input("请第一个字符串：")
str2 = input("请第二个字符串：")

max_cross_substring,connect_str = connect_strings(str1, str2)
print(f"最大字串长度为:", max_cross_substring)
print(f"合并后的新字符串为：",connect_str)