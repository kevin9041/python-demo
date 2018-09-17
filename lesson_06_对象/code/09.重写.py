# 继承

# 定义一个类 Animal（动物）
#   这个类中需要两个方法：run() sleep() 
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
        
# 当我们调用一个对象的方法时，
#   会优先去当前对象中寻找是否具有该方法，如果有则直接调用
#   如果没有，则去当前对象的父类中寻找，如果父类中有则直接调用父类中的方法，
#   如果没有，则去父类的父类中寻找，以此类推，直到找到object，如果依然没有找到，则报错
class A(object):
    def test(self):
        print('AAA')

class B(A):
    def test(self):
        print('BBB')

class C(B):
    def test(self):
        print('CCC')   

# 创建一个c的实例
c = C()
c.test()

