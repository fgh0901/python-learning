
users = [
    {'name':'xiaohong','password':'123','status':True},
    {'name':'mia','password':'46','status':True},
    {'name':'jack','password':'789','status':False}
]

for j in range(3):
    user = input("请输入用户名")
    pwd = input("请输入你的密码")
    flag = False
    #for  else写法，如果内层break执行过，不进else，否则进入else
    for i in users:
        if user == i['name']:
            if pwd == i['password']:
                if i['status']:
                    print("success login in")
                    flag = True
                    break
                else:
                    print("false")
            else:
                print("密码错误")
            break
    else:
        print("用户名不存在")
    if flag:
        break