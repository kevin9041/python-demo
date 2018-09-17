
# def test2():
#     print('这是主模块中的test2')  #如果主模块定义的变量和引入模块变量重复，依照循序加载生效，即先引入后定义还是先定义后引入都是后者生效

# 也可以只引入模块中的部分内容
# 语法 from 模块名 import 变量,变量....
# from m import Person
# from m import test
# from m import Person,test
# from m import * # 引入到模块中所有内容，一般不会使用

# p1 = Person()
# print(p1)
# test()
# test2()

# 可以为引入的变量使用别名
# 语法：from 模块名 import 变量 as 别名
# from m import test2 #as new_test2   #起别名以区分主模块和引入模块同变量名
from m import test2 as new_test2 

def test2():
    print('这是主模块中的test2')

test2()
new_test2()