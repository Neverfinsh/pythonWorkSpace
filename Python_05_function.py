#python的使用就是熟悉一些函数的使用方法

# print("输入俩个数比较大小")
# a=input("输入一个数");
# b=input("输入另一个数");
# c=max(a,b)
# print("俩个数中最大的一个数是："+c);


#字符串转整数的实例
print(int ('123'))

# 自定函数;带有参数的
def my_class(x):
    if x>0:
        return x
    else:
        return -x

print("参数为负数")
print(my_class(-1))
print("参数为正数")
print(my_class(3))


#关键字的是def 进行 赋值。

# def nop():
 # pass

# print("测试一个空函数"+nop())


# 自定义函数的def
def my_class2(x):
    return x*x
print("调用一个含参的函数")
print(my_class2(5))

# 调用俩个含参的自定义函数

def myfunction3(a,b):#a表示想，b表示乘以几次
    s=1
    while b>0:
          b=b -1#n--的方法
          s=s*a
    return s
print("自定义的的一个方法")
print(myfunction3(3,4))






