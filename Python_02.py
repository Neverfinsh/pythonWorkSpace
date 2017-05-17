
# python的编码问题
print("py中文输出整数的编码")
print(ord("A"));
print(ord("我"));
print(ord("爱"));
print(ord("你"));

#py 把整数转换成字符串

print(chr(97));

# py求字符串的长度问题,使用的是Unicode的编码方式。中文只占一个字节。
# py在保存中文是必须要添加utf-8的头文件

print(len('aaa'));
print(len("爱"));

# py  list集合中使用;有序,可以重复
listview=['a','b','c']
print(listview);
listview.append("d");#追加的对象；
listview.append("a");
print(listview);


# list中用俩个list中情况；
listview2=['a',['a','b','c'],'c'];
print("---------------")
print(listview2);
print(listview2[1][1]);#可以用二维数组进行访问；
print("测试list的长度")
print(len(listview2));
print(listview2.pop(-1));#-1表示最后一个
print(listview2);#没有了c的长度；

#作业
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])


#py判断语句的作用；

age=input("请输入年龄");
iage=int(age);
if iage<10:
     print("小学");
elif 10<iage<18:
    print("高中");
elif iage>18:
    print("大学");
else:
    print("毕业或者辍学");

