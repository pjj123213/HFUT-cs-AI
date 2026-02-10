import matplotlib.pyplot as plt
from matplotlib import font_manager

# 设置 matplotlib 支持中文
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

import csv
from datetime import datetime

class ExpenseManager:
    def __init__(self):
        self.records = []
        self.file = "expenses.csv"
        self.load_data()

    def load_data(self):
        try:
            with open(self.file, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                self.records = list(reader)
        except FileNotFoundError:
            self.records = []

    def save_data(self):
        with open(self.file, "w", newline="", encoding="utf-8") as f:
            fieldnames = ["date", "category", "amount", "note"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.records)

    def add_record(self):
        date = input("输入日期(YYYY-MM-DD): ")
        category = input("输入类别(餐饮/交通/娱乐/教育/日常生活用品/其他): ")
        amount = input("输入金额: ")
        note = input("备注: ")
        self.records.append({"date": date, "category": category, "amount": amount, "note": note})
        self.save_data()
        print("✅ 添加成功！")

    def delete_record(self):
        self.show_all()
        idx = int(input("输入要删除的序号: ")) - 1
        if 0 <= idx < len(self.records):
            del self.records[idx]
            self.save_data()
            print("✅ 删除成功！")
        else:
            print("❌ 无效序号！")

    def show_all(self):
        print("\n=== 所有支出记录 ===")
        for i, r in enumerate(self.records, 1):
            print(f"{i}. {r['date']} | {r['category']} | ￥{r['amount']} | {r['note']}")

    def query(self):
        category = input("输入要统计的类别(留空则统计全部): ")
        total = 0
        for r in self.records:
            if category == "" or r["category"] == category:
                total += float(r["amount"])
        print(f"总支出: ￥{total:.2f}")

    def chart(self):
        """显示支出饼图（非阻塞显示，不会卡住程序）"""
        stat = {}
        for r in self.records:
            cat = r["category"]
            stat[cat] = stat.get(cat, 0) + float(r["amount"])

        # 生成圆饼图
        plt.figure()
        plt.pie(stat.values(), labels=stat.keys(), autopct="%1.1f%%")
        plt.title("支出类别占比")
        plt.savefig("chart.png")

        # 使用非阻塞模式
        plt.show(block=False)
        plt.pause(0.1)  # 保持窗口打开，让程序继续执行

    def mainmenu(self):
        while True:
            print("\n--- 支出管理系统 ---")
            print("1. 添加支出")
            print("2. 删除支出")
            print("3. 查看记录")
            print("4. 查询统计")
            print("5. 查看图表")
            print("6. 退出")
            choice = input("请选择(1-6): ")
            if choice == "1": self.add_record()
            elif choice == "2": self.delete_record()
            elif choice == "3": self.show_all()
            elif choice == "4": self.query()
            elif choice == "5": self.chart()
            elif choice == "6":
                print("💾 数据已保存，程序结束。")
                break
            else:
                print("❌ 无效选择！")

if __name__ == "__main__":
    manager = ExpenseManager()
    manager.mainmenu()
