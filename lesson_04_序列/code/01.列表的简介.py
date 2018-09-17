# 创建列表，通过[]来创建列表
my_list = [] # 创建了一个空列表
# print(my_list , type(my_list))

# 列表存储的数据，我们称为元素
# 一个列表中可以存储多个元素，也可以在创建列表时，来指定列表中的元素
my_list = [10] # 创建一个只包含一个元素的列表

# 当向列表中添加多个元素时，多个元素之间使用,隔开
my_list = [10,20,30,40,50]

# 列表中可以保存任意的对象
my_list = [10,'hello',True,None,[1,2,3],print]

# 列表中的对象都会按照插入的顺序存储到列表中，

# 如果使用的索引超过了最大的范围，会抛出异常
# print(my_list[5]) IndexError: list index out of range