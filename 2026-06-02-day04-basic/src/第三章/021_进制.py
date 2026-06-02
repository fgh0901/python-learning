#0b开头表示二进制
num1 = 0b11001

#0o开头表示8进制
num2 = 0o1034

#ox开头表示十六进制
num3 = 0x1cf

#python中所有非十进制数字，打印时会转为10进制
print(bin(num1),num2,num3)

#bin()    将十进制数转为二进制字符串
#oct()    将十进制数转为八进制字符串
#hex()    将十进制数转为十六进制字符串




#使用int()将指定进制的数转为十进制数字
value1 = int('0b11001',2)
value2 = int('0o1034',8)
value3 = int('0x1cf',16)