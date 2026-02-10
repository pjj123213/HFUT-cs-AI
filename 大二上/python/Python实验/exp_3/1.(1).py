class Student:
    # 初始化学生基本信息与成绩字典
    def __init__(self, student_id, name, gender, age):
        # 基本信息
        self.student_id = student_id
        self.name = name
        self.gender = gender
        self.age = age
        self.scores = {} # 字典存储课程成绩
    # 设置课程成绩
    def set_score(self, course, score):
        self.scores[course] = score
    # 计算三门课程（语文、数学、英语）的平均分
    def calculate_average(self):
        courses = ["语文", "数学", "英语"]
        total = 0
        for course in courses:
            if course in self.scores:
                total += self.scores[course]
        # 确保有三门有效成绩，否则返回None（实际可根据需求调整）
        return total / 3
    # 从文件读取学生基本信息，返回Student对象列表
    def read_students_from_file(filename):
        students = []
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(",")
                student_id, name, gender, age = parts[0], parts[1], parts[2], int(parts[3])
                students.append(Student(student_id, name, gender, age))
        return students
    # 为每个学生录入三门课程成绩
    def input_scores(students):
        courses = ["语文", "数学", "英语"]
        for student in students:
            print(f"\n----- 录入学生 {student.name}（学号：{student.student_id}）的成绩 -----")
            for course in courses:
                score = float(input(f"请输入「{course}」成绩："))
                student.set_score(course, score)
    # 计算平均分、排序并输出学生信息与排名
    def rank_and_print(students):
        # 存储（学生对象，平均分）的列表
        student_with_avg = []
        for student in students:
            avg = student.calculate_average()
            student_with_avg.append((student, avg))
        # 按平均分正序排序
        student_with_avg.sort(key=lambda x: x[1])
        # 格式化输出
        print("\n---- 学生成绩排名（正序） ----")
        print("学号\t姓名\t性别\t年龄\t语文成绩\t数学成绩\t英语成绩\t平均分\t排名")
        for rank, (student, avg) in enumerate(student_with_avg, 1):
            chinese = student.scores.get("语文", 0)
            math = student.scores.get("数学", 0)
            english = student.scores.get("英语", 0)
            print(
                f"{student.student_id}\t{student.name}\t{student.gender}\t{student.age}"
                f"\t{chinese}\t\t{math}\t\t{english}\t\t{avg:.2f}\t{rank}")

def main():
    filename = r"D:\exp_3\students.txt"  # 学生基本信息文件
    students = Student.read_students_from_file(filename)  # 步骤2：读取文件
    Student.input_scores(students)                       # 步骤3：录入成绩
    Student.rank_and_print(students)                     # 步骤4：排名并输出

if __name__ == "__main__":
    main()