# help()是Python中的内置函数
# 通过help()函数可以查询python中的函数的用法
# 语法：help(print) # 获取print()函数的使用说明

# 文档字符串（doc str）
# 在定义函数时，可以在函数内部编写文档字符串，文档字符串就是函数的说明
def fn(a:int,b:bool,c:str='hello') -> int:
    '''
    这是一个文档字符串的示例

    函数的作用：。。。。。
    函数的参数：
        a，作用，类型，默认值。。。。
        b，作用，类型，默认值。。。。
        c，作用，类型，默认值。。。。
    '''
    return 10

help(fn)
