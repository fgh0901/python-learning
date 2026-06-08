#新增，在列表尾追加一个元素
#列表.append（）
nums = [10,20,30,41]

nums.append(50)

print(nums)
#在指定下标处插入一个元素
#列表.insert（）

nums.insert(0,50)
print(nums)



#方式3，通过extend方法，将可迭代对象内容依次取出，放入列表尾
nums.extend(['nihao','world'])
nums.extend('nihao')
nums.extend(range(1,4))
print(nums)



#删除
#方式1：列表.pop（下标），删除指定的元素，并将删除掉的元素返回
nums.pop(0)
print(nums)


#方式2：删除列表中第一次出现的指定值。语法：列表.remove（值）
nums.remove(10)
print(nums)

#方式3：删除列表的所有元素
#语法：列表.clear()

nums.clear()

#方式4：删除指定位置的元素  del 列表[下标]