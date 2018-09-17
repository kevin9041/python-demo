# 元组 tuple
# 元组是一个不可变的序列
# 它的操作的方式基本上和列表是一致的 在操作元组时，就把元组当成是一个不可变的列表就ok了
# 一般当我们希望数据不改变时，就使用元组，其余情况都使用列表

# 创建元组
# 使用()来创建元组
my_tuple = () # 创建了一个空元组

my_tuple = (1,2,3,4,5) # 创建了一个5个元素的元组
# 元组是不可变对象，不能尝试为元组中的元素重新赋值或者新增
# my_tuple[3] = 10 TypeError: 'tuple' object does not support item assignment

# 当元组不是空元组时，括号可以省略
# 如果元组不是空元组，它里边至少要有一个,
my_tuple = 10,20,30,40
my_tuple = 40,
# print(my_tuple , type(my_tuple))

# 元组的解包（解构）
# 解包指就是将元组当中每一个元素都赋值给一个变量，变量的个数和元组中元素的个数要相等
# 也可以在变量前边添加一个*，这样变量将会获取元组中所有剩余的元素(list列表对象)
# 不能同时出现两个或以上的*变量
# *a , *b , c = my_tuple SyntaxError: two starred expressions in assignment
a,b,c,d = my_tuple
a , b , *c = my_tuple
a , *b , c = my_tuple
*a , b , c = my_tuple
a , b , *c = [1,2,3,4,5,6,7] #列表也可以解包
a , b , *c = 'hello world' #字符串也可以解包

a = 100
b = 300
# 交互a 和 b的值，这时我们就可以利用元组的解包
a , b = b , a #（相当于临时元组）