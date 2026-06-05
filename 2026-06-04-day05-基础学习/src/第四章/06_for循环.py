#range 范围为左闭右开
for n in range(0,10):
    print(n)

for m in "abcdef":
    print(m)




text = input("请输入：")
secret = ''

for t in text:
    unicode = ord(t)
    secret += chr(unicode + 1)
print(f"加密后的内容为{secret}")

answer = ''
for t in secret:
    unicode = ord(t)
    answer += chr(unicode -1)
print(f"解密后的内容为：{answer}")