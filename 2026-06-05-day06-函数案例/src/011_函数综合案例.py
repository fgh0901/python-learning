
def my_sum(*nums):#*nums代表可变参数，可以接受任意数量的位置参数
    return sum(nums)

def my_avg(total,days = 7):
    return total/days

def check_success(total,goal):
    if total >= goal:
        return True
    else :
        return False


def main(title,duration):
    print(f"{title}:仰卧起坐{duration}天挑战赛，请输入每天数量")
    num1 = int(input("第1天:"))
    num2 = int(input("第2天:"))
    num3 = int(input("第3天:"))
    num4 = int(input("第4天:"))
    num5 = int(input("第5天:"))
    num6 = int(input("第6天:"))
    num7 = int(input("第7天:"))
    total = my_sum(num1,num2,num3,num4,num5,num6,num7)
    avg = int(my_avg(total))
    print(f"平均每天{avg}个仰卧起坐")
    if check_success(total,50):
        return "挑战成功"
    else:
        return "挑战失败"


print(main('仰卧起坐',7))