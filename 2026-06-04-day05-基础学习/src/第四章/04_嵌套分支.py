
age = int(input("请输入你的年龄："))
has_report = input("您是否提交了体检报告：是/否")
level = int(input("请输入你的会员等级"))

if 18 <= age <= 45:
    print("您的年龄符合要求！")
    if has_report == "是":
        print("您已提交体检报告")
        if level == 1:
            print("你是会员1级")
        elif level == 2:
            print("你是会员2级")
        else:
            print("你是会员3级")
    elif has_report == "否":
        print("您未提交体检报告")
else :
    print("您不符合要求")