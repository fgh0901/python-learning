from logging import exception
try:
    pwd = input("请输入密码")
    if len(pwd)<8:
        raise Exception('密码长度不够')#手动抛出异常
except Exception as e:
    print(e)