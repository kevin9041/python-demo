# 可以在模块中定义变量，在模块中定义的变量，在引入模块后，就可以直接使用了
a = 10
b = 20

# 添加了_的【属性和方法】，只能在模块内部访问，在通过import * 引入时，不会引入_开头的变量
_c = 30

# 可以在模块中定义函数，同样可以通过模块访问到
def test():
    print('test')

def test2():
    print('test2')

# 也可以定义类    
class Person:
    def __init__(self):
        self.name = '孙悟空'

# 编写测试代码，这部分代码，只要当当前文件作为主模块的时候才需要执行
#   而当模块被其他模块引入时，__name__就是自身模块名而不是__main__ 
if __name__ == '__main__':
    test()
    test2()
    p = Person()
    print(p.name)