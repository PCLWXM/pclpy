a = 3    #全局变量

def test01():
    b = 4      #局部变量
    print(b*10)
#    a = 300
#    print(a)   #这里的a是局部变量

    global a   #如果在函数中改变全局变量的值，加global关键字声明
    a = 300
    print(locals())    #打印输出的局部变量
    print(globals())   #打印输出的全局变量

test01()
test01()
print(a)
#print(b)   #局部变量