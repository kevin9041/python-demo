

# 递归
#   它的整体思想是，将一个大问题分解为一个个的小问题，直到问题无法分解时，再去解决问题
# 递归式函数的两个要件
#   1.基线条件
#       - 问题可以被分解为的最小问题，当满足基线条件时，递归就不在执行了
#   2.递归条件
#       - 将问题继续分解的条件

def factorial(n):
    '''
        该函数用来求任意数的阶乘

        参数：
            n 要求阶乘的数字
    '''
    # 基线条件 判断n是否为1，如果为1则此时不能再继续递归
    if n == 1 :
        # 1的阶乘就是1，直接返回1
        return 1
    # 递归条件    
    return n * factorial(n-1)

# print(factorial(10))

# 练习
#   创建一个函数 power 来为任意数字做幂运算 n ** i
def power(n , i):
    '''
        power()用来为任意的数字做幂运算

        参数：
            n 要做幂运算的数字
            i 做幂运算的次数
    '''
    # 基线条件
    if i == 1:
        # 求1次幂
        return n
    # 递归条件
    return n * power(n , i-1)

# print(power(8,6))    



#   
# 练习
#   创建一个函数，用来检查一个任意的字符串是否是回文字符串，如果是返回True，否则返回False
#   回文字符串，字符串从前往后念和从后往前念是一样的
#       abcba
#   abcdefgfedcba
#   先检查第一个字符和最后一个字符是否一致，如果不一致则不是回文字符串
#       如果一致，则看剩余的部分是否是回文字符串
#   检查 abcdefgfedcba 是不是回文
#   检查 bcdefgfedcb 是不是回文
#   检查 cdefgfedc 是不是回文
#   检查 defgfed 是不是回文
#   检查 efgfe 是不是回文
#   检查 fgf 是不是回文
#   检查 g 是不是回文

def hui_wen(s):
    '''
        该函数用来检查指定的字符串是否回文字符串，如果是返回True，否则返回False

        参数：
            s：就是要检查的字符串
    '''
    # 基线条件
    if len(s) < 2 :
        # 字符串的长度小于2，则字符串一定是回文
        return True
    elif s[0] != s[-1]:
        # 第一个字符和最后一个字符不相等，不是回文字符串
        return False    
    # 递归条件    
    return hui_wen(s[1:-1])

# def hui_wen(s):
#     '''
#         该函数用来检查指定的字符串是否回文字符串，如果是返回True，否则返回False

#         参数：
#             s：就是要检查的字符串
#     '''
#     # 基线条件
#     if len(s) < 2 :
#         # 字符串的长度小于2，则字符串一定是回文
#         return True
#     # 递归条件    
#     return s[0] == s[-1] and hui_wen(s[1:-1])

print(hui_wen('abcdefgfedcba'))    

