def add(a,b):
    print("计算两个数的和：{0},{1},{2}".format(a,b,(a+b)))
    return a+b
def test02():
    print("A")
    print("B")
    return   #return两个作用：1 返回值。2结束函数的执行
    print("hello")
def test03(x,y,z):
    return [x*10,y*10,z*10]

c=add(30,40)
print(c)
print(add(20,30)*10)
test02()
print(test03(4,3,2))