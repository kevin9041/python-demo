a = int(10) # 创建一个int类的实例
b = str('hello') # 创建一个str类的实例

# print(a , type(a))
# print(b , type(b))

# 定义一个简单的类
class MyClass():
    pass

# print(MyClass)
# 创建一个对象
mc = MyClass() 

# isinstance()用来检查一个对象是否是一个类的实例
result = isinstance(mc,MyClass)
result = isinstance(mc,str)

# print(MyClass , id(MyClass),type(MyClass))
# print(mc , id(mc),type(mc))

# 可以向对象中添加变量，对象中的变量称为属性
# 语法：对象.属性名 = 属性值
mc.name = '孙悟空'
print(mc.name)
