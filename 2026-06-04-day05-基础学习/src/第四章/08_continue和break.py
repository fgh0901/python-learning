for day in range(0,5):
    print(f"现在是第{day}天")
    print("吃饭")
    for num in range(1,4):
        print(f"面包{num}")
        if num == 2:
            break
            print("牛奶")
    print("sleep")