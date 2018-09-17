# 多态

# 定义两个类
class A:
    def __init__(self,name):
        self._name = name

    @property
    def name(self):
        return self._name
        
    @name.setter
    def name(self,name):
        self._name = name   

class B:
    def __init__(self,name):
        self._name = name

    def __len__(self):
        return 10

    @property
    def name(self):
        return self._name
        
    @name.setter
    def name(self,name):
        self._name = name   

class C:
    pass


a = A('孙悟空')
b = B('猪八戒')
c = C()

# 定义一个函数
# 对于say_hello()这个函数来说，只要对象中含有name属性，它就可以作为参数传递
#   这个函数并不会考虑对象的类型，只要有name属性即可
def say_hello(obj):
    print('你好 %s'%obj.name)

# 在say_hello_2中我们做了一个类型检查，也就是只有obj是A类型的对象时，才可以正常使用，违反了多态 isinstance()这种函数，在开发中一般是不会使用的！
def say_hello_2(obj):
    # 做类型检查
    if isinstance(obj , A):
        print('你好 %s'%obj.name)    

# len()
# 之所以一个对象能通过len()来获取长度，是因为对象中具有一个特殊方法__len__
# 换句话说，只要对象中具有__len__特殊方法，就可以通过len()来获取它的长度
l = [1,2,3]
s = 'hello'

# print(len(l))
# print(len(s))
print(len(b))
print(len(c))
