
# 用户输入的都是字符串，要进行数学运算必须进行数据类型转换
result1 = str(18)
result2 = str(75.6)
result3 = str(1.8e3)
result4 = str(12_000)
print(type(result1),result1)
print(type(result2),result2)
print(type(result3),result3)
print(type(result4),result4)


result5 = int(18)
result6 = int("79")
result7 = int("   555    ")
result8 = int(12_000)
print(type(result5),result5)
print(type(result6),result6)
print(type(result7),result7)
print(type(result8),result8)