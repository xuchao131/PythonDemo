# -*- coding:UTF-8 -*-
'''
Created on 2018年10月18日

@author: bingw
'''
#引入包或函数
from PythonUtils.AbsTest import myAbs
from typing import Iterable
import os
from PythonTest.Student import Student
from PythonTest.Student import Aniaml
from PythonUtils.EnumTest import Weekday


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
user = {"name":"张三","age":"23","sex":"男"};
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
#运用列表生成式列出指定目录下的所有文件和目录名
print([d for d in os.listdir('E:\workspaces\PythonDemo')]);
#运用列表生成式迭代出dict中的键值对
print([k+'='+v for k,v in user.items()]);
#使用内置函数isinstance判断变量是不是字符串
print(isinstance(num, str));
#生成器generator是将列表生成式的[]改成()
generator_test = (x*x for x in range(11));
#输出生成器generator中的每一个元素的方式是for循环
for i in generator_test:
    print(i);
#一个变量指向一个函数，通过该变量来调用这个函数
f=abs;
print(f(-20));
#一个函数接收另一个函数作为参数，这种函数称为高阶函数
def add(x,y,f):
    return f(x)+f(y);
x=1;
y=-2;
f=abs;
print(add(x,y,f));
#map()函数接收两个参数，一个是函数，一个是Iterable
def f(x):
    return x*x;
r = map(f,[1,2,3,4,5,6,7]);
print(list(r));
#filter()也接收一个函数和一个序列，把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素
def is_odd(n):
    return n % 2 == 1;
print(list(filter(is_odd,[1,3,5,6,8,2])));
#sorted()函数就可以对list进行排序
print(sorted([-20,-4,2,1,7,-10]));
#sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序
print(sorted([-20,-4,2,1,7,-10],key=abs));
#要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True
print(sorted([-20,-4,2,1,7,-10],key=abs,reverse=True));
#关键字lambda表示匿名函数，冒号前面的x表示函数参数
print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])));
#新建student实例
student = Student("lisi",33);
student.name = 'zhangshan';
print(student.name);
animal = Aniaml();
animal.name = 'dog';
animal.sex = 'man';
#因为Animal类设置了属性限制，所以设置age时会报错
#animal.age = 32;
print(animal.name);
print(animal.sex);
#访问枚举类Weekday
print(Weekday.Thu);
print(Weekday.Thu.value);