def test01(a,b,c,d):
    print("{0}-{1}-{2}-{3}".format(a,b,c,d))

def test02(a,b,c=10,d=15):     #默认参数必须位于其它参数后面
    print("{0}-{1}-{2}-{3}".format(a,b,c,d))

test01(10,20,30,40)   #位置参数

test01(d=20,b=40,a=10,c=100)  #命名参数，通过形参名称来匹配
test02(2,3)
test02(2,3,4)
