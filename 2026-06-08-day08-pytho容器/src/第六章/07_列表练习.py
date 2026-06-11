print("请输入学生成绩，输入结束结束输入")

score_list = []

#持续循环，让用户输入成绩
while True:
    data = input("请输入成绩:")
    if data == "结束":
        break
    else:
        score_list.append(int(data))


if score_list:
    avg = sum(score_list)/len(score_list)
    pass_count = 0
    good_count = 0
    for item in score_list:
        if item > 60:
            pass_count += 1
        if item > 90:
            good_count += 1
    pass_rate = pass_count/len(score_list) * 100
else:
    print("null")