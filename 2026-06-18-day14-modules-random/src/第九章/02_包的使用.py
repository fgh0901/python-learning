#包是python模块的一种组织形式，将多个模块组合在一起，形成一个大的python工具库。
#包同通常是一个拥有__init__.py文件的目录，它定义了包的属性和方法
from my_package import my_math,my_card
result = my_math.total(1,2,3)
print(result)
my_card.menu()