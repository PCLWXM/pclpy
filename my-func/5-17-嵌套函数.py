def outer():
    print("outer running")

    def inner01():
        print("inner01 running")
    inner01()
outer()

#使用嵌套函数避免重复代码
def printChineseName(name,familyName):
    print("{0} {1}".format(familyName,name))
def printEnglishName(name,familyName):
    print("{0} {1}".format(name, familyName))

#使用1 个函数代替上面的两个函数
def printName(isChinese,name,familyName):
    def inner_print(a,b):
        print("{0} {1}".format(a,b))
    if isChinese:
        inner_print(familyName,name)
    else:
        inner_print(name,familyName)
printName(True,"小七","高")
printName(False,"George","Bush")