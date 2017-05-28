#从列表中取前几行的中
L=['a','b','c','d','e',]
print("要求输出前三个的值");
print(L[1],L[2]);


R=[];
n=3
for i in range(n):
 R.append(L[i]);
 print(R)
 #python的切片就是的截取

print(R[1:3])
print(" 切片中使用切片支持负数")
print(R[-1:])





