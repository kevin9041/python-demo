# 尝试定义一个表示人的类
class Person :
    # 类中的属性和方法，所有实例都可以访问，而且在类中定义的属性一定要初始化！
    name = 'swk' 

    def say_hello(self) :
        # 方法每次被调用时，解析器都会自动传递第一个实参，即调用方法的对象本身self
        #  区别于java，在方法中不能直接访问类中的属性！
        print('你好！我是 %s' %self.name)

# 创建Person的实例
p1 = Person()
p2 = Person()

print("===========>实例化对象后，默认都采用类属性")
print(p1.name)
print(p2.name)

print("===========>修改p1,p2的name属性")
p1.name = '猪八戒'
p2.name = '沙和尚'

p1.say_hello() # '你好！我是 猪八戒'
p2.say_hello() # '你好！我是 沙和尚'

print("===========>删除p1的name属性后就采用类中的属性值了")
del p1.name # 删除p1的name属性后就采用类中的属性值了

print(p1.name) 
print(p2.name) 
