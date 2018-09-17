
class A:
    def __init__(self):
        self.name = 'A类'

    # del是一个特殊方法，它会在对象被垃圾回收前调用
    def __del__(self):
        print('A()对象被删除了~~~',self)

a = A()
b = a # 又使用一个变量b，来引用a对应的对象

print(a.name)

a = None # 将a设置为了None，此时没有任何的变量对A()对象进行引用，它就是变成了垃圾
b = None

# del a
# del b

input('回车键退出...')
