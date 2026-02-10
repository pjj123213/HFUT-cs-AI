# 检查密码是否符合所有有效性条件
def is_valid_password(password):
    # 条件5、6：长度在 6~12 之间
    if not (6 <= len(password) <= 12):
        return False
    # 条件1：至少1个小写字母 [a-z]
    has_lower = any(c.islower() for c in password)
    # 条件3：至少1个大写字母 [A-Z]
    has_upper = any(c.isupper() for c in password)
    # 条件2：至少1个数字 [0-9]
    has_digit = any(c.isdigit() for c in password)
    # 条件4：至少1个特殊字符 [$#@]
    has_special = any(c in '$#@' for c in password)
    # 所有条件都满足时返回 True
    return has_lower and has_upper and has_digit and has_special
def main():
    # 读取用户输入的逗号分隔密码
    input_str = input("请输入逗号分隔的密码：")
    # 分割为密码列表
    passwords = input_str.split(',')
    valid_passwords = []
    # 遍历检查每个密码的有效性
    for pwd in passwords:
        if is_valid_password(pwd):
            valid_passwords.append(pwd)
    # 输出符合条件的密码
    print(','.join(valid_passwords))

if __name__ == "__main__":
    main()