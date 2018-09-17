# 创建几个函数

def add(a , b):
    '''
        求任意两个数的和
    '''
    r = a + b
    return r


def mul(a , b):
    '''
        求任意两个数的积
    '''
    r = a * b
    return r    



# 希望函数可以在计算前，打印开始计算，计算结束后打印计算完毕
# 我们希望在不修改原函数的情况下，来对函数进行扩展 

def new_add(a,b):
    print('计算开始~~~')
    r = add(a,b)
    print('计算结束~~~')
    return r

# r = new_add(111,222)    
# print(r)

# 上边的方式，已经可以在不修改源代码的情况下对函数进行扩展了
#   但是，这种方式要求我们每扩展一个函数就要手动创建一个新的函数，实在是太麻烦了
#   为了解决这个问题，我们创建一个函数，让这个函数可以自动的帮助我们生产函数

def begin_end(old):
    '''
        用来对其他函数进行扩展，使其他函数可以在执行前打印开始执行，执行后打印执行结束

        参数：
            old 要扩展的函数对象
    '''
    # 创建一个新函数
    def new_function(*args , **kwargs):
        print('开始执行~~~~')
        # 调用被扩展的函数
        result = old(*args , **kwargs)
        print('执行结束~~~~')
        # 返回函数的执行结果
        return result

    # 返回新函数        
    return new_function

f2 = begin_end(add)
f3 = begin_end(mul)

# r = f2(123,456)
# r = f3(123,456)
# print(r)
# 向begin_end()这种函数我们就称它为装饰器
#   通过装饰器，可以在不修改原来函数的情况下来对函数进行扩展
#   在开发中，我们都是通过装饰器来扩展函数的功能的
# 在定义函数时，可以通过@装饰器，来使用指定的装饰器，来装饰当前的函数
#   可以同时为一个函数指定多个装饰器，这样函数将会安装从内向外的顺序被装饰 

def begin_end2(old):
    '''
        用来对其他函数进行扩展，使其他函数可以在执行前打印开始执行，执行后打印执行结束

        参数：
            old 要扩展的函数对象
    '''
    # 创建一个新函数
    def new_function(*args , **kwargs):
        print('begin_end2装饰~开始执行~~~~')
        # 调用被扩展的函数
        result = old(*args , **kwargs)
        print('begin_end2装饰~执行结束~~~~')
        # 返回函数的执行结果
        return result

    # 返回新函数        
    return new_function

@begin_end2
@begin_end
def say_hello():
    print('大家好~~~')

say_hello()
