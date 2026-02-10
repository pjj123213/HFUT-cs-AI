class Myqueue:
    # 初始化队列：指定最大长度，初始化数据和元素计数
    def __init__(self, size):
        self.size = size      # 队列最大长度
        self.data = []        # 存储队列元素的列表
        self.current = 0      # 当前元素个数
    # 判断队列是否为空
    def is_empty(self):
        return self.current == 0
    # 判断队列是否已满
    def is_full(self):#
        return self.current == self.size
    # 取队头元素（队列非空时有效）
    def get_front(self):
        if self.is_empty():
            raise Exception("队列空，无法取队头元素")
        return self.data[0]
    # 入队：将元素添加到队尾（队列未满时有效）
    def enqueue(self, item):
        if self.is_full():
            print("队列已满，无法入队")
            return False
        self.data.append(item)
        self.current += 1
        return True
    # 出队：删除队头元素（队列非空时有效）
    def dequeue(self):
        if self.is_empty():
            print("队列空，无法出队")
            return False
        self.data.pop(0)
        self.current -= 1
        return True
def main():
    # 创建长度为 5 的队列实例
    N = 5
    queue = Myqueue(N)
    # 测试初始化后的状态
    print("队列初始化后：")
    print("是否为空？", queue.is_empty())
    print("是否已满？", queue.is_full())
    # 入队 5 个元素
    print("\n入队 5 个元素（1-5）：")
    for i in range(1, 6):
        queue.enqueue(i)
    print("当前队列数据：", queue.data)
    print("是否为空？", queue.is_empty())
    print("是否已满？", queue.is_full())
    # 取队头元素
    print("\n取队头元素：")
    try:
        front = queue.get_front()
        print("队头元素：", front)
    except Exception as e:
        print(e)
    # 5. 出队操作
    print("\n执行出队：")
    queue.dequeue()
    print("出队后队列数据：", queue.data)
    # 6. 再次入队（此时队列可再入 1 个元素）
    print("\n再次入队元素 6：")
    queue.enqueue(6)
    print("入队后队列数据：", queue.data)
    # 7. 测试队列满时入队
    print("\n队列满时入队元素 7：")
    queue.enqueue(7)  # 队列已满，应提示“队列已满，无法入队”

if __name__ == "__main__":
    main()