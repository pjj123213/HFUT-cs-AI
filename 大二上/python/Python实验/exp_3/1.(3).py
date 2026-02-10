class Vehicle:
    def __init__(self, max_speed, weight):
        # 定义两个私有属性（双下划线开头，触发名字修饰）
        self.__MaxSpeed = max_speed
        self.__weight = weight
class Bicycle(Vehicle):
    def __init__(self, max_speed, weight, height):
        # 调用父类构造方法，初始化父类的私有属性
        super().__init__(max_speed, weight)
        # 定义子类私有属性
        self.__height = height
    def SetMaxSpeed(self, new_max_speed):
        # 通过“名字修饰”访问父类私有属性 __MaxSpeed
        self._Vehicle__MaxSpeed = new_max_speed
    # 利用 @property 装饰器，将 __height 封装为可读写删的属性
    @property
    # 定义 height 的 getter 方法: 读取 __height
    def height(self):
        return self.__height
    # 定义 height 的 setter 方法: 修改 __height
    @height.setter
    def height(self, new_height):
        self.__height = new_height
    # 定义 height 的 deleter 方法: 删除 __height
    @height.deleter
    def height(self):
        del self.__height

def main():
    # 创建Bicycle实例
    bike = Bicycle(max_speed=20, weight=10, height=1.2)
    # 2. 调用 SetMaxSpeed 修改父类的 __MaxSpeed
    bike.SetMaxSpeed(25)
    # 验证父类 __MaxSpeed 是否被修改（通过名字修饰后的属性访问）
    print(f"验证height属性是否存在：{hasattr(bike, 'height')}")
    print("父类 MaxSpeed 被修改为：", bike._Vehicle__MaxSpeed)
    # 测试 height 的 property（读、写、删）
    print("初始height：", bike.height)  # 读取 height
    bike.height = 1.3  # 修改 height
    print("修改后height：", bike.height)
    del bike.height  # 删除 height
    try:
        print(bike.height)
    except AttributeError:
        print("height已被成功删除")

if __name__ == "__main__":
    main()