import random

def randon_list_process(n):
    # 生成含n个取值范围为1到100的元素的列表
    List = [random.randint(1, 100) for _ in range(n)]
    ave = sum(List) / n
    # 利用列表推导式筛选出列表中大于平均数的所有元素
    above_ave = [i for i in List if i > ave]
    # 返回原数列和需要输出的元组
    return List, (ave,) + tuple(above_ave)

n  = int(input(f"请输入一个整数n:"))
original_list, result = randon_list_process(n)
print(f"原数列为：",original_list)
print(f"计算结果：",result)