#定义函数时，在形参前加上*，可以接受任意数量的位置参数，并打包成一个元组
def test1(*args):
    print(args)

test1('我',1,5,6)


#定义函数时，在形参前加上**，可以接受任意数量的关键字参数，打包成一个字典
def test2(**kwargs):
    print(kwargs)

test2(name = '张三',gender = 'man', age = 18, height = 180)
