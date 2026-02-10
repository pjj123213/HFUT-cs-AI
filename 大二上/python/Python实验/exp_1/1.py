import random
# 生成1到10之间的随机数
random_num = random.randint(1, 10)

print("欢迎进入猜数字游戏！")
print(f"计算机已经想好了一个1到10之间的数字，请试着去猜出它。")

while True:
    try:
        guess = int(input(f"请输入你的猜测："))
        break
    except ValueError:
        print("请输入有效的整数！")
        continue
if guess == random_num:
    print(f"恭喜你！猜对了，答案就是{random_num}。")
else:
    print(f"很遗憾你猜错了，游戏结束")
    print(f"正确答案是：{random_num}")
