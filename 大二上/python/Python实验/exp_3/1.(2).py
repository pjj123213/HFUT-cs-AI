class Employee:
    # 初始化雇员基础属性：姓名、编号、月薪
    def __init__(self, name, id, monthly_salary):
        self.name = name
        self.id = id
        self.monthly_salary = monthly_salary
    # 计算月薪（基类默认返回月薪本身）
    def pay(self):
        return self.monthly_salary
    # 显示雇员基础信息
    def show(self):
        print(f"雇员 {self.name}（编号：{self.id}），月薪：{self.monthly_salary} 元")

class Manager(Employee):
    # 初始化经理属性：姓名、编号、月薪、奖金
    def __init__(self, name, id, monthly_salary, bonus):
        super().__init__(name, id, monthly_salary)  # 调用父类初始化
        self.bonus = bonus  # 经理还有额外奖金
    # 计算经理月收入（重写pay()方法：经理月收入 = 月薪 + 奖金）
    def pay(self):
        return self.monthly_salary + self.bonus
    # 显示经理详细信息（含奖金、月收入）
    def show(self):
        total_pay = self.pay()
        print(
            f"经理 {self.name}（编号：{self.id}），月薪：{self.monthly_salary} 元，奖金：{self.bonus} 元，月收入：{total_pay} 元")

class Salesman(Employee):
    # 初始化销售员属性：姓名、编号、月薪、销售额、提成率
    def __init__(self, name, id, monthly_salary, sales, commission_rate):
        super().__init__(name, id, monthly_salary)  # 调用父类初始化
        self.sales = sales  # 月度销售额
        self.commission_rate = commission_rate  # 提成比例（如 0.1 表示 10%）
    # 计算销售员月收入（重写pay()方法：月薪 + 销售额×提成率）
    def pay(self):
        commission = self.sales * self.commission_rate  # 计算提成
        return self.monthly_salary + commission
    # 显示销售员详细信息（含销售额、提成率、提成、月收入）
    def show(self):
        commission = self.sales * self.commission_rate
        total_pay = self.pay()
        print(
            f"销售员 {self.name}（编号：{self.id}），月薪：{self.monthly_salary} 元，销售额：{self.sales} 元，提成率：{self.commission_rate}，提成：{commission} 元，月收入：{total_pay} 元")

def main():
    # 创建经理实例
    manager = Manager(name="张三", id="M001", monthly_salary=10000, bonus=5000)
    manager.show()
    print(f"经理 {manager.name} 的月收入：{manager.pay()} 元\n")
    # 创建销售员实例
    salesman = Salesman(name="李四", id="S001", monthly_salary=5000, sales=20000, commission_rate=0.1)
    salesman.show()
    print(f"销售员 {salesman.name} 的月收入：{salesman.pay()} 元")

if __name__ == "__main__":
    main()