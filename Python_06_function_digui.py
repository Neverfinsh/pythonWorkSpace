#递归函数的定义
print("函数的递归使用")

def test(x):

    if(x==1):
        return  1
    else:
        return  x * test(x-1)


num1=input("请输入递归的函数")#输入的是正数
num=int(num1);
result=test(num);
print(result);


#作业
L=[];
n=1;
while n<99:
    L.append(n);
    n=n+2;

    print("输出一个奇数的列表");#不同的类型不在一起使用
    print(L)