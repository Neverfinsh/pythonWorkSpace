#循环的计算for循环的使用
names=['Micheal','Bob','Jack']
for name in names:#记得打冒号
    print(name);

sum=0
for x  in [1,3,4,5,]:
    sum=sum+x
    print(sum)

#for循环的函数怎么写
print("for循环加range函数的使用")
sum=0;
for x  in range(10):
    sum=sum+x
    print(sum)

#for循环加while条件循环
sum=0
n=99
while n>0:
    sum=sum+n
    n=n-2
    print(sum)
#练习题,循环打印hello

names=['刘武','刘波','刘坤']

for name in names:
    print("Hello "+name)




