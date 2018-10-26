# -*- coding:UTF-8 -*-
'''
Created on 2018年10月23日

@author: bingw
'''
import logging
from _io import StringIO
import os
import pickle
import json
from multiprocessing import Process
import re
from datetime import datetime, timedelta
logging.basicConfig(level=logging.INFO)

#定义Student类并继承Object
class Student(object):
    #定义初始化方法，包含__name属性和__age属性，使用__开头可以私有化属性
    def __init__(self,name,age):
        self.__name = name;
        self.__age = age;
    #属性私有化后要通过get和set来获取和设置    
    def set_age(self,age):
        self.__age = age;
        
    def set_name(self,name):
        self.__name = name;
        
    def get_age(self):
        return self.__age;
    
    def get_name(self):
        return self.__name;
    
    #Python内置的@property装饰器就是负责把一个方法变成属性调用的
    @property
    def name(self):
        return self.__name;
    '''@property本身创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值，
                    这样实例就可以直接通过.name来设置和获取属性值，不需要再通过set_name和get_name了'''
    @name.setter
    def name(self,value):
        self.__name = value;

class Aniaml(object):
    #定义一个特殊的__slots__变量，来限制该class实例能添加的属性，但仅对当前类实例起作用，对继承的子类是不起作用的
    __slots__=('name','sex');
    def run(self):
        print("animal is running...");
        
animal = Aniaml();
animal.run();

class Dog(Aniaml):
    def run(self):
        print("dog is running...");

dog = Dog();
dog.run();
#通过type()函数创建出Hello类,先定义函数，再创建hello类
def fn(self,name='world'):
    print('hello,%s'% name);
Hello = type('Hello',(object,),dict(hello=fn))#第一个参数类名称，第二个参数所继承的父类，第三个参数把函数fn绑定到方法名hello上
h = Hello();
h.hello();
#使用try...except...finally...的错误处理机制
try:
    r = 10/0;
    print(r);
except Exception as e:
    logging.exception(e);#logging模块可以非常容易地记录错误信息
    #print(e);
finally:
    print('finally');
print('END');
'''用open函数打开一个文件并读取内容,参数r表示读取，如果读取图片，视频等二进制文件则改为'rb'即可，读取非UTF-8编码的文本文件，
        需要给open()函数传入encoding参数，如f = open('/gitTest.txt','r',encoding='gbk')，
        遇到编码错误后如何处理。最简单的方式是直接忽略，可以加上参数(errors='ignore')。
        写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件。
        以'w'模式写入文件时，如果文件已存在，会直接覆盖，如果追加内容到文件末尾可以传入'a'以追加（append）模式写入'''
try:
    f = open('C:/Users/bingw/Desktop/mygit/gitTest.txt','r');
    print(f.read());#如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用read(size)比较保险；如果是配置文件，调用readlines()最方便
finally:
    if f:
        f.close();
#with语句来自动帮我们调用close()方法
with open('C:/Users/bingw/Desktop/mygit/gitTest.txt','r') as f:
    print(f.read());
#使用readlines函数读取文件内容
with open('C:/Users/bingw/Desktop/mygit/gitTest.txt','r') as f:
    for line in f.readlines():
        print(line.strip());
#StringIO在内存中读写str，如果要操作二进制数据，就需要使用BytesIO，方法和StringIO类似
s = StringIO();
s.write('hello');
print(s.getvalue());
#读取StringIO
f = StringIO('hello,world');
while True:
    str1 = f.readline();
    if str1 == '':
        break;
    print(str1.strip());
#os模块的基本功能
print(os.name);#操作系统类型，如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统
print(os.environ);#查看环境变量
print(os.environ.get('JAVA_HOME'));#获取某个环境变量的值
print(os.path.abspath('.'));#查看当前目录的绝对路径
'''在某个目录下创建一个新目录，首先把新目录的完整路径表示出来；
   os.path.split()用来拆分路径；os.path.splitext()可以直接让你得到文件扩展名'''
print(os.path.join('E:/','testdir'));
#os.mkdir('E:/testdir');#创建一个目录
#os.rmdir('E:/testdir');#删除一个目录
#os.rename('1.txt', '2.txt')#对文件重命名
#os.remove('1.txt')#删除文件
#pickle模块用来实现序列化
d = dict(name='小明',age=23);
print(pickle.dumps(d));#pickle.dumps()方法把任意对象序列化成一个bytes，就可以把这个bytes写入文件
#pickle.dump()直接把对象序列化后写入一个file-like Object
#f = open('1.txt', 'wb');
#pickle.dump(d, f);
#f.close();
#当把对象从磁盘读到内存时，可以用pickle.loads()方法反序列化出对象，也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象
#f = open('1.txt', 'rb');
#d = pickle.load(f);
#f.close();
print(json.dumps(d));#把Python对象变成一个JSON
#把JSON反序列化为Python对象，用loads()或者对应的load()方法，前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化
print(json.loads(json.dumps(d)));
'''（进程和线程这块不太清楚）创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动，
   join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步'''
#子进程要执行的代码
def run_proc(name):
    print('Run Child Process %s (%s)' % (name,os.getpid()));
if __name__=='__main__':
    print('Parent Process %s' % os.getpid());
    p = Process(target=run_proc,args=('test',));
    print('Child process will start.');
    p.start();
    p.join();
    print('Child process end.');
'''正则表达式：用\d可以匹配一个数字，用\w可以匹配一个字母或数字，用.可以匹配任意字符，用*表示任意个字符（包括0个），
       用+表示至少一个字符，用?表示0个或1个字符，用{n}表示n个字符，用{n,m}表示n-m个字符，用\s可以匹配一个空格（包括Tab等空白符），
   (A|B)可以匹配A或B，^表示行的开头，^\d表示必须以数字开头，$表示行的结束，\d$表示必须以数字结束，
   re.match(r'正则表达式', '要匹配的字符串')用来判断是否匹配，r可以替代转义符“\”，[]可以表示范围'''
test = '123@126.com';
if re.match(r'^[0-9a-zA-Z]+@[0-9a-zA-Z]+.(com|cn|com.cn)$',test):
    print('ok');
else:
    print('failed');
#re.split(r'[\s\,]+', 'a,b, c  d')用来切割字符串
#用()表示要提取的分组（Group），如：^(\d{3})-(\d{3,8})$分别定义了两个组，可以直接从匹配的字符串中提取出区号和本地号码
m = re.match(r'^(\d{3})-(\d{3,8})$','010-123456');
print(m.group(0));#group(0)永远是原始字符串，group(1)表示第1个字符串
print(m.group(1));
print(m.group(2));
#出于效率的考虑，我们可以预编译该正则表达式，在重复使用时就不需要编译这个步骤了
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$');
re_telephone.match('010-12345').groups();
#获取当前日期和时间
nowTime = datetime.now();
print(nowTime);
#把datetime转换为timestamp
print(nowTime.timestamp());
#把timestamp转换为datetime
t = nowTime.timestamp();
print(datetime.fromtimestamp(t));
#timestamp也可以直接被转换到UTC标准时区的时间
print(datetime.utcfromtimestamp(t));
#把str转换为datetime
strDate = datetime.strptime('2018-10-26 03:45:42','%Y-%m-%d %H:%M:%S');
print(strDate);
#把datetime转换为str
print(nowTime.strftime('%Y-%m-%d %H:%M:%S'));
#datetime加减需要导入timedelta类
print(nowTime + timedelta(hours=10));
print(nowTime - timedelta(days=1));