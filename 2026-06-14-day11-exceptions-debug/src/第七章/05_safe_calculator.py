print("这是一个计算机，请选择你需要的功能\n1.+\n2.*\n3./\n4.-")
try:#用于规定可能抛出异常的代码段
    n = input()
    if not n.isdigit():
        raise Exception("请输入一个数字")#raise用于抛出异常
    n = int(n)
    match n:
        case 1:
            n1 = int(input("请输入要加的数字1"))
            n2 = int(input("请输入要加的数字2"))
            print(n1+n2)
        case 2:
            n1 = int(input("请输入要*的数字1"))
            n2 = int(input("请输入要*的数字2"))
            print(n1 * n2)
        case 3:
            n1 = int(input("请输入要加的数字1"))
            n2 = int(input("请输入要加的数字2"))
            if n2 == 0:
                raise Exception("除数不能为0")
            print(n1 / n2)
        case 4:
            n1 = int(input("请输入要加的数字1"))
            n2 = int(input("请输入要加的数字2"))
            print(n1 - n2)

        case _:
            raise Exception("功能编号只能是1-4")

except Exception as e:
    print(e)