# 格式化字符串

# 字符串不能和其他的类型进行加法运算，如果做了会出现异常 TypeError: must be str, not int，如a = 'abc' + 123 
# print("a = "+a) 这种写法在Python中不常见，print('a =',a)取而代之

# 在创建字符串时，可以在字符串中指定占位符
# %s 在字符串中表示任意字符
# %f 浮点数占位符
# %d 整数占位符
b = 'Hello %s'%'孙悟空'
b = 'hello %s 你好 %s'%('tom','孙悟空')
b = 'hello %3.5s'%'abcdefg' # %3.5s字符串的长度限制在3-5之间
b = 'hello %s'%123.456
b = 'hello %.2f'%123.456
b = 'hello %d'%123.95
b = '呵呵'

# print('a = %s'%a)

# 格式化字符串，可以通过在字符串前添加一个f来创建一个格式化字符串
# 在格式化字符串中可以直接嵌入变量
c = f'hello {a} {b}'
