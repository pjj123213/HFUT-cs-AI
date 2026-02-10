import re
# 使用正则表达式findall函数
def find_three_letter_words(text):
    # 查找所有由3个字母组成的单词
    # [a-zA-Z]{3}匹配3个字母
    pattern = r'\b[a-zA-Z]{3}\b'
    return re.findall(pattern, text)

def main():
    # 获取用户输入
    text = input("请输入一段英文: ")
    result = find_three_letter_words(text)
    print("\n使用正则表达式findall找到的3字母单词:")
    print(result)

if __name__ == "__main__":
    main()