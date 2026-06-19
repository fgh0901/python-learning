try:
    print("may error")
    n = int(input("请输入一个数字"))
    n = 5/n
    print(n)

except ZeroDivisionError as e:
    print("除数不能为0")
    print(e)
except:
    print("请输入数字")

else:#运行不报错，没有进入except会进入else模块，是可选的
    print()

finally:#无论如何都会执行的模块
    print()