#函数的编程
#  1.  变量可以指向一个函数
#  2.  函数的参数是可以是一个函数

#x=abs(-10)
#rint("函数编程之高阶函数");
#print(x);

#print("用一个变量指向一个函数")
#f=abs
#print(f(-10));


# 函数的参数的可以是一个函数的参数
  x=5
  y=6
  f=abs
def add(x, y, z):
    return  f(x) + f(y)
print(add(5,6,abs))