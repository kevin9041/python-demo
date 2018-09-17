# 继承

class Animal:
    def run(self):
        print('动物会跑~~~')

    def sleep(self):
        print('动物睡觉~~~')

class Dog(Animal):
    def bark(self):
        print('汪汪汪~~~') 

    def run(self):
        print('狗跑~~~~')    

class Hashiqi(Dog):
    def fan_sha(self):
        print('我是一只傻傻的哈士奇') 

# 在创建类时，如果省略了父类，则默认父类为object
#   object是所有类的父类，所有类都继承自object
class Person(object):
    pass

# issubclass() 检查一个[类]是否是[另一个类]的[子类]
print(issubclass(Animal , Dog))
print(issubclass(Animal , object))
print(issubclass(Person , object))

# isinstance()用来检查一个[对象]是否是一个[类]的[实例]
#   如果这个类是这个对象的父类，也会返回True
#   所有的对象都是object的实例
d = Dog()
h = Hashiqi()
print(isinstance(print , object)) #True
print(isinstance(d , Dog)) # True
print(isinstance(d , Animal)) # True