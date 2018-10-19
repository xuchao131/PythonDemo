# -*- coding:UTF-8 -*-
'''
Created on 2018年10月18日

@author: bingw
'''
#引入包或函数
from PythonUtils.AbsTest import myAbs
from _collections_abc import Iterable

#输出字符串
print ("你好，世界");
#声明一个list列表
names = ["张三","李四","王五"];
#输出列表长度
print (len(names));
#输出列表中指定的元素
print(names[1]);
#向列表中追加元素
names.append('赵六');
#输出列表中所有元素
print(names);
#通过for循环来输出列表元素
for name in names:
    print (name);
#声明一个不可变的列表tuple    
age = (23,22,34,56);
#输出tuple中的元素
print(age);
#if判断语句
if age[0]==21:
    print("第一个元素是23");
else:
    print("不存在");
#定义变量    
num = 0;
#range（101）函数表示循环的列表内容是0到100
for item in range(101):
    num = num + item;
#输出0到100的相加总和
print (num);
#声明一个dict（key,value形式存储元素）
user = {"name":"张三","age":23,"sex":"男"};
#输出dict中指定key的value值
print(user["sex"]);
#使用get函数通过key获取value
print(user.get("age"));
#内置函数abs用来去绝对值
print(abs(-19));
#内置函数max用来去最大值
print(max(1,2));
#调用引入的自定义函数myAbs
print(myAbs(-25));
#自定义函数power计算x的n次方
def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
#输出5的2次方
print(power(5, 2));
#切片，输出names列表中前1个元素，0是起始索引，1是前1个元素，类似substring
print(names[0:1]);
#切片，输出names列表中倒数第二个元素，-1是倒数第一个
print(names[-2:-1]);
#迭代dict中的key和value值并输出
for k,v in user.items():
    print(k,v);
#输出user是否能进行迭代    
print(isinstance(user, Iterable));