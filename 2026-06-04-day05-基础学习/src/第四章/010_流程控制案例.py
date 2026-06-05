

# for n in range(1,4):
#     print(f"现在是关卡{n}")
#     error = 0
#     if n == 1:
#         for num in range(1,4):
#             answer1 = input("请问你叫什么？")
#             while answer1 == '':
#                 answer1 = input("输入不能为空，请问你叫什么？")
#             if answer1 == "fgh":
#                 print(f"回答正确，进入第{n+1}关")
#                 break
#             error += 1
#             print(f"您第{num}次回答错误，还有{3-num}次机会")
#
#     elif n == 2:
#         for num in range(1,4):
#             answer2 = int(input("我的幸运数字是多少？"))
#             if answer2 == 888:
#                 print(f"回答正确，进入第{n + 1}关")
#                 break
#             error += 1
#             print(f"您第{num}次回答错误，还有{3-num}次机会")
#
#     elif n == 3:
#         for num in range(1,4):
#             answer2 = input("我的性别是什么")
#             if answer2 == "男":
#                 print("全部问题回答成功！！！")
#                 break
#             error += 1
#             print(f"您第{num}次回答错误，还有{3-num}次机会")
#     if error == 3:
#         break

print("欢迎来到：答题闯关塞（输入q可以随时退出游戏）\n")

#题目与答案
ques1, ans1 = "python 中用于输出的函数是什么？", "print"
ques2, ans2 = "python 中用于表示且的关键字是什么？", "and"
ques3, ans3 = "python 属于编译型还是解释型？", "解释型"

#最多尝试次数
max_tries = 3

#总关卡数
total_levels = 3

#是否处于可以游戏状态
is_playing = True


for level in range(1,total_levels + 1):
    print(f"******第{level}关******")
    if level == 1:
        question, answer = ques1, ans1
    elif level == 2:
        question, answer = ques2, ans2
    else :
        question, answer = ques3, ans3
    user_input = input(question)
    if user_input == answer:
        print("回答正确")
    elif user_input == '':
        print("输入不能为空，请重新作答")
    elif user_input == 'q':
        print("您已退出游戏")
    else :
        print("回答错误，还有几次机会")
