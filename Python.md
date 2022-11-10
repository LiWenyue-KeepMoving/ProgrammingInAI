# Python基础语法简述

### Some Tips

* 无法使用 pip：考虑关闭系统代理。

* 中文编码出错：在代码文件最前添加一行：

  ```python
  # -*-coding:GBK -*- 
  # -*-coding:utf-8 -*- 
  ```

* whl 文件在 pip 过程中若因文件名问题无法安装，直接修改为需要的文件名格式即可。使用 `python -m pip debug --verbose`命令查看需要的文件名格式。

* 手动下载完模块后记得使用 `pip install 文件名` 命令在 Scripts 文件夹中安装。























---

#### Input() 函数

* 功能：接受标准输入数据
* 语法格式：`input([prompt])` ，其中 prompt 为用户提示信息

###### 示例代码

```python
name = input(“Please input your name:”) #由此输出提示信息
a = int(input()) #强制类型转换，因为input()输出类型为 string，这样可使 a 参与计算
a = int(input("请输入同学" + str(name) + "的学号"))
d, e, f  = map(int, input('以逗号隔开：').split(","))
```

----

#### print() 函数

* 功能：用于打印输出

* 语法格式：`print ( *objects,  sep = ' ',  end = ' \n ',  file = sys.stdout )`

  参数具体含义如下：

  * objects   表示输出的对象，输出多个对象时，需要用 逗号 分隔
  * sep  用来间隔多个对象
  * end  用来设定以什么结尾，默认值是换行符 \n，可以换成其他字符
  * file  要写入的文件对象

###### 示例代码

```python
print('"有生命便有希望"')
print("'永不气馁! '") #单双引号可交替复用打出
print(a, b) #可以一次输出多个对象，对象之间用逗号分隔
print("www", "snh48", "com", sep = ".")  #设置间隔符
for x in range(0, 5):
    print(x, end = ' ') #设置结尾符
print('\n') #print() 自带一次换行，故此指令换行两次
#下面是一些格式化输出的示例
name = "逆境清醒"
print("我的名字是%s" % name)
age = 100
print("我的年龄是%d" % (age) + "岁")
i = 2.67145573
print("保留两位小数输出，设置宽度为8位，用0补足宽度，左对齐，加正负号%-+08.2f" % (i))
s = '逆境清醒'
x = len(s)
print('%s名字的长度是 %d' %(s,x)) #多个格式化参数
```

----

#### eval() 函数

* 功能：计算指定表达式的值。也就是说它要执行的Python代码只能是单个运算表达式（注意eval不支持任意形式的赋值操作），而不能是复杂的代码逻辑

* 语法格式：`eval ( expression, global = None, local = None )`

  参数具体含义如下：

  * expression  必选参数，可以是字符串，也可以是一个任意的 code 对象实例（可以通过 compile 函数创建）。如果它是一个字符串，它会被当作一个（使用 globals 和 locals 参数作为全局和本地命名空间的）Python 表达式进行分析和解释
  * globals  可选参数，表示全局命名空间（存放全局变量），如果被提供，则必须是一个字典对象
  * locals  可选参数，表示当前局部命名空间（存放局部变量），如果被提供，可以是任何映射对象。如果该参数被忽略，那么它将会取与globals 相同的值
  * 如果globals与locals都被忽略，那么它们将取 eval() 函数被调用环境下的全局命名空间和局部命名空间

###### 示例代码

```python
x = 10
y = 20
c = eval('x + y', {'x': 1,'y': 2}, {'y': 3,'z': 4})
d = eval('print(x,y)')
```

----

#### 数据类型：list

> 列表中可以包含多个元素，且元素类型可以不同
>
> 每一元素可以是任一数据类型，包括列表（即列表嵌套）及后面要介绍的元组、集合、字典
>
> 所有元素写在[]中，每两个元素间用逗号分隔
>
> 对于不包含任何元素的列表，即[]，称为空列表

```python
ls = [1,2.5,'test',3+4j,True,[3,1.63],5.3] #创建一个 list
ls = list((1,2,3)) # 根据元组创建列表对象，并赋值给 ls 变量
ls[2] = 2.2 #下标访问和修改
ls2 = ls[1:4] #获取子列表，并且可以用这种方式多项修改列表，如下：
ls[1:4] = [2,2,2]
```

> 在 Python 中，通过赋值运算实际上是将两个变量指向同一个对象。当通过一个变量修改对象中元素的值后，通过另一个变量访问对象时，访问到的元素也是修改后的值。
>
> 但如果使用元素截取方法，可以实现修改一个对象中的元素值不会影响另一个对象。
>
> ```python
> ls1=[1,2,3]
> ls2=ls1[:] #这是产生了一个新对象
> print(id(ls1),id(ls2)) #本质上是内存地址不同
> ```
>
> 可以直接使用深拷贝方法从根本上解决问题。copy 模块中的 deepcopy 函数可以全面地复制一份原对象的副本。
>
> ```python
> import copy
> ls1=[1,[2,3]]
> ls2=copy.deepcopy(ls1) 
> ```

> 以下是列表的一些简单操作。
>
> ```python
> #查找 ls 中第一个值为 x 的位置
> ls.index(3)
> #将元素插入列表指定位置
> ls.insert(index, x)
> #列表最后添加元素
> ls.append(x)
> #在列表中删除元素
> del ls[8] #删除下标为 8 的元素
> ls[1:6]=[] #将 ls 中下标 1 至 5 的元素删除
> #获取最大元素和最小元素
> max(ls)
> min(ls)
> #统计 x 在列表中出现的次数
> ls.count(x)
> #列表中元素数量
> len(ls)
> ```

###### 列表元素排序

> 使用 sort 方法可对列表中的元素按指定规则排序。
>
> 语法格式：`ls.sort(key = None, reverse =  False)`
>
> 其中 key 接受一个函数，通过此函数获取用于排序时比较大小的数据，reverse 用于指定按升序（False，默认值）还是按降序（True）排列。
>
> ```python
> def GetStuSno(stu):
>     return stu.sno
> ls1 = [23,56,12,37,28]
> ls1.sort()
> ls1.sort(reverse = True)
> ls2 =[Student('1810101','a'),Student('1810100','b'),Student('1810102','c')]
> ls2.sort(key = lambda stu:stu.sno, reverse = True)
> ls2.sort(key = GetStuSno, reverse = True) 
> ```

---

#### 数据类型：Tuple

> Tuple元组是一个有序且不可更改的集合
>
> 元组和列表类似，可以包含多个不同类型的元素，同样用逗号分隔
>
> 与列表不同的是，元组中的元素写在小括号中，==且元组中的元素不能修改 (字符串也是这样）==
>
> 对于不含任何元素的元素即 ()，称为空元组
>
> ```python
> #根据列表创建元组对象
> t1 = tuple([1,2,3])
> #单元素元组创建要加逗号
> t2 = (15,)
> #拼接生成新元组
> t3 = t1 + t2
> #元组最大最小元素
> max(t1)
> max(t2)
> ```

---

#### 数据类型：Set

> 与元组和列表类似，Set  (集合) 中同样可以包含多个不同类型的元素， 但集合中的各元素==无序==、==不允许有相同元素==且元素必须是==可哈希== (hashable) 的对象
>
> 可哈希对象是指拥有 \__hash__(self) 内置函数的对象，可以计算哈希值且可与其他对象比较是否相等的对象。列表、集合和字典类型的数据不是可哈希对象，所以它们不能作为集合中的元素
>
> 集合中的元素不能使用下标方式访问，集合也没有索引
>
> 集合主要用于做并、交、差等集合运算，以及基于集合进行元素的快速检索
>
> ==空集合的创建不可以用{}，而应该使用 set()，{}创建的是空字典==

```python
# 创建集合的三种方式
s = {1,2,3,1,2,3,4,5}
fruit = set(("apple", "banana", "cherry")) # 函数创建
fruit = set(["apple", "banana", "cherry"])
li = [1,2,3,1,2,3]
t = set(li) #可迭代对象为参数创建，这是列表去重的一种方式
#将可哈希对象插入集合
s.add(x)
#将可迭代兑现拆分成多个元素再插入集合
s.update(x)
```

###### 集合的运算

> 计算交集：`s1.intersection(s2)`
>
> 计算 s1 和 s2 的交集并返回，此方法不会修改 s1 和 s2 本身的值
>
> 计算并集：`s1.union(s2)`
>
> 计算 s1 和 s2 的并集并返回，此方法不会修改 s1 和 s2 本身的值
>
> 计算差集：`s1.difference(s2)`
>
> 计算 s1 和 s2 的差集并返回，此方法不会修改 s1 和 s2 本身的值
>
> 计算对称差集：`s1.symmetric_difference(s2)`
>
> 计算 s1 和 s2 的对称差集并返回，此方法不会修改 s1 和 s2 本身的值
>
> 子级和父级：`s1.issubset(s2)`
>
> 判断 s1 是否是 s2 的子集。如果是则返回 True，不是则返回 False
>
> 子级和父级：`s1.issuperset(s2)`
>
> 判断 s1 是否是 s2 的父集。如果是则返回 True，不是则返回 False

---

#### 数据类型：Dictionary

> 字典（Dictionary）是另一种无序的对象集合
>
> 但与集合不同，字典是一种映射类型，每个元素是一种映射关系，由 key 和 value 对构成
>
> * 字典的key必须是唯一的，且必须可哈希
> * 字典的value没有特别要求，可以是任意类型
> * 对于不包含任何元素的字典，即{}，称为空字典

```python
#字典的几种创建方式
a = {'one':1, 'two':2, 'three':3}
b = dict(one = 1, two = 2, three = 3)
c = dict(zip(['one','two','three'], [1,2,3])) #zip() 函数合并两个列表，返回一个以元组为元素的新列表
d = dict([('one',1), ('two',2), ('three', 3)]) #与上一条等价
e = dict({'one':1, 'two':2, 'three':3}) #以字典为参数
#第一个参数为键值序列，第二个参数为个元素初值，默认为 None
#但使用此方法后字典中的原有元素都会被清除
d2 = dict().fromkeys(['sno','name','major'], 'Unknown')
#给指定键元素赋值时，如果键不存在则会在字典中插入一个新元素
stu=dict(sno='1810101')
stu['name']='Jane'
#使用 update() 添加或修改元素
stu.update({'name':'LiMing','age':19})
stu.update(name = 'LiHua',major = 'CS')
#字典元素的删除
d=dict(sno='1810100', name='lm', age=19)
del d['age']
name = d.pop('name') #返回字典中键值 name 对应元素的值
```

###### 判断字典中是否存在键

> 语法格式：`d.get(key,default = None)`
>
> 从字典中获取键为 key 的元素的值并返回，如不存在键则返回 default 参数的值，默认为None

###### 拼接两个字典

> 语法格式：`dMerge = dict(d1, **d2)`
>
> 或：
>
> ```python
> dMerge = d1.copy()
> dMerge.update(d2)
> ```

###### 其他操作

```python
#清除所有元素
d=dict(sno='1810100', name='LiHua', age=19)
d.clear()
#获取字典中所有的键
print(d.keys())
#获取字典中所有的值
print(d.values())
#使用 items 方法遍历字典
for key,value in d.items():
  print(key,value)
```

---

#### 切片和列表生成表达式

```python
ls1 = list(range(0,20))
#从 ls1 下标从 3 至 9 的元素中以步长 2 取元素生成一个新列表赋给 ls2
ls2 = ls1[3:10:2]
#每个元素为 x 的二次方，要求 x 为 10 以内的奇数
ls = [x*x for x in range(10) if x % 2 != 0]
#列表生成表达式中支持多层循环
snolist=['1810101','1810102','1810103']
namelist=['赵高','王丽','李明']
ls=['学号'+ sno + '姓名：' + name for sno in snolist for name in namelist]
for stu in ls:
print(stu)
```



---

#### 运算符

###### 占位运算符

> 由于 % 作为占位符的前缀字符，因此对于有占位符的字符串，表示一个 % 时需要写成 “ %% “

```python
print('优秀比例为%.2f%%，良好比例为%.2f%%。' % (5.2, 20.35))
```

![image-20221013204102004](C:\Users\19643\Desktop\AIpython\引用图片\image-20221013204102004.png)

###### 算术运算符

> 在 python 中，// 为整除运算符，** 为幂运算符

###### 逻辑运算符

> 在 python 中，and 为且运算符，or 为或运算符，not 为非运算符

###### 身份运算符 is / is not

> 身份运算符，用于比较两个对象是否对应同样的存储单元
>
> 程序在运行时，输入数据和输出数据都是存放在内存中。内存中的一个存储单元可以存储一个字节的数据，每个存储单元都有一个唯一的编号，称为内存地址。根据数据类型不同，其所占用的内存大小也不同。一个数据通常会占据内存中连续多个存储单元，起始存储单元的地址称为该数据的内存首地址
>
> `x is y` 等价于 `id(x) == id(y)` ，即判断 x 和 y 的内存首地址是否相同；` x is not y` 等价于`id(x) != id(y)`，即判断 x 和 y 的内存首地址是否不同
>
> 如果赋值运算符 “ = ” 的右操作数也是一个变量，则赋值运算后左操作数变量和右操作数变量会对应同样的存储单元
>
> Python 出于性能上的考虑，在解释器启动的时候就已经将 5 到 256 的整数创建到内存中了。而当我们需要创建值在 5 到 256 的 int 数字的时候，Python 并不会新开辟一块新内存去创建数字，而是直接将已存在的对象返回。但是如果新创建的数字不在这个范围，Python 就会为每个变量单独开辟自己的内存空间
>
> 同样是出于对性能的考虑，不过 Python 并没有预先将字符串创建到内存中，而是使用了一种叫 intern 的机制（字符串长度超过20，则不启动），就是同样的字符串对象仅仅会保存一份，是共用的

###### 成员运算符 in / not in

> 成员运算用于判断一个可迭代对象 (序列、集合或字典) 中是否包含某个元素
>
> 使用成员运算符判断一个数据是否是字典中的元素，实际上就是判断该数据是否是字典中某个元素的键

```python
x, y = 15, ['abc', 15, True]
print(x in y) #输出“True”
x = 20
print(x not in y) #输出“True”
y = (20,'Python')
print(x in y) #输出“True ”
x, y = 'Py', 'Python'
print(x in y) #输出“True ”
x, y = 20, {15, 20, 25}
print(x in y) #输出“True ”
x, y = 'one', {'one':1, 'two':2, 'three':3}
print(x in y) #输出“True ”
print(1 in y) #输出“False ”
```

###### 序列运算符

> 用于序列操作的运算符

|  运算符   |                       功能                       |  示例   |
| :-------: | :----------------------------------------------: | :-----: |
| +（拼接） | 将序列 x 和序列 y 中的元素连接，生成一个新的序列 | `x + y` |
| *（重复） |   将序列 x 中的元素重复 n 次，生成一个新的序列   | `x * n` |

---

#### 条件语句

```python
x = 3
if x < 0:
    print("negative")
elif x == 0:
    print("zero")
else:
    print("positive")
```

---

#### pass 语句

> pass 表示一个空操作，只起到一个占位作用，执行时什么都不做
>
> pass 与条件语句并没有直接关系，在程序中所有需要的地方都可以使用 pass 作为占位符。

---

#### 循环语句

###### for 循环

```python
course_python = ["a", "b", "c"]
for course in course_python:
    print(course)
course_python = {"a":1, "b":2, "c":3}
for course in course_python:
    print("%s : %d" % (course, course_python[course]))
for i in range(0, 5, 1): # range(start, end, step)
    print(i)
# range() 函数返回的是一个可迭代对象，通过list函数可将该对象转换为列表
print(list(range(1,5,2))) # 输出：[1, 3]
print(list(range(5,-1,-2))) # 输出：[5, 3, 1]
print(list(range(1,5))) # 输出：[1, 2, 3, 4]
print(list(range(5))) # 输出：[0, 1, 2, 3, 4]
```

###### while 循环

```python
i = 0
while True:
    print(i)
    i += 1
    if i >= 9:
        break
```

###### else 语句

> 在循环语句后面可以接一个 else 分支，当 for 循环和 while 循环因为 break 语句跳出循环时，不会进入 else 分支，否则会进入分支

```python
for n in [12, 17]:
    for k in range(2, int(n ** 0.5)):
        if n % k == 0:
            print("不是素数")
            break
    else:
        print("是素数")
```

###### 索引

> 如果希望不仅获取到每一个元素的值，而且能获取到每一个元素的索引， 则可以通过 `len()` 函数获取可迭代对象中的元素数量，再通过 `range()` 函数生成由所有元素索引组成的可迭代对象。
>
> 也可以利用 `enumerate()` 函数返回的索引序列对象同时获得每个元素的索引和值

```python
courses = ["a", "b", "c"]
for i in range(0, len(courses)):
    print(courses[i])
for i, course in enumerate(courses):
    print(i, course)
```

---

#### 字符串

###### 字符串生成

> 单引号和双引号中的字符串如果分多行写，必须在行尾加上续行符 “ \ ”；如果要求输入多行信息则需要使用换行符“ \n ”；使用三引号创建字符串，则允许直接将字符串写成多行形式
>
> 在一对三引号括起来的字符串中，可以直接包含单引号和双引号，不需要使用转义字符

```python
s1 = 'Hello\
World!' 
s2 = "你好！\n欢迎学习Python语言程序设计！" 
s3 = '''你好！
欢迎学习Python语言程序设计！
祝你学习愉快！'''
```

###### 字符串比较

```python
str1 = 'Python'
str2 = 'C++'
print('str1 小于等于 str2', str1 <= str2)
```

###### 字符串切割

> 使用 split 内置函数可以按照指定的分隔符对字符串进行切割，返回由切割结果组成的列表
>
> `str.split ( sep = None, maxsplit = -1)`
>
> 其中`sep`是指定的分隔符，`maxsplit`决定了最大切割次数，默认值为 -1 表示应切尽切

```python
str1 = 'It is a book!'
str2 = 'Python##C++##Java##PHP'
ls1 = str1.split()
ls2 = str2.split('##') 
ls3 = str2.split('##',2)
```

> 除了 split 方法，字符串中还提供了一个 splitlines 方法，该方法固定以行结束符（'\r'、'\n'、'\r\n'）作为分隔符对字符串进行切割，返回由切割结果组成的列表
>
> `str.splitlines([keepends])`
>
> 其中的`keepends`表示切割结果中是否保留最后的行结束符，如果该参数为 True，则保留行结束符，否则不保留
>
> 现代系统中，=='\r' 用于将光标移至行首，'\n' 兼具此功能，且将光标移至下一行==

###### 字符串检索和替换

> 字符串中提供了以下 4 种字符串检索方法：
>
> `str.find(sub[, start[, end]])` // 从左向右检索，找到 sub ==第一次==出现的位置 (int）
> `str.index(sub[, start[, end]])`// 从右向左检索，找到 sub ==第一次==出现的位置 (int）
> `str.rfind(sub[, start[, end]])` //检索不到时不会返回 -1 而是返回异常，不建议使用
> `str.rindex(sub[, start[, end]])`
>
> 使用字符串中的 replace 方法可以将字符串中的指定字串替换成其他内容，语法格式为：
>
> `str.replace(old, new[,max])` // max 是最多替换的字串数量，默认为替换全部子串
>
> 

###### 字符串其他操作

* 去除字符串空格

  > `str.strip()` //去除头部和尾部空格
  >
  > `str.lstrip()` //去除头部空格
  >
  > `str.rstrip() `//去除尾部空格
  >
  > `str.replace(' ','')` //去除全部空格

* 大小写转换

  > `str.capitalize() `//首字母大写，其他字母小写
  >
  > `str.lower()` //所有字母小写
  >
  > `str.upper() `//所有字母大写
  >
  > `str.swapcase()` //原字符串中小写变大写，大写变小写

* 连接字符串

  > 使用 join 方法将序列中的元素以指定的字符连接成一个新的子串:
  >
  > `str.join(seq)` // str 为连接符，seq 是一个序列对象（如列表）

* format 方法

  > 可以用此方法进行字符串格式化操作，其语法格式为：
  >
  > `str.format(*args,**kwargs)`
  >
  > str 是用于格式化的字符串，可以包含由大括号括住的替换字段。每个字段可以是位置参数的数字索引，也可以是关键字参数的名称
  >
  > ```python
  > str1 = '{0}的计算机成绩是{1}，{0}的数学成绩是{2}'
  > str2 = '{name}的计算机成绩是{cs},{name}的数学成绩是{ms}'
  > print(str1.format('Jane',90,85))
  > print(str2.format(cs = 90, ms = 85,name = 'Jane'))
  > ```
  >
  > 此外，在 format 方法格式化字符串时，字符串的替换字段中可以包含对实参属性的访问：
  >
  > ```python
  > class Student: 
  >   def init (self,name,cs):
  >     self.name = name
  >     self.cs = cs
  > s = Student('Jane',90)
  > str1 = '{0.name}的计算机成绩是{0.cs}' 
  > str2 = '{stu.name}的计算机成绩是{stu.cs}'
  > print(str1.format(s))
  > print(str2.format(stu = s))
  > ```

---

#### 正则表达式的基础语法

###### 部分匹配模式

![屏幕截图 2022-10-14 154956](C:\Users\19643\Desktop\AIpython\引用图片\屏幕截图 2022-10-14 154956.png)

![屏幕截图 2022-10-14 155025](C:\Users\19643\Desktop\AIpython\引用图片\屏幕截图 2022-10-14 155025.png)

![屏幕截图 2022-10-14 155049](C:\Users\19643\Desktop\AIpython\引用图片\屏幕截图 2022-10-14 155049.png)

![屏幕截图 2022-10-14 155110](C:\Users\19643\Desktop\AIpython\引用图片\屏幕截图 2022-10-14 155110.png)

![屏幕截图 2022-10-14 155132](C:\Users\19643\Desktop\AIpython\引用图片\屏幕截图 2022-10-14 155132.png)

> 通常在用于表示正则表达式的字符串前加上一个字符 r，使得后面的字符串忽略转义符。
>
> 例如，对于字符串 '\\bfoo\\b'，可以将它写作 r'\bfoo\b'。
>
> 此外，==数字和下划线被认为是可能出现在单词中的字符！==

---

#### re 模块的使用

###### compile 函数

> `compile()` 函数用于将一个字符串形式的正则表达式编译成一个正则表达式对象，供 `match()`、`search()` 以及其他一些函数使用。
>
> 语法格式：`re.compile(pattern, flags = 0)`
>
> 其中，pattern 是一个字符串类型的正则表达式；flags 指定了匹配选项，可以使用按位或运算符将多个选项连接起来。默认值为 0，表示没有任何匹配选项。
>
> 以下是一些 flags 参数对应的匹配选项：
>
> ![屏幕截图 2022-10-14 162150](C:\Users\19643\Desktop\AIpython\引用图片\屏幕截图 2022-10-14 162150.png)

###### match 函数

> re 模块中的 match 函数用于对字符串开头的若干字符进行正则表达式匹配。匹配成功则返回一个 Match 对象；匹配失败则返回 None。
>
> 语法格式为：`re.match(pattern, string, flags = 0)`
>
> 其中，pattern 是要匹配的正则表达式；string 是要做正则表达式匹配的字符串；flags 与 compile 函数中的 flags 参数含义相同。
>
> ```python
> import re
> result1 = re.match(r'python', 'Python是一门流行的编程语言', re.I)
> result2 = re.match(r'python', '我喜欢学习Python', re.I)
> result3 = re.match(r'python', '''我喜欢学习Python
> Python是一门流行的语言''', re.I|re.M)
> print('result1:',result1)
> print('result2:',result2)
> print('result3:',result3)
> ```
>
> 返回如下：
>
> ```python
> result1: <re.Match object; span=(0, 6), match='Python'>
> result2: None
> result3: None
> ```
>
> 因此，即使制定了匹配选项 re.M，re.Match 函数也只会对字符串开头的若干字符做匹配，而不会对后面行的开头字符做匹配。
>
> 除了直接调用 re 模块中的 match 函数外，也可以使用 compile 函数生成的正则表达式对象实现同样的功能，语法格式为：
>
> `Pattern.match(match(string[,pos[,endpos]]))`
>
> ```python
> import re
> pattern = re.compile(r'python', re.I) 
> result1 = pattern.match('Python是一门流行的编程语言')
> result2 = pattern.match('我喜欢学习Python！',5)
> print('result1:',result1)
> print('result2:',result2)
> ```
>
> ```python
> result1: <re.Match object; span = (0, 6), match = 'Python'>
> result2: <re.Match object; span = (5, 11), match = 'Python'>
> ```

###### search 函数

> search 函数与 match 函数参数形式完全相同，不同之处在于 search 函数可以对整个字符串从左向右找到第一个匹配的字符序列。
>
> 同 pattern.match 方法一样，也可以使用 compile 函数返回的正则表达式对象中的 search 方法实现 search 函数同样的功能，其语法格式与 pattern.match 完全相同。

###### 匹配对象

> Match 对象提供了多种方法，这里仅学习 group，groups，start，end 几种方法的使用

![屏幕截图 2022-10-14 193949](C:\Users\19643\Desktop\AIpython\引用图片\屏幕截图 2022-10-14 193949.png)

```python
import re
str='''sno:#1810101#,name:#LiHua#,age:#19#,major:#CS#
sno:#1810102#,name:#ZhangXia#,age:#20#,major:#Mathematic#'''
rlt = re.search(r'name:#([\s\S]*?)#[\s\S]*?major:#([\s\S]*?)#',str, re.I)
if rlt: 
  print('whole str：', rlt.group())
  print('name:%s, startpos:%d, endpos:%d'%(rlt.group(1),rlt.start(1), rlt.end(1)))
  print('major:%s, startpos:%d, endpos:%d'%(rlt.group(2),rlt.start(2), rlt.end(2)))
  print('match result：', rlt.groups())
else:
  print('Fail')
```

###### findall

> re 模块中的 findall 函数用于在字符串中找到所有与正则表达式匹配的子串。
>
> 语法格式：`re.findall(pattern, string, flags = 0)`
>
> 各参数含义与 re.match 和 re.search 函数完全相同。如果匹配成功，则将匹配的数据以列表的形式返回；如果匹配失败，返回空列表。
>
> ```python
> import re
> str='''sno:#1810101#,name:#LiHua#,age:#19#,major:#CS#
> sno:#1810102#,name:#ZhangXia#,age:#20#,major:#Mathematic#'''
> rlt = re.findall(r'name:#([\s\S]*?)#[\s\S]*?major:#([\s\S]*?)#',str, re.I)
> print(rlt)
> ```
>
> 

###### finditer

> re 模块中的 finditer 函数与 findall 函数功能完全相同，唯一区别在于 findall 函数返回列表形式的结果，而finditer 返回迭代器形式的结果，其中每一个元素都是一个 Match 对象。
>
> 语法格式：`re.finditer(pattern, string, flags)`
>
> ```python
> import re
> str='''sno:#1810101#,name:#LiHua#,age:#19#,major:#CS#
> sno:#1810102#,name:#ZhangXia#,age:#20#,major:#Mathematic#'''
> rlt1 = re.finditer(r'name:#([\s\S]*?)#[\s\S]*?major:#([\s\S]*?)#',str, re.I)
> rlt2=re.finditer(r'department:#([\s\S]*?)#', str, re.I)
> print('rlt1:')
> for r in rlt1:
> print(r)
> print('rlt2:')
> for r in rlt2:
> print(r)
> ```
>
> 

###### split、sub 和 subn

> re 模块中的 split() 函数用于将字符串按与正则表达式匹配的子串分割。
>
> 语法格式：`re.split(pattern,string,maxspilt,flags = 0)`
>
> ```python
> str='sno:1810101,name:LiHua,age:19,major:CS'
> rlt = re.split(r'\W+',str)
> print(rlt)
> ```
>
> re 模块中的 sub() 函数用于替换字符串中与正则表达式匹配的子串。
>
> 语法格式：`re.sub(pattern,repl,string,count = 0,flags = 0)`
>
> 其中 repl 是要将匹配子串替换成的字符串。
>
> ```python
> html = '''<h3 class="c-title">
> <a href="http://tttt.html"><em>PekingUniversity</em>LiWenyue</a>
> </h3>'''
> content = re.sub(r'<[^<]*>', '', html)
> content=content.strip() 
> print(content)
> ```
>
> subn() 函数与 sub() 函数用法格式完全相同，只是 subn() 函数会返回一个包含新字符串和替换次数的元组。 

---

#### 函数

###### 不定长参数

> 不定长参数，即在调用函数时可以接收任意数量的实参，这些实参在传递给函数时会被封装成元组（位置参数）或字典（关键字参数）形式。
>
> 一般情况下，不定长参数放在参数列表最后。对于使用位置参数形式的不定长参数，允许普通形参放在不定长参数的后面，但此时要求在调用函数时不需使用关键字参数方式给不定长参数后面的形参传递实参。
>
> 带不定长参数的函数定义方法：
>
> def 函数名([普通形参列表，] *不定长参数名[，普通形参列表])：#封装为元组
>
> def 函数名([普通形参列表，] **不定长参数名)：                           #封装为字典

###### 拆分参数列表

> 如果函数所需要的参数已经存储在了列表、元组或字典中，则可以直接从列表、元组或字典中拆分出函数所需要的参数。
>
> 其中列表、元组拆分出来的结果作为位置参数，字典拆分出来的结果作为关键字参数。
>
> ```python
> def SumVal(*args): 
>   sum = 0
>   for i in args:
>     sum += i
>   print('求和结果为：',sum)
> ls=[3,5.2,7,1]
> SumVal(*ls) #等价于 SumVal(3,5.2,7,1)
> 
> def StudentInfo(name, chineselevel, country):
>     print('姓名：%s，中文水平：%s，国家：%s'%(name,chineselevel,country))
> d={'country': '中国', 'chineselevel':'良好', 'name':'李华'}
> StudentInfo(**d) #等价于StudentInfo(country='中国',chineselevel='良好', name='李华')
> ```
>
> ###### 返回值
>
> > 如果在函数中返回多个值，则这些值会被封装成一个元组被返回。

---

#### 模块概述和 import 语句

> Python 提供了交互式和脚本式两种运行方式，当要执行的代码比较长、且需要重复使用时，通常将代码放在扩展名为 .py 的 Python 脚本文件中。这些脚本文件就是模块（Module）。
>
> 当要使用一个模块中的某些功能时，可以通过 import 方式将该模块导入。
>
> 导入模块后，如果要使用该模块中定义的标识符，则需要通过 模块名.标识符名 来访问。

---

#### 全局变量  \__name__  和系统模块 

###### 全局变量 \__name__

> 每个模块中都有一个全局变量 \__name__。
>
> \__name__ 的作用是获取当前模块的名称，如果当前模块时单独执行的，则其  \__name__ 的值就是\__main__ ；否则，如果是作为模块导入，则其 \__name__ 的值就是模块的名字

###### 系统模块

> 可以直接导入系统提供的模块，使用其中的功能
>
> 例：通过 sys 模块获取运行 Python 脚本时传入的参数
>
> ```python
> import fibo 
> import sys
> n = int(sys.argv[1]) #可在命令行中赋值参数，如：python testfibo.py 5
> fibo.PrintFib(n) 
> ls = fibo.GetFib(n)
> print(ls) 
> ```

---

#### from...import

> 除了使用 import 将整个模块导入，也可以使用 from import 将模块中的标识符（变量名、函数名等）直接导入当前环境，这样在访问这些标识符时就不需要再指定模块名。
>
> 语法格式：`from 模块名 import 标识符1，标识符2，...，标识符 N`
>
> 如果要导入一个模块中的所有标识符，也可以使用 "from 模块名 import *"。在此情况下，如果一个模块定义了列表\__all__ ，则只能导入该列表中存在的标识符（此列表只能在模块第一行中定义）。
>
> 可以使用 as 为模块或标识符起别名
>
> ```python
> import fibo as f 
> f.PrintFib(5)
> from fibo import PrintFib as pf
> pf(5)
> ```
>
> 

---

### 面向对象

#### 类属性

```python
class Student:
    name = 'Unknown'
Student.name = '学生'
stu = Student()
stu.name = '马红'
#即：类属性和对象属性可以分别赋值
```

###### 私有属性

> 在定义类时，如果一个类属性名是以 __ 开头，则该类属性为私有属性在类外无法直接访问。但如果硬要访问，则可以在私有属性名前加上：`_类名`
>
> ```python
> print('身份证号：'%stu._Student__id)
> #其中 __id 是 Student 的一个私有属性
> ```
>
> 

#### 类中普通方法定义及调用

> 在定义类的普通方法时，要求第一个参数需要对应调用方法所使用的实例对象（ 一般为 self ）。在通过类的实例对象调用类中的普通方法时，并不需要传入 self 参数的值， self 会自动对应调用该方法时所使用的对象。
>
> ```python
> class Student: 
>   name='Unknown' 
>   def SetName(self, newname): 
>     self.name=newname 
>   def PrintName(self): 
>     print('姓名: %s'%self.name) 
> if __name__ == '__main__':
>   stu1 = Student() 
>   stu2 = Student() 
>   stu1.SetName('=>?')
>   stu2.SetName('CD') 
>   stu1.PrintName() 
>   stu2.PrintName() 
> ```
>
> 类的普通方法不能通过类名直接调用。

#### 构造方法

> 构造方法是 Python 内置方法之一，它的方法名为`__init__`，在创建一个类对象时会自动执行，负责完成新创建对象的初始化工作。
>
> ```python
> class Student: 
>   def __init__ (self): 
>     print('构造方法被调用！')
>     self.name = '未知' 
>   def PrintInfo(self): 
>     print('姓名：' % self.name) 
> if __name__ ==' main ':
>   stu = Student() 
>   stu.PrintInfo() 
> ```
>
> 

#### 析构方法

> 析构方法是类的另一个内置方法，其方法名为`__del__`，负责完成待销毁对象的资源清理工作。类对象的销毁有如下三种情况：
>
> * 调用了函数，其中局部变量的作用域结束
> * 使用 del 删除对象
> * 程序结束时程序中的所有对象都将被销毁
>
> 注意：如果多个变量对应同一片内存空间，则只有这些变量都删除后，才会销毁这片内存空间中所保存的对象，也才会自动执行析构方法：
>
> ```python
> class Student: 
>   def __init__ (self,name): 
>     self.name = name 
>     print('姓名为%s的对象被创建！' % self.name)
>   def __del__ (self): 
>     print('姓名为%s的对象被销毁！' % self.name)
>   def func(name):
>     stu = Student(name) 
>  if name =='__main__':
>    stu1 = Student('李晓明') 
>    stu2 = Student('马红') 
>    stu3 = stu2
>    del stu2 
>    func('张刚') 
>    del stu3 
>    stu4 = Student('刘建') 
> ```
>
> 

#### `__str__`内置方法

> 调用 str() 函数对类对象进行处理时或者调用 Python 内置函数 format() 和 print() 时自动执行，`__str__`方法的返回值必须是字符串。
>
> ```python
> class Complex:
>     def __init__(self, real, image):
>         self.real = real
>         self.image = image
>     def __str__(self):
>         return str(self.real) + '+' + str(self.image) + 'i'
> if __name__ == '__main__':
>     c = Complex(3.2, 5.3)
>     print(c)
> ```
>
> 

#### 对象间比较运算的内置方法

> ![屏幕截图 2022-10-28 162740](C:\Users\19643\Desktop\AIpython\引用图片\屏幕截图 2022-10-28 162740.png)
>
> ```python
> class Student:
>   def __init__ (self, name, age): 
>     self.name=name
>     self.age=age 
>   def __le__ (self, other):
>      return self.age <= other.age
> if __name__ == '__main__’:
>   stu1 = Student('李晓明',19) 
>   stu2 = Student('马红',20) 
>   print(stu2 <= stu1)
> ```
>
> 

---

#### 继承

> 基于已有的类创建新的类。
>
> 子类继承父类中定义的所有属性和方法，也能在子类中增加新的属性和方法。
>
> 一个子类可能有多个父类，这种继承关系为多重继承。

###### 子类的定义

```python
class Person: 
  def SetName(self, name): 
    self.name = name 
class Student(Person): 
  def SetSno(self, sno): 
    self.sno = sno 
class Teacher(Person):
  def SetTno(self, tno): 
    self.tno = tno 
class TA(Student,Teacher): 
  def SetTeacher(self, teacher): 
    self.teacher = teacher 
if __name__ == '__main__':
    stu = Student()
    stu.SetSno('1810100')
    stu.SetName('李晓明')
    print(stu.sno, stu.name)
```

###### 方法重写

> 子类可以对从父类中继承过来的方法进行重新定义，使得子类对象可以表现出与父类对象不同的行为。
>
> ```python
> class Person: 
>   def __init__ (self, name):
>     self.name = name
>   def PrintInfo(self):
>     print('姓名：', self.name)
> class Student(Person): 
>   def init (self, sno, name):
>     self.sno = sno
>     self.name = name 
>   def PrintInfo(self):
>     print('学号：', self.sno, '姓名：', self.name)
> if __name__ =='__main__':
>   p = Person('李晓明')
>   stu = Student('1810100','马红') 
>   p.PrintInfo()
>   stu.PrintInfo()
> ```
>
> 多态，是指在执行同样代码的情况下，系统会根据对象实际所属的类去调用相应类中的方法。

###### 鸭子类型

> 在 Python 中编写一个函数，传递实参前其参数的类型并不确定，用形参进行操作时只要传入的对象能够支持该操作，程序就能正常运行。
>
> 传入实参后，参数类型确定，实际运行时程序会寻找参数对象所属的类并在那个类中寻找已设定的方法。
>
> Python 的 “多态” 机制就是利用鸭子类型实现的，但它和 C++ 中的多态含义不同。

###### Super 方法

> super 方法用于获取父类的代理对象，以执行已在子类中被重写的父类方法，其语法格式为：
>
> `super([类名][，对象名或类名])`
>
> 第一个参数是要获取父类代理对象的类名
>
> 第二个参数如果传入对象名，则其所属的类必须是第一个参数指定的类或该类的子类，找到的父类对象的 self 会绑定到这个对象上；如果传入类名，则该类必须是第一个参数指定的类的子类。
>
> 在一个类 A 的定义中调用 super 方法时，可以将两个参数都省略，此时，super() 等价于 super(A, self)，即获取 A 的父类代理对象。且获取到的父类代理对象中的 self 绑定到当前 A 类对象的 self 上。
>
> ```python
> class Person:
>     def __init__(self, name):
>         print('Person类构造方法被调用！')
>         self.name = name
> class Student(Person):
>     def __init__(self, sno, name):
>         print('Student类构造方法被调用！')
>         super().__init__(name)
>         self.sno = sno
> class Postgraduate(Student):
>     def __init__(self,sno, name, tutor):
>         print('Postgraduate类构造方法被调用！')
>         super().__init__(sno, name)
>         self.tutor = tutor
> pg = Postgraduate('1810100', '李晓明'，'马红')
> print(pg.sno,pg.name,pg.tutor)
> ```
>
> 

###### 内置函数 isinstance、issubclass 和 type

```python
isinstance(stu, Person) # stu 是否是 Person 类或其子类对象
issubclass(Student,Person) # Student 是否是 Person 的子类
type(stu) #stu 所属的类
type(stu) == Student #stu 是否属于类 Student
```

---

#### 类方法

> 类方法是指使用`@classmethod` 修饰的方法，其第一个参数是类本身。类方法的特点是既可以通过类名直接调用，也可以通过类的实例对象调用。
>
> ```python
> class Complex:
>     def init (self,real=0,image=0):
>         self.real=real
>         self.image=image
>     @classmethod
>     def add(cls,c1,c2):
>         print(cls)
>         c=Complex()
>         c.real=c1.real+c2.real
>         c.image=c1.image+c2.image
>         return c
> c1=Complex(1,2.5)
> c2=Complex(2.2,3.1)
> c=Complex.add(c1,c2) 
> print(c.real,c.image)       
> ```
>
> 

#### 静态方法

> 静态方法是指使用`@staticmethod` 修饰的方法，既可以通过类名直接调用，也可以通过类的实例对象调用。但静态方法中没有类方法中的第一个类参数。
>
> ```python
> class Complex:
>     def init (self,real=0,image=0):
>         self.real=real
>         self.image=image
>     @staticmethod
>     def add(c1,c2):
>         c=Complex()
>         c.real=c1.real+c2.real
>         c.image=c1.image+c2.image
>         return c
> c1 = Complex(1,2.5)
> c2 = Complex(2.2,3.1)
> c = Complex.add(c1,c2) 
> print(c.real,c.image)  
> ```
>
> 

---

### Numpy 模块

#### N 维数组对象：ndarray

> ndarray 数组要求所有元素类型相同，数组下标从 0 开始。在程序中的别名是 array。
>
> ```python
> import numpy as np
> a = np.array([0,1,2,3,4],[9,8,7,6,5])
> print(a)
> ```

#### ndarray 对象的属性

![屏幕截图 2022-10-30 115344](C:\Users\19643\Desktop\AIpython\引用图片\屏幕截图 2022-10-30 115344.png)

#### ndarray 的元素类型

![屏幕截图 2022-10-30 115540](C:\Users\19643\Desktop\AIpython\引用图片\屏幕截图 2022-10-30 115540.png)

![屏幕截图 2022-10-30 115636](C:\Users\19643\Desktop\AIpython\引用图片\屏幕截图 2022-10-30 115636.png)

![屏幕截图 2022-10-30 115653](C:\Users\19643\Desktop\AIpython\引用图片\屏幕截图 2022-10-30 115653.png)

#### ndarray 数组的创建方法

> * 从 Python 中的列表、元组等类型创建 ndarray 数组，并且可以指定 dtype。
>
>   语法格式：`x = np.array(list/tuple, dtype = np.float32)`
>
>   ```python
>   x = np.array([[1,2],[9,8],(3,4)], dtype = np.uint64)
>   print(x)
>   ```
>
> * 使用 Numpy 中的函数创建 ndarray 数组
>
>   ![屏幕截图 2022-10-30 120545](C:\Users\19643\Desktop\AIpython\引用图片\屏幕截图 2022-10-30 120545.png)
>
>   ![屏幕截图 2022-10-30 120708](C:\Users\19643\Desktop\AIpython\引用图片\屏幕截图 2022-10-30 120708.png)
>
>   ![屏幕截图 2022-10-30 120835](C:\Users\19643\Desktop\AIpython\引用图片\屏幕截图 2022-10-30 120835.png)

#### ndarray 数组的变换

> ![屏幕截图 2022-10-30 135802](C:\Users\19643\Desktop\AIpython\引用图片\屏幕截图 2022-10-30 135802.png)
>
> * `.astype(new_type)`方法可以创建基于原数组的新的数组，数据内容相同，但类型不一定相同（可指定）
>
> * `.tolist()`方法可将数组转化为列表形式。
>
> * ```python
>   import numpy as np
>   a = np.full((2,3,4),25)
>   print(a.tolist())
>   ```

#### ndarray 数组的索引和切片

> * 一维数组的索引和切片，与列表相同。
>
> * 多维数组的索引和切片：
>
>   ![屏幕截图 2022-10-30 141610](C:\Users\19643\Desktop\AIpython\引用图片\屏幕截图 2022-10-30 141610.png)
>
>   ![屏幕截图 2022-10-30 142040](C:\Users\19643\Desktop\AIpython\引用图片\屏幕截图 2022-10-30 142040.png)
>
>   注意：
>
>   * 每一维度上和一维数组处理方法一样，都有起始索引，终止索引（不含），步长三个参数，如果一个参数都没有则用 : 占位。
>   * 仔细阅读上面的例子，体会多维数组切片中使用 ：占位的方法。

#### ndarray 数组的运算

> * 数组与标量之间的运算作用于数组的每一个元素
>
>   ![屏幕截图 2022-10-30 142619](C:\Users\19643\Desktop\AIpython\引用图片\屏幕截图 2022-10-30 142619.png)
>
> * numpy 中一些用于元素间运算的函数：
>
>   ![屏幕截图 2022-10-30 143138](C:\Users\19643\Desktop\AIpython\引用图片\屏幕截图 2022-10-30 143138.png)
>
>   ![屏幕截图 2022-10-30 143154](C:\Users\19643\Desktop\AIpython\引用图片\屏幕截图 2022-10-30 143154.png)
>
>   ![屏幕截图 2022-10-30 143210](C:\Users\19643\Desktop\AIpython\引用图片\屏幕截图 2022-10-30 143210.png)
>
>   其中 `np.modf()`返回一个由两个数组组成的元组。

#### 数据的 CSV 文件存取

> * `np.savetxt(frame, array, fmt = '%.18e', delimiter = None)`
>   * frame：文件名
>   * array：要存入文件的数组
>   * fmt：写入文件的格式，如 %d，%.2f 等
>   * delimiter：分割字符串，默认为空格，需要设置为逗号
> * `np.loadtxt(frame, dtype = np.float, delimiter = None, unpack = False)`
>   * frame：文件名
>   * dtype：数据类型，可选
>   * delimiter：分割字符串，默认为空格，需设定为逗号
>   * unpack：如果为 True，读入属性将分别写入不同变量

#### 多维数据存取

> * `a.tofile(frame, sep = '', format = '%s')`
>   * `frame`：文件、字符串
>   * `sep`：数据分割字符串，如果是空串，写入文件为二进制
>   * `format`：写入数据的格式
>   * a 是一个 np 对象
> * `np.fromfile(frame, dtype = float, count = -1, sep = '')`
>   * `dtype`：读取的数据类型
>   * `count`：读入元素个数，-1 表示读入整个文件
>   * `sep`：同上
>
> Numpy 的便捷文件存储：
>
> * `np.save(fname, array)`
> * `np.load(fname)`
>   * fname：文件名，以 .npy 为扩展名，压缩扩展名为 .npz
>
> 

#### Numpy 的随机函数

![屏幕截图 2022-11-07 193314](C:\Users\19643\Desktop\AIpython\引用图片\屏幕截图 2022-11-07 193314.png)

![屏幕截图 2022-11-07 193550](C:\Users\19643\Desktop\AIpython\引用图片\屏幕截图 2022-11-07 193550.png)

![屏幕截图 2022-11-07 193811](C:\Users\19643\Desktop\AIpython\引用图片\屏幕截图 2022-11-07 193811.png)

#### Numpy 的统计函数

![屏幕截图 2022-11-07 193937](C:\Users\19643\Desktop\AIpython\引用图片\屏幕截图 2022-11-07 193937.png)

![屏幕截图 2022-11-07 194528](C:\Users\19643\Desktop\AIpython\引用图片\屏幕截图 2022-11-07 194528.png)

###### 关于 numpy 中的 axis 参数

> * `axes`：np 数组中的维度
> * `rank`：np 数组中维度的数量
> * `axis`：标识 np 数组中某一个维度，可以将它当成坐标轴
> * `lenth`：数组某个维度上元素的个数
>
> 归结为一句话：**设 `axis = i` , 则 numpy 沿着第 i 个下标变化的方向进行操作**

#### Numpy 的梯度函数

`np.gradient(f)`：计算数组 f 中元素的梯度，当 f 为多维时，返回每个维度的梯度。

#### 图像的数组表示

> PIL 库是一个具有强大图像处理能力的第三方库。`Image` 是 PIL 库中代表一个图像的类。
>
> 图像是一个由像素组成的二维矩阵，每个元素是一个 RGB 值。
>
> 示例：
>
> ![屏幕截图 2022-11-07 202638](C:\Users\19643\Desktop\AIpython\引用图片\屏幕截图 2022-11-07 202638.png)

---

### Matplotlib 库的使用

#### plot 函数

`plt.plot(x, y, format_string, **kwargs)`

* x：x 轴数据，列表或数组，可选
* y：y 轴数据，列表或数组
* format_string：控制曲线的格式字符串，可选
* **kwargs：第二组或更多 （x，y，format_string）

当绘制多条曲线时，各条曲线的 x 不能忽略。

示例：

![屏幕截图 2022-11-07 213057](C:\Users\19643\Desktop\AIpython\引用图片\屏幕截图 2022-11-07 213057.png)

![屏幕截图 2022-11-07 213133](C:\Users\19643\Desktop\AIpython\引用图片\屏幕截图 2022-11-07 213133.png)

![屏幕截图 2022-11-07 213133](C:\Users\19643\Desktop\AIpython\引用图片\屏幕截图 2022-11-07 213133.png)

![屏幕截图 2022-11-07 213316](C:\Users\19643\Desktop\AIpython\引用图片\屏幕截图 2022-11-07 213316.png)

![屏幕截图 2022-11-07 213327](C:\Users\19643\Desktop\AIpython\引用图片\屏幕截图 2022-11-07 213327.png)

































































