# 1.python第一个程序

'Hello,World!' 中文意思是“你好，世界”。因为 计算机语言之母C语言中使用它做为第一个演示程序，后来的程序员在学习编程或进行设备调试时都将以输出hello world为是否成功（hello world也是程序员学习的新计算机语言的仪式感）

在编辑器里输入

    print("hello world!")

输出结果将显示

    hello world!

# 2.行与缩进

python最具特色的就是使用缩进来表示代码块，不需要使用大括号 {} 。

缩进的空格数是可变的，但是同一个代码块的语句必须包含相同的缩进空格数。实例如下：

    if True:
        print ("True")
    else:
        print ("False")

一般我是使用tab键进行缩进
以下代码最后一行语句缩进数的空格数不一致，会导致运行错误：

    if True:
        print ("Answer")
        print ("True")
    else:
        print ("Answer")
      print ("False")    # 缩进不一致，会导致运行错误

以上程序由于缩进不一致，执行后会出现类似以下错误：

    File "test.py", line 6
    print ("False")    # 缩进不一致，会导致运行错误
                                      ^
    IndentationError: unindent does not match any outer indentation level


# 3.基本语法
## print()函数
print()函数是python里最基本的函数，用于输出到屏幕。在上面运行的`print("hello world!")`中，只要在`print()`括号里输入任何内容，都将输出到屏幕，例如`print("我爱学python")`（手动狗头）屏幕将输出`我爱学python`

## 数据类型

还是以"print("hello world!")"为例，为什么括号里要加`""`符号？因为在python的基本数据类型中一共有两种，数字和字符串

### 基本数据类型--数字(number)

python 数字又分为4种类型：

+ __int__ (整数), 如 1, 只有一种整数类型 int，表示为长整型
+ __bool__ (布尔), 如 True和False，1等于True，0等于False
+ __float__ (浮点数), 如 1.23、3E-2
+ __complex__ (复数), 如 1 + 2j、 1.1 + 2.2j __(这个我从来还没用过，简单了解一下即可)__

### 基本数据类型--字符串(string)

+ Python 中单引号 `'` 和双引号 `"` 使用完全相同。
+ 使用三引号`('''` 或 `""")`可以指定一个多行字符串。
+ 转义符 `\`。
+ 反斜杠可以用来转义，使用 `r` 可以让反斜杠不发生转义。 如 r"this is a line with \n" 则 `\n` 会显示，并不是换行。
+ 按字面意义级联字符串，如 `"this " "is " "string"` 会被自动转换为 `this is string。`
+ 字符串可以用 `+` 运算符连接在一起，用 `*` 运算符重复。
+ Python 中的字符串有两种索引方式，从左往右以 `0` 开始，从右往左以 `-1` 开始。
+ Python 中的字符串不能改变。
+ Python 没有单独的字符类型，一个字符就是长度为 1 的字符串。
+ 字符串的截取的语法格式如下：`变量[头下标:尾下标:步长]`


        word = '字符串'
        sentence = "这是一个句子。"
        paragraph = """这是一个段落，
        可以由多行组成"""  

__实例__

    #!/usr/bin/python3
 
    str='123456789'
 
    print(str)                 # 输出字符串
    print(str[0:-1])           # 输出第一个到倒数第二个的所有字符
    print(str[0])              # 输出字符串第一个字符
    print(str[2:5])            # 输出从第三个开始到第五个的字符
    print(str[2:])             # 输出从第三个开始后的所有字符
    print(str[1:5:2])          # 输出从第二个开始到第五个且每隔一个的字符（步长为2）
    print(str * 2)             # 输出字符串两次
    print(str + '你好')         # 连接字符串
    
    print('------------------------------')
    
    print('hello\nrunoob')      # 使用反斜杠(\)+n转义特殊字符
    print(r'hello\nrunoob')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义

这里的 r 指 raw，即 raw string，会自动将反斜杠转义，例如：

    >>> print('\n')       # 输出空行

    >>> print(r'\n')      # 输出 \n
    \n
    >>>

以上实例输出结果：

    123456789
    12345678
    1
    345
    3456789
    24
    123456789123456789
    123456789你好
    ------------------------------
    hello
    runoob
    hello\nrunoob


### 其他数据类型

#### 空行
函数之间或类的方法之间用空行分隔，表示一段新的代码的开始。类和函数入口之间也用一行空行分隔，以突出函数入口的开始。

空行与代码缩进不同，空行并不是 Python 语法的一部分。书写时不插入空行，Python 解释器运行也不会出错。但是空行的作用在于分隔两段不同功能或含义的代码，便于日后代码的维护或重构。

__记住__：空行也是程序代码的一部分。

#### 等待用户输入

__实例__
    
    input("\n\n按下 enter 键后退出。")

以上代码中 ，\n\n 在结果输出前会输出两个新的空行。一旦用户按下 enter 键时，程序将退出。

#### 同一行显示多条语句
Python 可以在同一行中使用多条语句，语句之间使用分号 `;` 分割，以下是一个简单的实例：
__实例__

    import sys; x = 'runoob'; sys.stdout.write(x + '\n')

使用脚本执行以上代码，输出结果为：

    runoob

#### 多个语句构成代码组

缩进相同的一组语句构成一个代码块，我们称之代码组。

像if、while、def和class这样的复合语句，首行以关键字开始，以冒号( : )结束，该行之后的一行或多行代码构成代码组。

我们将首行及后面的代码组称为一个子句(clause)。

如下实例：

    if expression : 
       suite
    elif expression : 
       suite 
    else : 
       suite

#### print 输出

`print` 默认输出是换行的，如果要实现不换行需要在变量末尾加上 `end=""：`

__实例__

    x="a"
    y="b"
    # 换行输出
    print( x )
    print( y )
     
    print('---------')
    # 不换行输出
    print( x, end=" " )
    print( y, end=" " )
    print()

以上实例执行结果为：

    a
    b
    ---------
    a b

#### import 与 from...import

在 python 用 `import` 或者 `from...import` 来导入相应的模块。

将整个模块(somemodule)导入，格式为： `import somemodule`

从某个模块中导入某个函数,格式为： `from somemodule import somefunction`

从某个模块中导入多个函数,格式为： `from somemodule import firstfunc, secondfunc, thirdfunc`

将某个模块中的全部函数导入，格式为： `from somemodule import *`

__导入 sys 模块__

    import sys
    print('================Python import mode==========================')
    print ('命令行参数为:')
    for i in sys.argv:
        print (i)
    print ('\n python 路径为',sys.path)

__导入 sys 模块的 argv,path 成员__

    from sys import argv,path  #  导入特定的成员
 
    print('================python from import===================================')
    print('path:',path) # 因为已经导入path成员，所以此处引用时不需要加sys.path
