
n = 1
while n<=10:
    print("hello")
    n+=1



print("回答正确问题逃出密室")
riddle = "你是什么人"
answer = "你的心上人"
guess = input("请输入你的答案：")
while guess != answer:
    print("你的答案猜错了")
    guess = input("请输入你的答案：")
print("结果正确，恭喜！！！")