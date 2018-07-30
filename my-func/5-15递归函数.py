def test01():
    print("test01")
    test02()

def test02():
    print("test02")

test01()

print("**************************")
def test01(n):
    print("test01:",n)
    if n==0:
        print("over")
    else:
        test01(n-1)


def test02():
    print("test02")

test01(4)

print("er**************************")
def test01(n):
    print("test01:",n)
    if n==0:
        print("over")
    else:
        test01(n-1)

    print("test01***",n)
    
def test02():
    print("test02")

test01(4)