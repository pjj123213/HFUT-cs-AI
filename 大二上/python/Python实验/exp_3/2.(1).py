def generate_strings():
    # 生成多个字符串（这边选择固定生成）
    return ["Hello", "World", "Python", "Programming", "FileIO"]

def write_to_file(strings, filename):
    # 将字符串列表写入文件，每行一个字符串
    with open(filename, "w", encoding="utf-8") as f:
        for s in strings:
            f.write(s + "\n")  # 每行末尾加换行符，确保每行一个字符串

def read_and_count(filename):
    # 读取文件并统计字符串个数（按行数统计）
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()  # 读取所有行到列表
    return len(lines)  # 列表长度即为字符串个数

def main():
    filename = "strings.txt"  # 文件名
    # 生成字符串
    strings = generate_strings()
    print("生成的字符串列表：", strings)
    # 将字符串写入文件
    write_to_file(strings, filename)
    print(f"已将字符串写入 {filename}")
    # 读取文件并统计个数
    count = read_and_count(filename)
    print(f"文件中字符串的个数：{count}")

if __name__ == "__main__":
    main()