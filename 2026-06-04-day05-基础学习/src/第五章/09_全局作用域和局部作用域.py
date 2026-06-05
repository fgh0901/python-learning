a = 100
b = 200

def test():
    c = 'nihao'
    d = 'hello'
    global a
    a = 300
    print("函数中打印（a）",a)
    print("函数中打印（b）",b)
    print("函数中打印（c）",c)
    print("函数中打印（d）",d)

test()
print("全局打印（a）",a)
print("全局打印（b）",b)