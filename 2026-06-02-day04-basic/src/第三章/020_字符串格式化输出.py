name = '张三'
gender = 'man'
weight = 65.2
age = 12

# 写法一：直接用+拼接，写起来麻烦且代码混乱，而且只能是字符串类型进行拼接
info = '我叫' + name + ',我是' + gender + '我的年龄是'
# print(info)

# 写法2：使用占位符
info2 = '我叫%s,我是%s,我的年龄是%i,我的体重是%f' % (name,gender,age,weight)
print(info2)

#写法3：使用f-string,会将所有嵌入的内容同意转化为字符串，因此不用担心数据类型的问题
info3 = f"我叫{name}，我是{gender}，我的体重是{weight}，年龄是{age}"
print(info3)
