score_list = [65,50,25,66,84,94]

index = 0
while index < len(score_list):
    print(score_list[index])
    index += 1



#写法1
for item in score_list:
    print(item)


#写法2
for index in range(len(score_list)):
    print(score_list[index])