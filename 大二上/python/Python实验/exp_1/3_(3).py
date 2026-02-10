# 判断回文字符串
def is_palindrome(s,is_Case_Sensitive):
    # 预处理：去除字符串中的空格（并将其转换为小写）
    if is_Case_Sensitive:
        pre_processed = s.replace(" ", "")
    else:
        pre_processed = s.replace(" ", "").lower()
    return pre_processed == pre_processed[::-1] # 将字符串反转，并与原字符串进行比较

s1 = input("请输入需要判断的字符串：")
is_case_sensitive = int(input(f"是否区分大小写？（是请输入1，否请输入0）"))
if is_palindrome(s1,is_case_sensitive):
    print("此字符串为回文字符串")
else:
    print("此字符串不是回文字符串")