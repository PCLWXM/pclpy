a = [10,20]

print(id(a))
print(a)
print("***********************")
def test01(m):
    print(id(m))
    a.append(300)
    print(id(m))

test01(a)
print(a)