import random
# 生成1到100之间的随机数
random_num = random.randint(1, 100)
# 设置最大可用的猜测次数
max_chances = 20
# 记录当前的猜测次数
current = 0
# 标识用户是否猜对
flag = False
print("欢迎进入猜数字游戏！")
print(f"计算机已经想好了一个1到100之间的数字，你有{max_chances}次机会猜出它。")

# 循环让用户猜测，直到猜对或次数用完
while current < max_chances:
    # 获取用户输入并转换为整数
    try:
        guess = int(input(f"请输入你的猜测："))
    except ValueError:
        print("请输入有效的整数！")
        current += 1 # 输入格式错误也会消耗猜测次数
        continue
    current += 1
    # 使用if判断比较猜测的数字和答案
    if guess == random_num:
        print(f"恭喜你！用了{current}次就猜对了，答案就是{random_num}。")
        flag = True  # 猜对了，标志位置True
        break
    elif guess < random_num:
        print(f"太小了！你还剩{max_chances - current}次机会。")
    else:
        print(f"太大了！你还剩{max_chances - current}次机会。")
if(not flag):
    print(f"很遗憾游戏结束！你已经用完了所有d的机会。")
    print(f"正确答案是：{random_num}")