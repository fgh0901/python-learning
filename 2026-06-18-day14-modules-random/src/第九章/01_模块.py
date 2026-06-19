from 第九章.my_package import my_module

result = my_module.add(3, 4)
print(result)
print(my_module.auther)


#从模块中导入特定的函数
from 第九章.my_package.my_module import total
#from my_module import total as f  将从模块中导入的函数重命名，防止重名
result = total([1,2,3,4])
print(result)
