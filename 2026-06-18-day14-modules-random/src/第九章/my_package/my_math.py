auther = 'woziji'

def add(a,b):
    return a+b

def total(*a):
    '''

    :param a: 接收一个列表
    :return: 返回a列表中个元素的平方和
    '''
    result = 0
    for i in a:
        result = result + i**2
    return result