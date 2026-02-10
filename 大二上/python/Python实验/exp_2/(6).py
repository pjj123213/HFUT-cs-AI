import string
# 统计输入字符串中每个单词的出现次数
def count_words(input_str):
    # 创建标点符号翻译表，用于去除字符串中的标点
    translator = str.maketrans('', '', string.punctuation)
    # 去除标点符号
    processed_str = input_str.translate(translator)
    # 将字符串按空格分割为单词列表
    words = processed_str.split()
    # 用字典存储单词及其出现次数
    word_counts = {}
    # 统计每个单词的出现次数
    for word in words:
        # 若单词已在字典中，计数加1；否则添加到字典并设为1
        word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts

def main():
    # 获取用户输入的字符串
    input_str = input("请输入任意长度的字符串: ")
    # 统计单词出现次数
    result = count_words(input_str)
    print("\n单词出现次数统计如下:")
    for word, count in result.items():
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()