
def welcome(n):
    print("hello world")
    if n > 1:
        welcome(n-1)
welcome(5)



#求阶乘
def factorial(n):
    """递归调用函数，实现阶乘求结果"""
    if n > 1:
        return n * factorial(n-1)
    return n

print(factorial(5))
