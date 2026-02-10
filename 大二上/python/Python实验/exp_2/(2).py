# 法一：使用系统集合类实现
def set_operations_system():
    # 输入两个集合
    input_str1 = input("请输入第一个集合的元素（用逗号分隔）：")
    input_str2 = input("请输入第二个集合的元素（用逗号分隔）：")
    # 转换为集合
    setA = set(int(item) for item in input_str1.split(','))
    setB = set(int(item) for item in input_str2.split(','))
    # 计算交集、并集、差集
    intersection = setA & setB
    union = setA | setB
    difference = setA - setB
    # 输出结果
    print(f"集合A: {setA}")
    print(f"集合B: {setB}")
    print(f"交集: {intersection}")
    print(f"并集: {union}")
    print(f"差集(A-B): {difference}")

# 法二：自定义集合类实现
class Custom_set():
    def __init__(self, elements=None):
        self.elements = []
        if elements:
            for element in elements:
                self.add(element)
    #__iter__方法，使Custom_set可迭代
    def __iter__(self):
        return iter(self.elements)
    # 添加元素
    def add(self, element):
        # 如果不存在，向集合中添加元素
        if element not in self.elements:
            self.elements.append(element)
    # 判断元素是否在集合中
    def contains(self, element):
        return element in self.elements
    # 集合的交集
    def intersection(self, other_set):
        result = Custom_set()
        for item in self.elements:
            if other_set.contains(item):
                result.add(item)
        return result
    # 集合的差集
    def difference(self, other_set):
        result = Custom_set()
        for item in self.elements:
            if not other_set.contains(item):
                result.add(item)
        return result
    # 集合的并集
    def union(self, other_set):
        result = Custom_set(self.elements)
        for item in other_set:
            result.add(item)
        return result
    def __str__(self):
        return "{" + ", ".join(self.elements) + "}"

def set_operations_selfdefine():
    input_str1 = input("请输入第一个集合的元素（用逗号分隔）：")
    input_str2 = input("请输入第二个集合的元素（用逗号分隔）：")
    # 转换为自定义集合
    setA = Custom_set(input_str1.split(','))
    setB = Custom_set(input_str2.split(','))
    # 计算交集、并集、差集
    intersection = setA.intersection(setB)
    union = setA.union(setB)
    difference = setA.difference(setB)
    # 输出结果
    print(f"集合A: {setA}")
    print(f"集合B: {setB}")
    print(f"交集: {intersection}")
    print(f"并集: {union}")
    print(f"差集(A-B): {difference}")

if __name__ == "__main__":
    print("=== 使用系统集合类实现 ===")
    set_operations_system()

    print("\n=== 使用自定义集合类实现 ===")
    set_operations_selfdefine()
