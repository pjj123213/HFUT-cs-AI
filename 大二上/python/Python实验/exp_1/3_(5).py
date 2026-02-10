import math

def calculate_daily_effort():
    # 相关数据初始化
    days_in_year = 365
    work_days_per_week = 5
    rest_days_per_week = 2
    rest_day_factor = 0.99  # 休息日水平下降0.01
    target_effect = 37.78  # 每天努力1%一年后的效果
    # 计算一年之中的工作日和休息日数量，多余的天数按工作日计算（前5天为工作日）
    weeks_in_year = days_in_year // 7
    extra_days = days_in_year % 7
    work_days = weeks_in_year * work_days_per_week + min(extra_days, work_days_per_week)
    rest_days = weeks_in_year * rest_days_per_week + max(0, extra_days - work_days_per_week)
    # 计算休息日的总影响
    rest_days_effect = pow(rest_day_factor, rest_days)
    # 计算工作日需要达到的努力程度
    # (1 + x)^work_days * rest_days_effect = target_effect
    # => 1 + x = (target_effect / rest_days_effect)^(1/work_days)
    required_daily_factor = (target_effect / rest_days_effect) ** (1 / work_days) - 1
    # 转换为百分比努力程度
    daily_effort_percent = required_daily_factor * 100
    return daily_effort_percent

effort = calculate_daily_effort()
print(f"为了达到与每天努力1%相同的年度效果，")
print(f"在每周工作5天、休息2天（休息日水平下降1%）的情况下，")
print(f"每个工作日需要努力的程度为：{effort:.2f}%")