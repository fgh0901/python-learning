#默认值参数必须放在必选的参数后面
# 某个形参一旦设置了默认值，那么他之后的所有参数都需要设置默认值
def greet(name, age, height = 180):
    print(f"我是{name},我{age}岁了，我身高{height}")

greet('张三',15)