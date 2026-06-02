#and 用于判断两侧的值，是否都为true
print(True and True)
print(True and False)
print(False and False)
#and返回的不一定是布尔值，它返回的是某个参与计算的值本身
#规则：and会先看左边，如果左边为假，就直接返回左边，否则返回右边
#备注：若参与and运算的值不是布尔值，那么python会自动转为布尔值，然后在进行逻辑操作
print(2-2 and True)
print('' and True)
print(True and 8/2)
print(3+3 and 3*4)

#or 返回的也不一定是布尔值，它返回的是参与计算的值本身
#规则：or会先看左边，左边为真，就直接返回左边，否则返回右边
#备注：若参与or运算的值不是布尔值，那么python会自动转化为布尔值，然后在进行逻辑操作
print(7-2 or False)
print('你好' or '尚硅谷')
print(False or 8/2)
print(2-2 or 3*4)


#no用于取反
#not返回的值，一定是布尔值
print(not True)
print(not False)